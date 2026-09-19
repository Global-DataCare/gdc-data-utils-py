# Changelog

## Unreleased

- Synchronize frozen TypeScript `*Claim` objects and historical short-claim
  enums instead of silently omitting them from the Python catalog.
- Add the canonical `TaskClaim` and `ResearchSubjectClaim` classes, including
  the standard FHIR R5 Task workflow and asynchronous-job correlation fields.

- Added a generated Python catalog for the canonical flat FHIR-like claims
  defined by `gdc-common-utils-ts`.
- Added explicit mappings between `DiagnosticReport.code-text`, FHIR
  `code:text`, and the physical DataConv key `diagnosticreport_code-text`.
- Restricted generation to exported TypeScript `*Claim` objects, excluding
  FHIR projection paths and other lookalike literals, and generated one Python
  constant class per canonical claim object.
- Added `ChargeItem.supporting-information`, `ChargeItem.subject` and
  `ChargeItem.occurrence`; invoice links no longer repurpose
  `ChargeItem.part-of`.
- Documented the incomplete GW CORE financial persistence, indexing, search and
  DataConv-to-GW E2E boundary.
- Kept the canonical FHIR ChargeItem subject, occurrence and supporting
  information claims available to DataConv while the fixes-only TypeScript
  source line restores those accidentally omitted keys.
