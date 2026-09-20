"""Typed public facade for the synchronized FHIR IPS 2.0.1 catalog."""

from typing import Any, Literal, NotRequired, TypedDict

from .generated_ips_catalog import (
    IPS_FHIR_R4_VERSION,
    IPS_FHIR_SEARCH_VERSIONS,
    IPS_CANONICAL_FLAT_CLAIMS_BY_RESOURCE,
    IPS_PROFILE_CATALOG,
    IPS_RESOURCE_CAPABILITIES,
    IPS_VALUE_SET_CATALOG,
    IPS_VERSION,
    IpsCanonicalFlatClaim,
)


class IpsElementBinding(TypedDict):
    strength: Literal["required", "extensible", "preferred", "example"]
    valueSet: str
    additionalValueSets: list[str]


class IpsProfileElement(TypedDict):
    id: str
    path: str
    min: int
    max: str
    mustSupport: bool
    fhirTypes: list[str]
    typeProfiles: list[str]
    targetProfiles: list[str]
    contentReference: NotRequired[str]
    fixedValue: NotRequired[dict[str, Any]]
    patternValue: NotRequired[dict[str, Any]]
    binding: NotRequired[IpsElementBinding]
    creatorObligations: list[str]
    consumerObligations: list[str]


class FhirSearchParameterDefinition(TypedDict):
    code: str
    type: Literal[
        "number",
        "date",
        "string",
        "token",
        "reference",
        "composite",
        "quantity",
        "uri",
        "special",
    ]
    url: str
    expression: NotRequired[str]
    fhirVersions: list[str]


class IpsProfileDefinition(TypedDict):
    resourceType: str
    canonicalUrl: str
    version: str
    name: str
    elements: list[IpsProfileElement]


class IpsResourceCapability(TypedDict):
    resourceType: str
    supportedProfiles: list[str]
    profiles: list[str]
    interactions: list[str]
    searchParameters: list[FhirSearchParameterDefinition]


class IpsValueSetUsage(TypedDict):
    resourceType: str
    profile: str
    elementId: str
    path: str
    purpose: Literal["primary", "additional"]
    strength: Literal["required", "extensible", "preferred", "example"]


class IpsValueSetDefinition(TypedDict):
    canonicalReference: str
    canonicalUrl: str
    resolved: bool
    version: NotRequired[str]
    name: NotRequired[str]
    title: NotRequired[str]
    status: NotRequired[str]
    description: NotRequired[str]
    immutable: NotRequired[bool]
    compose: NotRequired[dict[str, Any]]
    expansion: NotRequired[dict[str, Any]]
    usages: list[IpsValueSetUsage]


__all__ = [
    "FhirSearchParameterDefinition",
    "IPS_FHIR_R4_VERSION",
    "IPS_FHIR_SEARCH_VERSIONS",
    "IPS_CANONICAL_FLAT_CLAIMS_BY_RESOURCE",
    "IPS_PROFILE_CATALOG",
    "IPS_RESOURCE_CAPABILITIES",
    "IPS_VALUE_SET_CATALOG",
    "IPS_VERSION",
    "IpsElementBinding",
    "IpsCanonicalFlatClaim",
    "IpsProfileDefinition",
    "IpsProfileElement",
    "IpsResourceCapability",
    "IpsValueSetDefinition",
    "IpsValueSetUsage",
]
