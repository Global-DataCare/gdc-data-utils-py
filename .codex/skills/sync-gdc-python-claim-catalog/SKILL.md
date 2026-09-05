---
name: sync-gdc-python-claim-catalog
description: Synchronize gdc-data-utils-py with canonical interoperable claims from gdc-common-utils-ts. Use when flat FHIR-like claim names, resource families, search modifiers, storage-key normalization, generated catalogs, or Python consumers such as DataConv change.
---

# Sync GDC Python Claim Catalog

## Source boundary

- Treat `gdc-common-utils-ts` as the current canonical claim owner and
  successor to `_dataspace-client-sdk-node-OLD`.
- Do not use unrelated historical data-utils repositories as sources.
- Reuse an identified Python helper implementation when available, but verify
  its output against the current canonical catalog before adoption.

## Workflow

1. Read both repositories' `AGENTS.md` files.
2. Add a failing Python parity or normalization test.
3. Regenerate the catalog:

   ```bash
   PYTHONPATH=src python scripts/generate_claim_catalog.py ../gdc-common-utils-ts
   ```

4. Inspect the generated diff and reject invented or missing claim keys. The
   extractor must read only exported `*Claim = {...} as const` objects; reject
   FHIR projection paths such as `Invoice.identifier.value`.
5. Run the Python package tests and affected DataConv integration tests.
6. Keep README, normalization docs, consumer docs, and changelogs aligned.

## Required example

```text
flat claim:    DiagnosticReport.code-text
FHIR search:   code:text
physical key:  diagnosticreport_code-text
```

Preserve the field hyphen. Reject `diagnosticreport_code_text`. Physical keys
must remain internal to database/search adapters.

For financial resources, require both relationship directions:

```text
Invoice.lineItem.chargeItemReference -> ChargeItem
ChargeItem.supporting-information    -> Invoice
ChargeItem.occurrence                -> ChargeItem.occurrence[x]
```

Never use `ChargeItem.part-of` for an Invoice; FHIR reserves it for a parent
ChargeItem. Do not report a gateway financial E2E as complete until Invoice and
ChargeItem have real collection, indexing, search and live boundary proof.
Do not claim multi-resource twin search is implemented while the gateway
rejects more than one resource-scoped claim family per request.
