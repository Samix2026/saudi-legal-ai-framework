#!/usr/bin/env python3
"""
validate_skill_graph.py
Saudi Legal AI Framework — typed skill relationship graph validator

Checks that every skills/*.md file has a ## Related skills section with
well-formed, typed edges pointing to existing skills.

Exit codes: 0 = pass (or warnings only), 1 = errors found
"""

import re
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
CROSS_REF_MAP = REPO_ROOT / "docs" / "cross-reference-map.md"

RELATED_SKILLS_HEADING_ALIASES = [
    "related skills",
    "مهارات مرتبطة",
]

ALLOWED_RELATIONSHIP_TYPES = {
    "escalates_to",
    "alternative_to",
    "cross_checks",
    "depends_on",
    "specializes",
    "precedes",
    "shares_sources_with",
    "overlaps_with",
}


@dataclass(frozen=True)
class Edge:
    target: str        # normalized: "skills/foo.md"
    relationship: str  # must be in ALLOWED_RELATIONSHIP_TYPES
    rationale: str     # free text description


def _normalize_heading(line: str) -> str:
    """Strip leading #, section numbers (e.g. 11., §11), and lowercase."""
    text = re.sub(r"^#+\s*", "", line)
    text = re.sub(r"^\d+\.\s*", "", text)
    text = re.sub(r"§\d+\s*", "", text)
    return text.strip().lower()


def _is_related_skills_heading(line: str) -> bool:
    normalized = _normalize_heading(line)
    return any(alias in normalized for alias in RELATED_SKILLS_HEADING_ALIASES)


def _heading_level(line: str) -> int:
    m = re.match(r"^(#+)", line)
    return len(m.group(1)) if m else 0


def _extract_section(lines: list, heading_predicate) -> str:
    """Return the text body of the first section matching heading_predicate."""
    in_section = False
    section_level = 0
    body: list = []
    for line in lines:
        if not in_section:
            if line.startswith("#") and heading_predicate(line):
                in_section = True
                section_level = _heading_level(line)
        else:
            lvl = _heading_level(line)
            if line.startswith("#") and lvl <= section_level:
                break
            body.append(line)
    return "\n".join(body)


def _has_section_heading(lines: list, heading_predicate) -> bool:
    """Return True if any line is a heading matching heading_predicate."""
    return any(
        line.startswith("#") and heading_predicate(line)
        for line in lines
    )


def _extract_skill_edges(section_text: str) -> list:
    """
    Parse 3-line edge blocks from a ## Related skills section body.

    Expected format per edge:
        * [label](../skills/foo.md)
          — relationship: escalates_to
          — rationale text

    Returns only structurally valid blocks. Malformed blocks are reported
    separately by _find_malformed_entries and validated in run_checks.
    """
    lines = [ln.rstrip() for ln in section_text.splitlines()]
    edges = []
    i = 0
    while i < len(lines):
        stripped = lines[i].strip()
        if stripped.startswith(("* ", "- ")):
            m = re.search(
                r'\[([^\]]*)\]\((?:\.\./)?(skills/[\w.-]+\.md)\)',
                stripped,
            )
            if m:
                target = m.group(2)
                # Find next non-blank line: — relationship: <type>
                j = i + 1
                while j < len(lines) and not lines[j].strip():
                    j += 1
                if j < len(lines):
                    rel_m = re.match(
                        r'^\s*[—\-]\s*relationship:\s*([A-Za-z_]+)\s*$',
                        lines[j],
                    )
                    if rel_m:
                        relationship = rel_m.group(1)
                        # Find next non-blank line: — <rationale>
                        k = j + 1
                        while k < len(lines) and not lines[k].strip():
                            k += 1
                        if k < len(lines):
                            rat_m = re.match(
                                r'^\s*[—\-]\s*(.+)',
                                lines[k],
                            )
                            if rat_m:
                                edges.append(
                                    Edge(
                                        target=target,
                                        relationship=relationship,
                                        rationale=rat_m.group(1).strip(),
                                    )
                                )
        i += 1
    return edges


def _find_malformed_entries(section_text: str) -> list:
    """
    Return bullet lines that are structurally malformed:
    - Bullet with no link to skills/
    - Bullet with skills/ link but missing — relationship: line
    - Bullet with skills/ link and relationship: but missing rationale line
    """
    lines = [ln.rstrip() for ln in section_text.splitlines()]
    malformed = []
    i = 0
    while i < len(lines):
        stripped = lines[i].strip()
        if stripped.startswith(("* ", "- ")):
            m = re.search(
                r'\[([^\]]*)\]\((?:\.\./)?(skills/[\w.-]+\.md)\)',
                stripped,
            )
            if not m:
                malformed.append(stripped)
                i += 1
                continue
            # Has skills link — check for relationship: line
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j >= len(lines) or not re.match(
                r'^\s*[—\-]\s*relationship:\s*[A-Za-z_]+\s*$', lines[j]
            ):
                malformed.append(stripped)
                i += 1
                continue
            # Check for rationale line
            k = j + 1
            while k < len(lines) and not lines[k].strip():
                k += 1
            if k >= len(lines) or not re.match(r'^\s*[—\-]\s*.+', lines[k]):
                malformed.append(stripped)
        i += 1
    return malformed


def parse_skill(path: Path) -> tuple:
    """
    Parse a skill file for its Related skills section.

    Returns (has_section, edges, malformed_entries):
    - has_section: True if ## Related skills heading found
    - edges: list of Edge (structurally valid blocks only)
    - malformed_entries: list of malformed bullet line strings
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    has_section = _has_section_heading(lines, _is_related_skills_heading)
    if not has_section:
        return False, [], []
    section_text = _extract_section(lines, _is_related_skills_heading)
    return (
        True,
        _extract_skill_edges(section_text),
        _find_malformed_entries(section_text),
    )
