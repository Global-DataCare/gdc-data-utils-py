# Claim normalization contract

`gdc-common-utils-ts` owns the canonical claim vocabulary. This Python package
ships a generated parity catalog and boundary tools for Python services.

| Layer | Diagnostic report example |
| --- | --- |
| API-CONFIG | `DiagnosticReport.code-text` |
| `resource.meta.claims` | `DiagnosticReport.code-text` |
| FHIR query | `code:text` |
| DataConv physical index | `diagnosticreport_code-text` |

The physical DataConv mapper lowercases the canonical claim and replaces its
resource separator `.` with `_`. It does not replace the hyphen in the field
name. Physical keys must not leak into API-CONFIG, resources, SDKs, or FHIR
queries.

