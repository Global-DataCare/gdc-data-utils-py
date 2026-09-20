"""Generate the Python claim catalog from gdc-common-utils-ts sources."""

from __future__ import annotations

from pathlib import Path
from copy import deepcopy
from hashlib import sha256
import json
from pprint import pformat
import re


_CLAIM_OBJECT = re.compile(
    r"export\s+const\s+(?P<name>[A-Za-z][A-Za-z0-9]*Claim)\s*=\s*"
    r"(?:Object\.freeze\s*\(\s*)?\{(?P<body>.*?)\}\s*as\s+const\s*\)?\s*;",
    re.DOTALL,
)
_CLAIM_ENUM = re.compile(
    r"export\s+enum\s+(?P<name>[A-Za-z][A-Za-z0-9]*Claim(?:sFhirApi)?)\s*"
    r"\{(?P<body>.*?)\}",
    re.DOTALL,
)
_CLAIM_PROPERTY = re.compile(
    r"^\s*(?P<name>[A-Za-z][A-Za-z0-9]*)\s*(?::|=)\s*"
    r"['\"](?P<value>[A-Z][A-Za-z0-9]+\.[A-Za-z0-9.-]+)['\"]\s*,?",
    re.MULTILINE,
)


def _extract_json_assignment(text: str, constant: str, type_name: str):
    start_marker = f"export const {constant} = "
    end_marker = f" as const satisfies {type_name};"
    start = text.find(start_marker)
    if start < 0:
        raise ValueError(f"missing generated TypeScript constant: {constant}")
    start += len(start_marker)
    end = text.find(end_marker, start)
    if end < 0:
        raise ValueError(f"missing generated TypeScript terminator: {constant}")
    return json.loads(text[start:end])


def extract_ips_catalog(path: Path) -> tuple[dict, list[dict]]:
    """Extract the generated IPS profile and resource catalogs from TypeScript."""

    source = Path(path)
    if source.is_file():
        text = source.read_text(encoding="utf-8")
        profiles = _extract_json_assignment(
            text, "IPS_PROFILE_CATALOG", "IpsProfileCatalog"
        )
        resources = _extract_json_assignment(
            text, "IPS_RESOURCE_CAPABILITIES", "readonly IpsResourceCapability[]"
        )
        return profiles, resources

    index = source.joinpath("index.ts").read_text(encoding="utf-8")
    ordered_files = re.findall(
        r"RESOURCE_CAPABILITY as [A-Za-z0-9_$]+Capability \} "
        r"from './resources/([^']+)'",
        index,
    )
    profiles: dict = {}
    resources: list[dict] = []
    for relative in ordered_files:
        text = source.joinpath("resources", f"{relative}.ts").read_text(
            encoding="utf-8"
        )
        profiles.update(
            _extract_json_assignment(text, "RESOURCE_PROFILES", "IpsProfileCatalog")
        )
        resources.append(
            _extract_json_assignment(
                text, "RESOURCE_CAPABILITY", "IpsResourceCapability"
            )
        )
    if not resources:
        raise ValueError(f"no generated IPS resource modules found: {source}")
    return profiles, resources


def _extract_value_set_assignment(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    chunks: list[tuple[str, list]] = []
    for variable, relative in re.findall(
        r"VALUE_SET_CHUNK as ([A-Za-z0-9_$]+) \} from './chunks/([^']+)'",
        text,
    ):
        chunk_text = path.parent.joinpath("chunks", f"{relative}.ts").read_text(
            encoding="utf-8"
        )
        marker = "export const VALUE_SET_CHUNK = "
        start = chunk_text.index(marker) + len(marker)
        end = chunk_text.index(" as const;", start)
        chunks.append((variable, json.loads(chunk_text[start:end])))
    for variable, chunk in sorted(chunks, key=lambda item: len(item[0]), reverse=True):
        text = text.replace(
            f"...{variable}", ", ".join(json.dumps(item) for item in chunk)
        )
    return _extract_json_assignment(text, "VALUE_SET", "IpsValueSetDefinition")


def extract_ips_value_sets(path: Path) -> dict[str, dict]:
    """Extract deduplicated ValueSets from the split TypeScript catalog."""

    directory = Path(path).joinpath("value-sets")
    values = [
        _extract_value_set_assignment(file)
        for file in sorted(directory.glob("*.generated.ts"))
    ]
    return {value["canonicalReference"]: value for value in values}


def _python_module_name(value: str) -> str:
    separated = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)
    result = re.sub(r"[^A-Za-z0-9]+", "_", separated).strip("_").lower()
    return f"_{result}" if result[:1].isdigit() else result


