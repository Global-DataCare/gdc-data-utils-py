# gdc-data-utils-py

Python claim catalogs and normalization utilities aligned with
`gdc-common-utils-ts`, the current canonical successor to the historical
`_dataspace-client-sdk-node-OLD` claim definitions.

The generated catalog and Python constant classes cover only exported
`*Claim = {...} as const` objects from `gdc-common-utils-ts`. FHIR projection
paths, examples and contextual enums are deliberately excluded. Regenerate
after a canonical TypeScript claim change:

```bash
PYTHONPATH=src python scripts/generate_claim_catalog.py ../gdc-common-utils-ts
python -m pytest -q
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
