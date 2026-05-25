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


def _count_components(all_nodes: set, graph: dict) -> int:
    """Count weakly connected components (treating edges as undirected)."""
    adjacency: dict = {n: set() for n in all_nodes}
    for src, edges in graph.items():
        for e in edges:
            adjacency.setdefault(src, set()).add(e.target)
            adjacency.setdefault(e.target, set()).add(src)

    visited: set = set()
    components = 0
    for start in all_nodes:
        if start not in visited:
            components += 1
            queue = [start]
            while queue:
                node = queue.pop()
                if node in visited:
                    continue
                visited.add(node)
                queue.extend(adjacency.get(node, set()) - visited)
    return components


def graph_stats(graph: dict) -> dict:
    """
    Compute summary statistics for the skill graph.

    graph: dict mapping "skills/source.md" -> list[Edge]
    Returns a dict with keys: nodes, edges, orphans, most_connected,
    type_counts, components.
    """
    all_nodes: set = set(graph.keys())
    for edges in graph.values():
        for e in edges:
            all_nodes.add(e.target)

    out_degree = {n: len(graph.get(n, [])) for n in all_nodes}
    in_degree: dict = {n: 0 for n in all_nodes}
    for edges in graph.values():
        for e in edges:
            in_degree[e.target] = in_degree.get(e.target, 0) + 1

    total_degree = {n: out_degree.get(n, 0) + in_degree.get(n, 0) for n in all_nodes}
    orphans = sorted(n for n in all_nodes if total_degree[n] == 0)
    most_connected = sorted(all_nodes, key=lambda n: total_degree[n], reverse=True)

    type_counts: dict = {}
    total_edges = 0
    for edges in graph.values():
        for e in edges:
            type_counts[e.relationship] = type_counts.get(e.relationship, 0) + 1
            total_edges += 1

    return {
        "nodes": len(all_nodes),
        "edges": total_edges,
        "orphans": orphans,
        "most_connected": most_connected[:3],
        "type_counts": type_counts,
        "components": _count_components(all_nodes, graph) if all_nodes else 0,
    }


def format_stats(stats: dict) -> str:
    """Format graph statistics for stdout display."""
    type_str = "  ".join(
        f"{t}\xd7{c}"
        for t, c in sorted(stats["type_counts"].items(), key=lambda x: -x[1])
    ) or "(none)"
    most_conn = ", ".join(stats["most_connected"]) if stats["edges"] > 0 else "—"
    orphan_str = ", ".join(stats["orphans"]) if stats["orphans"] else "none"
    return "\n".join([
        "── Skill Graph Summary ───────────────────────────",
        f"  Nodes (skills):        {stats['nodes']}",
        f"  Edges (relationships): {stats['edges']}",
        f"  Orphan skills:         {orphan_str}",
        f"  Most connected:        {most_conn}",
        f"  Relationship types:    {type_str}",
        f"  Connectivity:          {stats['components']} component(s)",
        "─" * 49,
    ])


def run_checks(
    skills_dir: Path = SKILLS_DIR,
    cross_ref_map: Path = CROSS_REF_MAP,
) -> tuple:
    """
    Run all validation checks. Returns (errors, warnings, stats).

    Errors (CI-blocking, exit 1):
      E1: required skills/ directory missing
      E2: referenced skill file does not exist on disk
      E3: invalid relationship type
      E4: malformed entry structure
      E5: self-reference

    Warnings (non-blocking, exit 0):
      W1: skill has no ## Related skills section
      W2: orphan skill (0 in-edges and 0 out-edges across full graph)
      W3: asymmetric relationship (informational)
      W4: cross-reference-map missing Skill Relationship Graph row
    """
    errors: list = []
    warnings: list = []
    no_section_skills: set = set()

    if not skills_dir.exists():
        errors.append(f"ERROR: required directory not found: {skills_dir}")
        return errors, warnings, {}

    map_text = cross_ref_map.read_text(encoding="utf-8") if cross_ref_map.exists() else ""

    graph: dict = {}

    for skill_file in sorted(skills_dir.glob("*.md")):
        skill_path = f"skills/{skill_file.name}"
        has_section, edges, malformed = parse_skill(skill_file)

        # W1: No section
        if not has_section:
            warnings.append(
                f"WARNING: {skill_path} has no '## Related skills' section."
            )
            no_section_skills.add(skill_path)
            graph[skill_path] = []
            continue

        graph[skill_path] = []

        # E4: Malformed entries
        for item in malformed:
            errors.append(
                f"ERROR: {skill_path} 'Related skills': malformed entry: {item!r}"
            )

        for edge in edges:
            # E5: Self-reference
            if edge.target == skill_path:
                errors.append(
                    f"ERROR: {skill_path} has a self-reference in 'Related skills'."
                )
                continue

            # E2: Broken path
            if not (skills_dir.parent / edge.target).exists():
                errors.append(
                    f"ERROR: {skill_path} references {edge.target!r} but file not found."
                )
                continue

            # E3: Invalid relationship type
            if edge.relationship not in ALLOWED_RELATIONSHIP_TYPES:
                errors.append(
                    f"ERROR: {skill_path} uses unknown relationship type "
                    f"{edge.relationship!r} (→ {edge.target})."
                )
                continue

            graph[skill_path].append(edge)

        # W4: Map drift
        row_present = (skill_path in map_text) and ("Skill Relationship Graph" in map_text)
        if not row_present:
            warnings.append(
                f"WARNING: cross-reference-map.md 'Skill Relationship Graph' "
                f"may be missing row for {skill_path}."
            )

    # Compute stats over full graph
    stats = graph_stats(graph)

    # W2: Orphan skills
    for orphan in stats["orphans"]:
        if orphan not in no_section_skills:
            warnings.append(
                f"WARNING: {orphan} appears to be an orphan (0 in-edges and 0 out-edges)."
            )

    # W3: Asymmetric relationships (informational)
    for src, src_edges in graph.items():
        for e in src_edges:
            target_edges = graph.get(e.target, [])
            reverse_exists = any(te.target == src for te in target_edges)
            if not reverse_exists:
                warnings.append(
                    f"WARNING: asymmetric — {src} → {e.target} "
                    f"({e.relationship}) has no reverse edge."
                )

    return errors, warnings, stats


def main() -> None:
    errors, warnings, stats = run_checks()

    if stats:
        print(format_stats(stats))

    for w in warnings:
        print(w)
    for e in errors:
        print(e)

    if not errors and not warnings:
        print("✓ All skill graph checks passed.")
    elif not errors:
        print("✓ No errors. See warnings above.")

    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
