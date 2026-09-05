"""Boundary mappings between flat claims, FHIR search, and physical indexes."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any


FHIR_API_CONTEXT = "org.hl7.fhir.api"


def canonical_claim_for_search_parameter(resource_type: str, parameter: str) -> str:
    """Map FHIR query syntax to the corresponding flat FHIR-like claim key."""

    resource = str(resource_type or "").strip()
    search_parameter = str(parameter or "").strip().lower()
    if not resource or not search_parameter:
        raise ValueError("resource_type and parameter are required")
    field = search_parameter.replace(":", "-")
    return f"{resource}.{field}"


def storage_key_for_claim(claim_key: str) -> str:
    """Return the DataConv physical key without changing field-name hyphens."""

    logical_key = str(claim_key or "").strip()
    resource, separator, field = logical_key.partition(".")
    if not separator or not resource or not field:
        raise ValueError("claim_key must use <ResourceType>.<field>")
    return f"{resource.lower()}_{field.lower().replace('.', '_')}"


def normalize_fhir_api_claims(claims: Mapping[str, Any]) -> dict[str, Any]:
    """Collapse expanded FHIR API claims to contextual flat claim keys."""

    context = str(claims.get("@context", FHIR_API_CONTEXT) or "").strip().rstrip(".")
    if context != FHIR_API_CONTEXT:
        raise ValueError(f"unsupported FHIR claims context: {context}")
    prefix = f"{FHIR_API_CONTEXT}."
    normalized: dict[str, Any] = {"@context": FHIR_API_CONTEXT}
    for raw_key, value in claims.items():
        key = str(raw_key or "").strip()
        if not key or key == "@context":
            continue
        normalized[key[len(prefix):] if key.startswith(prefix) else key] = value
    return normalized

