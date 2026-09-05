# AGENTS.md - gdc-data-utils-py

## Purpose

Python counterpart of `gdc-common-utils-ts` for canonical interoperable claim
catalogs and boundary normalization. TypeScript remains the owning source of
claim vocabulary; generated Python catalogs must pass parity tests against it.

## Mandatory TDD

Use red-green-refactor for every behavior change. The first physical line of
each new or modified test module must be:

`# Flow contract: reuse canonical claim catalogs; keep logical claims separate from physical storage keys.`

## Contract

- Flat FHIR-like claims use `<ResourceType>.<field>` and `@context=org.hl7.fhir.api`.
- FHIR search modifiers remain transport syntax, for example `code:text`.
- DataConv physical keys replace only the resource separator `.` with `_`,
  lowercase the result, and preserve field hyphens.
- Never expose a physical key as a canonical claim.

