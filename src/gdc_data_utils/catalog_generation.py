"""Generate the Python claim catalog from gdc-common-utils-ts sources."""

from __future__ import annotations

from pathlib import Path
import re


_CLAIM_OBJECT = re.compile(
    r"export\s+const\s+(?P<name>[A-Za-z][A-Za-z0-9]*Claim)\s*=\s*"
    r"\{(?P<body>.*?)\}\s*as\s+const\s*;",
    re.DOTALL,
)
_CLAIM_PROPERTY = re.compile(
    r"^\s*(?P<name>[A-Za-z][A-Za-z0-9]*):\s*"
    r"['\"](?P<value>[A-Z][A-Za-z0-9]+\.[A-Za-z0-9.-]+)['\"]\s*,?",
    re.MULTILINE,
)

# Canonical FHIR ChargeItem fields already consumed by DataConv. They remain
# explicit until the fixes-only TypeScript source line restores the same keys.
_PYTHON_CANONICAL_CLAIM_FIXES: dict[str, tuple[tuple[str, str], ...]] = {
    "ChargeItemClaim": (
        ("SupportingInformation", "ChargeItem.supporting-information"),
        ("Subject", "ChargeItem.subject"),
        ("Occurrence", "ChargeItem.occurrence"),
    ),
}


def extract_claim_definitions(
    source_dir: Path,
) -> dict[str, tuple[tuple[str, str], ...]]:
    """Read only exported ``*Claim = {...} as const`` definitions."""

    source = Path(source_dir)
    if not source.is_dir():
        raise ValueError(f"claim source directory does not exist: {source}")
    definitions: dict[str, tuple[tuple[str, str], ...]] = {}
    for path in sorted(source.glob("*-claims.ts")):
        text = path.read_text(encoding="utf-8")
        for object_match in _CLAIM_OBJECT.finditer(text):
            name = object_match.group("name")
            properties = tuple(
                (match.group("name"), match.group("value"))
                for match in _CLAIM_PROPERTY.finditer(object_match.group("body"))
            )
            if not properties:
                raise ValueError(f"exported claim object has no literal claims: {path}:{name}")
            if name in definitions:
                raise ValueError(f"duplicate exported claim object: {name}")
            definitions[name] = properties
    for name, fixes in _PYTHON_CANONICAL_CLAIM_FIXES.items():
        current = definitions.get(name, ())
        known = {claim for _, claim in current}
        definitions[name] = current + tuple(item for item in fixes if item[1] not in known)
    return dict(sorted(definitions.items()))


def extract_claim_catalog(source_dir: Path) -> dict[str, tuple[str, ...]]:
    """Extract canonical short claims from TypeScript claim model files."""

    claims: dict[str, set[str]] = {}
    for properties in extract_claim_definitions(source_dir).values():
        for _, claim in properties:
            claims.setdefault(claim.split(".", 1)[0], set()).add(claim)
    return {
        resource: tuple(sorted(values))
        for resource, values in sorted(claims.items())
    }


def render_python_catalog(catalog: dict[str, tuple[str, ...]]) -> str:
    """Render a deterministic importable Python catalog."""

    lines = [
        '"""Generated from gdc-common-utils-ts; do not edit by hand."""',
        "",
        "from typing import Literal, TypeAlias",
        "",
        "ClaimKey: TypeAlias = Literal[",
    ]
    all_claims = sorted({claim for claims in catalog.values() for claim in claims})
    lines.extend(f"    {claim!r}," for claim in all_claims)
    lines.extend([
        "]",
        "",
        "ALL_CLAIM_KEYS: tuple[str, ...] = (",
    ])
    lines.extend(f"    {claim!r}," for claim in all_claims)
    lines.extend([
        ")",
        "",
        "CLAIMS_BY_RESOURCE: dict[str, tuple[str, ...]] = {",
    ])
    for resource, claims in catalog.items():
        lines.append(f"    {resource!r}: (")
        lines.extend(f"        {claim!r}," for claim in claims)
        lines.append("    ),")
    lines.extend(["}", ""])
    return "\n".join(lines)


def _python_constant_name(name: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).upper()


def render_python_types(
    definitions: dict[str, tuple[tuple[str, str], ...]],
) -> str:
    """Render one Python constant class for every canonical TypeScript type."""

    lines = [
        '"""Generated from exported gdc-common-utils-ts *Claim objects; do not edit."""',
        "",
    ]
    for class_name, properties in definitions.items():
        lines.extend([
            f"class {class_name}:",
            f'    """Canonical flat claims from TypeScript ``{class_name}``."""',
            "",
        ])
        for property_name, claim in properties:
            lines.append(f"    {_python_constant_name(property_name)} = {claim!r}")
        lines.append("")
    lines.append("__all__ = [")
    lines.extend(f"    {name!r}," for name in definitions)
    lines.extend(["]", ""])
    return "\n".join(lines)
