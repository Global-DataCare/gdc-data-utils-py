# Flow contract: reuse canonical claim catalogs; keep logical claims separate from physical storage keys.

import os
from pathlib import Path

import gdc_data_utils

from gdc_data_utils import (
    CLAIMS_BY_RESOURCE,
    ALL_CLAIM_KEYS,
    DiagnosticReportClaim,
    ChargeItemClaim,
    InvoiceClaim,
    ResearchSubjectClaim,
    TaskClaim,
    FlagClaim,
    canonical_claim_for_search_parameter,
    normalize_fhir_api_claims,
    storage_key_for_claim,
    IPS_FHIR_R4_VERSION,
    IPS_CANONICAL_FLAT_CLAIMS_BY_RESOURCE,
    IPS_PROFILE_CATALOG,
    IPS_RESOURCE_CAPABILITIES,
    IPS_VALUE_SET_CATALOG,
    IPS_VERSION,
)
from gdc_data_utils.catalog_generation import (
    extract_claim_catalog,
    extract_claim_definitions,
    extract_ips_catalog,
    extract_ips_value_sets,
)



def _common_utils_root() -> Path:
    configured = os.environ.get("GDC_COMMON_UTILS_ROOT")
    return Path(configured) if configured else Path(__file__).parents[2] / "gdc-common-utils-ts"


def test_diagnostic_report_text_keeps_flat_claim_and_search_layers_distinct() -> None:
    assert DiagnosticReportClaim.CODE_TEXT == "DiagnosticReport.code-text"
    assert canonical_claim_for_search_parameter("DiagnosticReport", "code:text") == (
        DiagnosticReportClaim.CODE_TEXT
    )
    assert storage_key_for_claim(DiagnosticReportClaim.CODE_TEXT) == (
        "diagnosticreport_code-text"
    )
    assert storage_key_for_claim(DiagnosticReportClaim.CODE_TEXT) != (
        "diagnosticreport_code_text"
    )


def test_contextual_claim_normalization_preserves_flat_fhir_like_keys() -> None:
    claims = normalize_fhir_api_claims(
        {
            "@context": "org.hl7.fhir.api",
            "org.hl7.fhir.api.DiagnosticReport.code-text": "diagnostico local",
        }
    )

    assert claims == {
        "@context": "org.hl7.fhir.api",
        "DiagnosticReport.code-text": "diagnostico local",
    }


def test_storage_normalization_rejects_non_claim_keys() -> None:
    for invalid in ("", "code-text", "DiagnosticReport", "DiagnosticReport."):
        try:
            storage_key_for_claim(invalid)
        except ValueError:
            continue
        raise AssertionError(f"expected ValueError for {invalid!r}")


def test_generated_catalog_matches_gdc_common_utils_typescript() -> None:
    common_utils_root = _common_utils_root()
    extracted = extract_claim_catalog(
        common_utils_root / "src/models/interoperable-claims"
    )

    assert len(extracted) >= 20
    assert CLAIMS_BY_RESOURCE == extracted
    assert {
        "ChargeItem.supporting-information",
        "ChargeItem.subject",
        "ChargeItem.occurrence",
    } <= set(CLAIMS_BY_RESOURCE["ChargeItem"])
    assert ALL_CLAIM_KEYS == tuple(
        sorted({claim for claims in extracted.values() for claim in claims})
    )
    assert "DiagnosticReport.code-text" in CLAIMS_BY_RESOURCE["DiagnosticReport"]
    assert set(CLAIMS_BY_RESOURCE["Task"]) >= {
        TaskClaim.STATUS,
        TaskClaim.INTENT,
        TaskClaim.IDENTIFIER,
        TaskClaim.GROUP_IDENTIFIER,
    }
    assert CLAIMS_BY_RESOURCE["ResearchSubject"] == (
        ResearchSubjectClaim.IDENTIFIER,
    )


def test_generator_reads_only_exported_claim_objects_and_emits_python_types() -> None:
    common_utils_root = _common_utils_root()
    source_dir = common_utils_root / "src/models/interoperable-claims"
    definitions = extract_claim_definitions(source_dir)
    extracted = extract_claim_catalog(source_dir)

    assert len(definitions) >= 25
    assert sum(len(values) for values in extracted.values()) < 500
    assert "Invoice.identifier.value" not in extracted["Invoice"]
    assert "DocumentReference.content.attachment.url" not in extracted["DocumentReference"]
    assert InvoiceClaim.IDENTIFIER == "Invoice.identifier"
    assert ChargeItemClaim.SUPPORTING_INFORMATION == (
        "ChargeItem.supporting-information"
    )


def test_generator_includes_frozen_objects_and_historical_claim_enums(
    tmp_path: Path,
) -> None:
    (tmp_path / "task-claims.ts").write_text(
        """export const TaskClaim = Object.freeze({
  Status: 'Task.status',
  Intent: 'Task.intent',
} as const);
export enum HistoricalClaim {
  Value = 'Historical.value',
}
""",
        encoding="utf-8",
    )

    definitions = extract_claim_definitions(tmp_path)

    assert definitions["TaskClaim"] == (
        ("Status", "Task.status"),
        ("Intent", "Task.intent"),
    )
    assert definitions["HistoricalClaim"] == (("Value", "Historical.value"),)


