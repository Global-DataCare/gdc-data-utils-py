#!/usr/bin/env python3
"""Regenerate the Python catalog from gdc-common-utils-ts."""

from __future__ import annotations

import argparse
from pathlib import Path

from gdc_data_utils.catalog_generation import (
    extract_claim_catalog,
    extract_claim_definitions,
    render_python_catalog,
    render_python_types,
    extract_ips_catalog,
    extract_ips_value_sets,
    write_python_ips_package,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("gdc_common_utils_root", type=Path)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("src/gdc_data_utils/generated_catalog.py"),
    )
    parser.add_argument(
        "--ips-output",
        type=Path,
        default=Path("src/gdc_data_utils/generated_ips_catalog.py"),
    )
    parser.add_argument(
        "--types-output",
        type=Path,
        default=Path("src/gdc_data_utils/generated_claims.py"),
    )
    args = parser.parse_args()
    catalog = extract_claim_catalog(
        args.gdc_common_utils_root / "src/models/interoperable-claims"
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render_python_catalog(catalog), encoding="utf-8")
    definitions = extract_claim_definitions(
        args.gdc_common_utils_root / "src/models/interoperable-claims"
    )
    args.types_output.parent.mkdir(parents=True, exist_ok=True)
    args.types_output.write_text(render_python_types(definitions), encoding="utf-8")
    profiles, resources = extract_ips_catalog(
        args.gdc_common_utils_root
        / "src/models/interoperable-claims/ips-profile-catalog.generated"
    )
    value_sets = extract_ips_value_sets(
        args.gdc_common_utils_root
        / "src/models/interoperable-claims/ips-profile-catalog.generated"
    )
    write_python_ips_package(
        args.ips_output.parent / "generated/ips", profiles, resources, value_sets
    )
    args.ips_output.parent.mkdir(parents=True, exist_ok=True)
    args.ips_output.write_text(
        '"""Compatibility facade for the split generated IPS catalog."""\n\n'
        "from .generated.ips.catalog import (\n"
        "    IPS_CANONICAL_FLAT_CLAIMS_BY_RESOURCE,\n"
        "    IPS_FHIR_R4_VERSION,\n"
        "    IPS_FHIR_SEARCH_VERSIONS,\n"
        "    IPS_PROFILE_CATALOG,\n"
        "    IPS_RESOURCE_CAPABILITIES,\n"
        "    IPS_VALUE_SET_CATALOG,\n"
        "    IPS_VERSION,\n"
        ")\n"
        "from .generated.ips.canonical_claim_types import IpsCanonicalFlatClaim\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