def write_python_ips_package(
    output_root: Path,
    profiles: dict,
    resources: list[dict],
    value_sets: dict[str, dict],
) -> None:
    """Write a split generated Python package by resource and ValueSet."""

    import shutil

    root = Path(output_root)
    shutil.rmtree(root, ignore_errors=True)
    root.parent.mkdir(parents=True, exist_ok=True)
    root.parent.joinpath("__init__.py").write_text(
        '"""Generated package namespace."""\n', encoding="utf-8"
    )
    resource_dir = root / "resources"
    value_set_dir = root / "value_sets"
    chunk_dir = value_set_dir / "chunks"
    for directory in (root, resource_dir, value_set_dir, chunk_dir):
        directory.mkdir(parents=True, exist_ok=True)
        directory.joinpath("__init__.py").write_text(
            '"""Generated module namespace."""\n', encoding="utf-8"
        )

    resource_imports: list[str] = []
    profile_parts: list[str] = []
    capability_parts: list[str] = []
    canonical_claims: dict[str, tuple[str, ...]] = {}
    for resource in resources:
        resource_type = resource["resourceType"]
        module = _python_module_name(resource_type)
        resource_profiles = {
            canonical: profile
            for canonical, profile in profiles.items()
            if profile["resourceType"] == resource_type
            and canonical in resource["profiles"]
        }
        resource_dir.joinpath(f"{module}.py").write_text(
            "\n".join(
                [
                    '"""Generated IPS resource contract; do not edit."""',
                    "",
                    f"PROFILES = {pformat(resource_profiles, sort_dicts=False, width=100)}",
                    "",
                    f"CAPABILITY = {pformat(resource, sort_dicts=False, width=100)}",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        alias = re.sub(r"[^A-Za-z0-9]", "", resource_type)
        resource_imports.append(
            f"from .resources.{module} import CAPABILITY as {alias}_CAPABILITY, PROFILES as {alias}_PROFILES"
        )
        profile_parts.append(f"    **{alias}_PROFILES,")
        capability_parts.append(f"    {alias}_CAPABILITY,")
        canonical_claims[resource_type] = tuple(
            f'{resource_type}.{parameter["code"]}'
            for parameter in resource["searchParameters"]
        )

    value_set_imports: list[str] = []
    value_set_parts: list[str] = []
    for canonical, original in value_sets.items():
        digest = sha256(canonical.encode()).hexdigest()[:10]
        basename = canonical.split("|")[0].rsplit("/", 1)[-1]
        module = f"{_python_module_name(basename)}_{digest}"
        value_set = deepcopy(original)
        imports: list[str] = []
        replacements: list[tuple[str, str]] = []
        chunk_group = 0

        def split_large_array(parent, key: str, label: str) -> None:
            nonlocal chunk_group
            values = parent.get(key) if isinstance(parent, dict) else None
            if not isinstance(values, list) or len(values) <= 100:
                return
            variables: list[str] = []
            for offset in range(0, len(values), 100):
                chunk_index = offset // 100
                variable = f"VALUE_SET_CHUNK_{chunk_group}_{chunk_index}"
                chunk_module = f"{module}_{_python_module_name(label)}_{chunk_index}"
                chunk_dir.joinpath(f"{chunk_module}.py").write_text(
                    '"""Generated ValueSet concept chunk; do not edit."""\n\n'
                    f"VALUE_SET_CHUNK = {pformat(values[offset:offset + 100], sort_dicts=False, width=100)}\n",
                    encoding="utf-8",
                )
                imports.append(
                    f"from .chunks.{chunk_module} import VALUE_SET_CHUNK as {variable}"
                )
                variables.append(variable)
            placeholder = f"__VALUE_SET_CHUNKS_{chunk_group}__"
            parent[key] = placeholder
            replacements.append(
                (repr(placeholder), f"[{', '.join(f'*{name}' for name in variables)}]")
            )
            chunk_group += 1

        split_large_array(value_set.get("expansion", {}), "contains", "expansion")
        for include_index, include in enumerate(
            value_set.get("compose", {}).get("include", [])
        ):
            split_large_array(include, "concept", f"include_{include_index}")
        rendered = pformat(value_set, sort_dicts=False, width=100)
        for placeholder, expression in replacements:
            rendered = rendered.replace(placeholder, expression)
        value_set_dir.joinpath(f"{module}.py").write_text(
            "\n".join(
                [
                    '"""Generated deduplicated IPS ValueSet; do not edit."""',
                    "",
                    *imports,
                    "" if imports else "",
                    f"VALUE_SET = {rendered}",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        alias = f"VALUE_SET_{digest}"
        value_set_imports.append(
            f"from .value_sets.{module} import VALUE_SET as {alias}"
        )
        value_set_parts.append(f"    {alias}['canonicalReference']: {alias},")

    root.joinpath("catalog.py").write_text(
        "\n".join(
            [
                '"""Generated split FHIR IPS catalog; do not edit."""',
                "",
                *resource_imports,
                *value_set_imports,
                "",
                'IPS_VERSION = "2.0.1"',
                'IPS_FHIR_R4_VERSION = "4.0.1"',
                'IPS_FHIR_SEARCH_VERSIONS = ("4.0.1", "5.0.0")',
                "",
                "IPS_PROFILE_CATALOG = {",
                *profile_parts,
                "}",
                "",
                "IPS_RESOURCE_CAPABILITIES = (",
                *capability_parts,
                ")",
                "",
                f"IPS_CANONICAL_FLAT_CLAIMS_BY_RESOURCE = {pformat(canonical_claims, sort_dicts=False, width=100)}",
                "",
                "IPS_VALUE_SET_CATALOG = {",
                *value_set_parts,
                "}",
                "",
            ]
        ),
        encoding="utf-8",
    )
    all_claims = sorted(
        claim for claims in canonical_claims.values() for claim in claims
    )
    root.joinpath("canonical_claim_types.py").write_text(
        "\n".join(
            [
                '"""Generated canonical IPS flat-search claim type; do not edit."""',
                "",
                "from typing import Literal, TypeAlias",
                "",
                "IpsCanonicalFlatClaim: TypeAlias = Literal[",
                *(f"    {claim!r}," for claim in all_claims),
                "]",
                "",
            ]
        ),
        encoding="utf-8",
    )
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
        matches = [
            *((match, True) for match in _CLAIM_OBJECT.finditer(text)),
            *((match, False) for match in _CLAIM_ENUM.finditer(text)),
        ]
        for object_match, required in sorted(matches, key=lambda item: item[0].start()):
            name = object_match.group("name")
            properties = tuple(
                (match.group("name"), match.group("value"))
                for match in _CLAIM_PROPERTY.finditer(object_match.group("body"))
            )
            if not properties:
                if required:
                    raise ValueError(
                        f"exported claim object has no literal claims: {path}:{name}"
                    )
                continue
            if name in definitions:
                raise ValueError(f"duplicate exported claim object: {name}")
            definitions[name] = properties
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
        resource_type = properties[0][1].split(".", 1)[0]
        search_url = f"https://hl7.org/fhir/{resource_type.lower()}.html#search"
        extensions_url = (
            "https://hl7.org/fhir/extensions/"
            f"extensions-{resource_type}.html"
        )
        lines.extend([
            f"class {class_name}:",
            '    """FHIR-like flat claims generated from '
            f'TypeScript ``{class_name}``.',
            "",
            "    Only names published on the resource search page are canonical",
            "    FHIR search parameters. Other names require a FHIR standard or",
            "    custom extension contract.",
            "",
            f"    Search parameters: {search_url}",
            f"    Standard extensions: {extensions_url}",
            '    """',
            "",
        ])
        for property_name, claim in properties:
            lines.append(f"    {_python_constant_name(property_name)} = {claim!r}")
        lines.append("")
    lines.append("__all__ = [")
    lines.extend(f"    {name!r}," for name in definitions)
    lines.extend(["]", ""])
    return "\n".join(lines)
