# gdc-data-utils-py

Python claim catalogs and normalization utilities aligned with
`gdc-common-utils-ts`, the current canonical successor to the historical
`_dataspace-client-sdk-node-OLD` claim definitions.

The generated catalog and Python constant classes cover exported short-claim
`*Claim = {...} as const` objects, frozen claim objects, and historical claim
enums from `gdc-common-utils-ts`. FHIR projection paths, examples and expanded
contextual enums are deliberately excluded. Regenerate after a canonical
TypeScript claim change:

```bash
PYTHONPATH=src python scripts/generate_claim_catalog.py ../gdc-common-utils-ts
python -m pytest -q
```

## Claim origin

The `<ResourceType>.<name>` format does not make every key canonical FHIR.
Each flat claim has one of three origins:

1. **FHIR search parameter** — canonical only when `<name>` is published in
   that resource's official `#search` section.
2. **FHIR standard extension** — an HL7-published extension for the resource,
   retaining its canonical extension URL in native FHIR projections.
3. **custom extension** — a non-standard key with an explicitly documented
   canonical extension URL and projection contract.

A native FHIR element that is absent from `#search` is not automatically a
canonical flat-search claim. Each generated Python claim class links to both
official references for its resource:

```text
https://hl7.org/fhir/<resourcetype-lowercase>.html#search
https://hl7.org/fhir/extensions/extensions-<ResourceType>.html
```

For example:

- [ChargeItem search parameters](https://hl7.org/fhir/chargeitem.html#search)
- [ChargeItem standard extensions](https://hl7.org/fhir/extensions/extensions-ChargeItem.html)

## FHIR IPS 2.0.1 types

The package also exports the complete catalog synchronized from
`gdc-common-utils-ts` for all 28 resource types in the
[IPS Server CapabilityStatement](https://hl7.org/fhir/uv/ips/2.0.1/en/CapabilityStatement-ips-server.html),
not only `Observation`. `IPS_PROFILE_CATALOG` retains every constrained,
required or obligated profile field's FHIR types, cardinality, `Must Support`, Creator/Consumer obligations and
primary/additional ValueSet bindings. `IPS_RESOURCE_CAPABILITIES` includes all
advertised profiles, including the nine R4 vital-sign profiles.

`IPS_CANONICAL_FLAT_CLAIMS_BY_RESOURCE` and `IpsCanonicalFlatClaim` cover the
canonical FHIR search parameters for every IPS resource. Fields that are not
FHIR search parameters remain FHIR standard extensions or custom extensions.

Generated implementation is intentionally split instead of being a single
large module:

```text
src/gdc_data_utils/generated/ips/
├── resources/       # one module per FHIR resource type
├── value_sets/      # one deduplicated module per canonical ValueSet
│   └── chunks/      # bounded chunks for unusually large concept lists
├── catalog.py       # small aggregation index
└── canonical_claim_types.py
```

`src/gdc_data_utils/generated_ips_catalog.py` is only a small compatibility
facade. The repository name `gdc-data-utils-py` and import package path
`src/gdc_data_utils` are separate layers of the standard Python `src` layout.

```python
from gdc_data_utils import (
    IPS_PROFILE_CATALOG,
    IPS_CANONICAL_FLAT_CLAIMS_BY_RESOURCE,
)

allergy = IPS_PROFILE_CATALOG[
    "http://hl7.org/fhir/uv/ips/StructureDefinition/"
    "AllergyIntolerance-uv-ips|2.0.1"
]
assert "AllergyIntolerance.code" in (
    IPS_CANONICAL_FLAT_CLAIMS_BY_RESOURCE["AllergyIntolerance"]
)
```

## Flat claim, database key, and FHIR search

These are three representations of one concept and must remain separate:

```text
API-CONFIG
DiagnosticReport.code-text
          ↓
resource.meta.claims
{
  "@context": "org.hl7.fhir.api",
  "DiagnosticReport.code-text": "diagnóstico en español"
}
          ↓ indexación interna
diagnosticreport_code-text
          ↓ consulta FHIR
DiagnosticReport?code:text=diagnóstico
```

```python
from gdc_data_utils import DiagnosticReportClaim, storage_key_for_claim

assert DiagnosticReportClaim.CODE_TEXT == "DiagnosticReport.code-text"
assert storage_key_for_claim(DiagnosticReportClaim.CODE_TEXT) == (
    "diagnosticreport_code-text"
)
```

`code-display` is for the display associated with a terminology code.
Uncoded local-language diagnostic text uses `code-text`.

## Invoice and ChargeItem

`Invoice` and `ChargeItem` are separate resources. An invoice owns
`Invoice.lineItem[].chargeItemReference`; every imported ChargeItem links back
to its supporting invoice through the native FHIR element and flat claim:

```text
Invoice.lineItem.chargeItemReference -> urn:uuid:<charge-item-resource-id>
ChargeItem.supportingInformation    -> urn:uuid:<invoice-resource-id>
ChargeItem.supporting-information   -> urn:uuid:<invoice-resource-id>
```

`ChargeItem.part-of` is reserved for a parent `ChargeItem`. It must never be
used as an Invoice reference. Product or service codes and quantities remain
separate canonical claims, for example `ChargeItem.code`,
`ChargeItem.occurrence`, `ChargeItem.quantity-number`, and
`ChargeItem.quantity-unit`.

## GW CORE integration status

DataConv can materialize and search its local `Invoice` and `ChargeItem`
resources, but the GW CORE boundary is not complete yet:

- `ChargeItem` is absent from the GW CORE resource-type, collection and
  index-profile registries;
- `Invoice` is emitted by an order response flow but is not a normalized
  financial search collection;
- the current invoice Bundle does not persist separate ChargeItem resources or
  `Invoice.lineItem.chargeItemReference` entries;
- any legacy invoice association stored in `ChargeItem.part-of` must migrate to
  `ChargeItem.supporting-information` plus native `supportingInformation`;
- the DataConv-to-GW financial live E2E remains blocked until those persistence,
  indexing and search contracts are implemented in GW CORE.
- the public GW CORE `ResearchSubject/_search` accepts a FHIR `Parameters`
  array but currently rejects filters spanning more than one resource family;
  an AND query combining `ChargeItem` and `DiagnosticReport` therefore remains
  a gateway implementation and E2E gap, even though Communication and
  Bundle-search building blocks exist.

These are documented compatibility gaps, not behavior supplied by this Python
package.
