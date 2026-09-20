"""Compatibility facade for the split generated IPS catalog."""

from .generated.ips.catalog import (
    IPS_CANONICAL_FLAT_CLAIMS_BY_RESOURCE,
    IPS_FHIR_R4_VERSION,
    IPS_FHIR_SEARCH_VERSIONS,
    IPS_PROFILE_CATALOG,
    IPS_RESOURCE_CAPABILITIES,
    IPS_VALUE_SET_CATALOG,
    IPS_VERSION,
)
from .generated.ips.canonical_claim_types import IpsCanonicalFlatClaim