def test_invoice_link_does_not_repurpose_charge_item_part_of() -> None:
    assert ChargeItemClaim.PART_OF == "ChargeItem.part-of"
    assert ChargeItemClaim.SUPPORTING_INFORMATION != ChargeItemClaim.PART_OF


def test_charge_item_occurrence_is_generated_from_the_typescript_claim_object() -> None:
    assert ChargeItemClaim.OCCURRENCE == "ChargeItem.occurrence"


def test_every_generated_claim_type_links_its_fhir_search_and_extension_catalogs() -> None:
    common_utils_root = _common_utils_root()
    definitions = extract_claim_definitions(
        common_utils_root / "src/models/interoperable-claims"
    )

    for class_name, properties in definitions.items():
        resource_type = properties[0][1].split(".", 1)[0]
        documentation = getattr(gdc_data_utils, class_name).__doc__ or ""
        assert (
            f"https://hl7.org/fhir/{resource_type.lower()}.html#search"
            in documentation
        )
        assert (
            "https://hl7.org/fhir/extensions/"
            f"extensions-{resource_type}.html"
            in documentation
        )


def test_readme_defines_canonical_and_extension_claim_origins() -> None:
    readme = Path(__file__).parents[1].joinpath("README.md").read_text(
        encoding="utf-8"
    )

    assert "FHIR search parameter" in readme
    assert "FHIR standard extension" in readme
    assert "custom extension" in readme
    assert "GDC-owned extension" not in readme


def test_generated_ips_catalog_matches_the_typescript_contract() -> None:
    profiles, resources = extract_ips_catalog(
        _common_utils_root()
        / "src/models/interoperable-claims/ips-profile-catalog.generated"
    )
    value_sets = extract_ips_value_sets(
        _common_utils_root()
        / "src/models/interoperable-claims/ips-profile-catalog.generated"
    )

    assert IPS_VERSION == "2.0.1"
    assert IPS_FHIR_R4_VERSION == "4.0.1"
    assert IPS_PROFILE_CATALOG == profiles
    assert IPS_RESOURCE_CAPABILITIES == tuple(resources)
    assert IPS_VALUE_SET_CATALOG == value_sets
    assert len(IPS_RESOURCE_CAPABILITIES) == 28


def test_all_ips_resources_fields_types_and_valuesets_are_available_in_python() -> None:
    for resource in IPS_RESOURCE_CAPABILITIES:
        assert resource["profiles"]
        assert resource["searchParameters"]
        assert IPS_CANONICAL_FLAT_CLAIMS_BY_RESOURCE[resource["resourceType"]] == tuple(
            f'{resource["resourceType"]}.{parameter["code"]}'
            for parameter in resource["searchParameters"]
        )
        for profile_url in resource["profiles"]:
            profile = IPS_PROFILE_CATALOG[profile_url]
            assert profile["resourceType"] == resource["resourceType"]
            assert profile["elements"]
            for element in profile["elements"]:
                assert element["id"]
                assert element["path"]
                assert "fhirTypes" in element

    allergy_code = next(
        element
        for element in IPS_PROFILE_CATALOG[
            "http://hl7.org/fhir/uv/ips/StructureDefinition/"
            "AllergyIntolerance-uv-ips|2.0.1"
        ]["elements"]
        if element["path"] == "AllergyIntolerance.code"
    )
    assert allergy_code["fhirTypes"] == ["CodeableConcept"]
    assert allergy_code["binding"]["valueSet"] == (
        "http://hl7.org/fhir/uv/ips/ValueSet/"
        "allergies-intolerances-uv-ips|2.0.1"
    )
    observation = next(
        resource
        for resource in IPS_RESOURCE_CAPABILITIES
        if resource["resourceType"] == "Observation"
    )
    assert len(observation["supportedProfiles"]) == 16
    assert {"Flag.category", "Flag.status"} <= set(
        IPS_CANONICAL_FLAT_CLAIMS_BY_RESOURCE["Flag"]
    )
    assert FlagClaim.DETAIL == "Flag.flag-detail"
    assert FlagClaim.PRIORITY == "Flag.flag-priority"

    composition = IPS_PROFILE_CATALOG[
        "http://hl7.org/fhir/uv/ips/StructureDefinition/"
        "Composition-uv-ips|2.0.1"
    ]
    alerts_code = next(
        element
        for element in composition["elements"]
        if element["id"] == "Composition.section:sectionAlerts.code"
    )
    assert "fixedValue" not in alerts_code
    assert alerts_code["patternValue"] == {
        "fhirType": "CodeableConcept",
        "value": {
            "coding": [{"system": "http://loinc.org", "code": "104605-1"}]
        },
    }


def test_generated_ips_implementation_is_split_by_resource_and_value_set() -> None:
    package_root = Path(__file__).parents[1] / "src/gdc_data_utils"
    facade = package_root / "generated_ips_catalog.py"
    generated = package_root / "generated/ips"

    assert len(facade.read_text(encoding="utf-8").splitlines()) < 20
    assert len(list((generated / "resources").glob("*.py"))) == 29
    assert len(list((generated / "value_sets").glob("*.py"))) > 100
    assert max(
        len(path.read_text(encoding="utf-8").splitlines())
        for path in generated.rglob("*.py")
    ) < 8_000
