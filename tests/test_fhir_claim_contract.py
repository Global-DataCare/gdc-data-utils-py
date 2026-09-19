# Flow contract: reuse canonical claim catalogs; keep logical claims separate from physical storage keys.

import os
from pathlib import Path

from gdc_data_utils import (
    CLAIMS_BY_RESOURCE,
    ALL_CLAIM_KEYS,
    DiagnosticReportClaim,
    ChargeItemClaim,
    InvoiceClaim,
    ResearchSubjectClaim,
    TaskClaim,
    canonical_claim_for_search_parameter,
    normalize_fhir_api_claims,
    storage_key_for_claim,
)
from gdc_data_utils.catalog_generation import (
    extract_claim_catalog,
    extract_claim_definitions,
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
