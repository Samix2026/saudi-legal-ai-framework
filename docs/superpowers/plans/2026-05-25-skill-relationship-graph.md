# Skill Relationship Graph Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a typed, bidirectional skill relationship graph to the Saudi Legal AI Framework so skills are a navigable legal reasoning network rather than isolated documents.

**Architecture:** Each `skills/*.md` file gets a `## Related skills / مهارات مرتبطة` section using a 3-line-per-edge format (path, typed relationship, rationale). A new validator `scripts/validate_skill_graph.py` parses these sections, validates structure and types, detects self-references and orphans, and emits graph statistics to stdout on every CI run.

**Tech Stack:** Python 3.11, pytest, pathlib, re, dataclasses — no external dependencies. Same pattern as `validate_cross_refs.py` and `validate_example_coverage.py`.

---

## File Map

| Action | Path | Responsibility |
|--------|------|----------------|
| Create | `scripts/validate_skill_graph.py` | Validator: parsing, checks, stats |
| Create | `tests/test_validate_skill_graph.py` | ~31 unit + integration tests |
| Modify | `skills/arbitration.md` | Add `## Related skills` section |
| Modify | `skills/commercial-dispute.md` | Add `## Related skills` section |
| Modify | `skills/compliance-check.md` | Add `## Related skills` section |
| Modify | `skills/contract-review.md` | Add `## Related skills` section |
| Modify | `skills/labor-law-analysis.md` | Add `## Related skills` section |
| Modify | `skills/legal-drafting.md` | Add `## Related skills` section |
| Modify | `skills/real-estate-contracts.md` | Add `## Related skills` section |
| Modify | `docs/cross-reference-map.md` | Add `## Skill Relationship Graph` table |
| Modify | `.github/workflows/validate-datasets.yml` | Add CI step after example coverage |

## Edge Map (14 directed edges, 7 nodes)

The authoritative relationship list. Every `## Related skills` section in Task 3 is derived from this table.

| Source | Target | Type | Rationale |
|--------|--------|------|-----------|
| `contract-review` | `commercial-dispute` | `escalates_to` | Unresolved contract breach or contested clause may require Commercial Court proceedings |
| `contract-review` | `arbitration` | `escalates_to` | An arbitration clause in the contract activates this path instead of court litigation |
| `contract-review` | `legal-drafting` | `precedes` | Review identifies gaps and red flags; legal-drafting addresses them |
| `contract-review` | `compliance-check` | `cross_checks` | Contracts containing PDPL clauses, Nitaqat obligations, or WPS terms need compliance verification |
| `real-estate-contracts` | `contract-review` | `specializes` | Real estate contracts are a domain-scoped application of the general contract review methodology |
| `real-estate-contracts` | `compliance-check` | `depends_on` | Ejar registration, municipal approvals, and REGA requirements are compliance obligations |
| `commercial-dispute` | `arbitration` | `alternative_to` | Arbitration replaces court litigation when a valid arbitration clause exists or parties agree |
| `commercial-dispute` | `legal-drafting` | `precedes` | Formal demand notices must be drafted before court filing |
| `arbitration` | `commercial-dispute` | `alternative_to` | Court litigation is the fallback when arbitration is excluded, waived, or fails |
| `arbitration` | `legal-drafting` | `depends_on` | Arbitration requests, submissions, and award enforcement filings require legal drafting |
| `compliance-check` | `labor-law-analysis` | `cross_checks` | Nitaqat, WPS, and GOSI compliance are labor law sub-domains requiring cross-verification |
| `labor-law-analysis` | `compliance-check` | `cross_checks` | Employment compliance dimensions (PDPL over HR data, Saudization quotas) cross both domains |
| `labor-law-analysis` | `contract-review` | `depends_on` | Employment contracts are analysed using the contract-review methodology for clause-level risk |
| `legal-drafting` | `contract-review` | `depends_on` | Quality criteria for drafted documents are grounded in contract-review red flags and mandatory clause checklists |

**Degree summary (total = in + out):**
- `contract-review`: 7 (4 out, 3 in) — most connected
- `commercial-dispute`: 4 (2 out, 2 in)
- `arbitration`: 4 (2 out, 2 in)
- `compliance-check`: 4 (1 out, 3 in)
- `legal-drafting`: 4 (1 out, 3 in)
- `labor-law-analysis`: 3 (2 out, 1 in)
- `real-estate-contracts`: 2 (2 out, 0 in)

**Note on W3 (asymmetric) warnings:** ~8 of the 14 edges are intentionally one-directional (e.g., `specializes` and `escalates_to` do not require reverse edges). The validator will emit W3 warnings for each of these on clean runs. These are informational and non-blocking. Export flags (JSON/DOT/Mermaid) are deliberately excluded from this PR; follow-up PR after graph is stable.

---

## Task 1: Core parsing functions + unit tests (TDD)

**Files:**
- Create: `scripts/validate_skill_graph.py` (constants, `Edge` dataclass, 8 parsing functions)
- Create: `tests/test_validate_skill_graph.py` (20 unit tests for Task 1 functions)

No `run_checks` or `main` yet — only the pure parsing layer.

- [ ] **Step 1: Write the failing tests**

Create `tests/test_validate_skill_graph.py`:

```python
# tests/test_validate_skill_graph.py
"""Tests for scripts/validate_skill_graph.py — Saudi Legal AI Framework"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

import validate_skill_graph as vsg


# ── Helpers ─────────────────────────────────────────────────────────────────────

def _write_skill_with_edges(path: Path, edges: list) -> None:
    """Write a skill file with a properly-formed Related skills section.

    edges: list of (target_path, relationship_type, rationale) tuples
           e.g. ("skills/foo.md", "escalates_to", "some reason")
    """
    items = []
    for target, rel_type, rationale in edges:
        items.append(
            f"* [{target}](../{target})\n"
            f"  — relationship: {rel_type}\n"
            f"  — {rationale}"
        )
    body = "\n\n".join(items)
    path.write_text(
        "## Introduction\nIntro.\n\n"
        "## Related skills / مهارات مرتبطة\n\n"
        f"{body}\n",
        encoding="utf-8",
    )


def _write_skill_no_section(path: Path) -> None:
    path.write_text(
        "## Introduction\nIntro.\n\n## 11. Relevant Regulations\n",
        encoding="utf-8",
    )


def _write_skill_malformed_item(path: Path) -> None:
    path.write_text(
        "## Related skills / مهارات مرتبطة\n\n"
        "* some description without a link\n",
        encoding="utf-8",
    )


# ── Heading detection ────────────────────────────────────────────────────────────

def test_normalize_heading_strips_hashes():
    assert vsg._normalize_heading("## Related skills") == "related skills"

def test_normalize_heading_arabic():
    assert vsg._normalize_heading("## مهارات مرتبطة") == "مهارات مرتبطة"

def test_normalize_heading_strips_section_number():
    assert vsg._normalize_heading("## 15. Related skills") == "related skills"

def test_is_related_skills_heading_bilingual():
    assert vsg._is_related_skills_heading("## Related skills / مهارات مرتبطة")

def test_is_related_skills_heading_arabic_only():
    assert vsg._is_related_skills_heading("## مهارات مرتبطة")

def test_is_related_skills_heading_case_insensitive():
    assert vsg._is_related_skills_heading("## RELATED SKILLS")

def test_is_related_skills_heading_unrelated():
    assert not vsg._is_related_skills_heading("## Related examples")

def test_is_related_skills_heading_unrelated_arabic():
    assert not vsg._is_related_skills_heading("## الأنظمة ذات الصلة")


# ── Edge extraction ──────────────────────────────────────────────────────────────

VALID_EDGE_SECTION = (
    "* [commercial-dispute.md](../skills/commercial-dispute.md)\n"
    "  — relationship: escalates_to\n"
    "  — a contract dispute may require Commercial Court proceedings\n"
)

def test_extract_skill_edges_single_valid_edge():
    edges = vsg._extract_skill_edges(VALID_EDGE_SECTION)
    assert len(edges) == 1
    assert edges[0].target == "skills/commercial-dispute.md"
    assert edges[0].relationship == "escalates_to"
    assert "contract dispute" in edges[0].rationale

def test_extract_skill_edges_multiple_edges():
    section = (
        "* [commercial-dispute.md](../skills/commercial-dispute.md)\n"
        "  — relationship: escalates_to\n"
        "  — breach may lead to litigation\n"
        "\n"
        "* [arbitration.md](../skills/arbitration.md)\n"
        "  — relationship: escalates_to\n"
        "  — arbitration clause may activate this path\n"
    )
    edges = vsg._extract_skill_edges(section)
    assert len(edges) == 2
    assert edges[0].target == "skills/commercial-dispute.md"
    assert edges[1].target == "skills/arbitration.md"

def test_extract_skill_edges_normalizes_dotdot_prefix():
    section = (
        "* [foo.md](../skills/foo.md)\n"
        "  — relationship: depends_on\n"
        "  — rationale\n"
    )
    edges = vsg._extract_skill_edges(section)
    assert edges[0].target == "skills/foo.md"

def test_extract_skill_edges_no_links_returns_empty():
    assert vsg._extract_skill_edges("no links here\n* plain bullet\n") == []

def test_extract_skill_edges_missing_relationship_line_skips_entry():
    section = (
        "* [foo.md](../skills/foo.md)\n"
        "  just some text without relationship:\n"
        "  — rationale\n"
    )
    assert vsg._extract_skill_edges(section) == []


# ── Malformed entry detection ─────────────────────────────────────────────────────

def test_find_malformed_entries_clean_returns_empty():
    assert vsg._find_malformed_entries(VALID_EDGE_SECTION) == []

def test_find_malformed_entries_no_link():
    section = "* some text without a skills link\n"
    result = vsg._find_malformed_entries(section)
    assert len(result) == 1
    assert "some text" in result[0]

def test_find_malformed_entries_missing_relationship_line():
    section = (
        "* [foo.md](../skills/foo.md)\n"
        "  — just rationale without relationship line\n"
    )
    assert len(vsg._find_malformed_entries(section)) == 1

def test_find_malformed_entries_missing_rationale_line():
    section = (
        "* [foo.md](../skills/foo.md)\n"
        "  — relationship: escalates_to\n"
    )
    assert len(vsg._find_malformed_entries(section)) == 1


# ── parse_skill ──────────────────────────────────────────────────────────────────

def test_parse_skill_with_valid_section(tmp_path):
    f = tmp_path / "myskill.md"
    _write_skill_with_edges(f, [
        ("skills/commercial-dispute.md", "escalates_to", "breach may lead to litigation"),
    ])
    has_section, edges, malformed = vsg.parse_skill(f)
    assert has_section
    assert len(edges) == 1
    assert edges[0].target == "skills/commercial-dispute.md"
    assert malformed == []

def test_parse_skill_no_section(tmp_path):
    f = tmp_path / "myskill.md"
    _write_skill_no_section(f)
    has_section, edges, malformed = vsg.parse_skill(f)
    assert not has_section
    assert edges == []
    assert malformed == []

def test_parse_skill_malformed_entry(tmp_path):
    f = tmp_path / "myskill.md"
    _write_skill_malformed_item(f)
    has_section, edges, malformed = vsg.parse_skill(f)
    assert has_section
    assert edges == []
    assert len(malformed) == 1

def test_parse_skill_arabic_heading(tmp_path):
    f = tmp_path / "myskill.md"
    f.write_text(
        "## مهارات مرتبطة\n\n"
        "* [foo.md](../skills/foo.md)\n"
        "  — relationship: depends_on\n"
        "  — rationale text\n",
        encoding="utf-8",
    )
    has_section, edges, _ = vsg.parse_skill(f)
    assert has_section
    assert len(edges) == 1
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
python3 -m pytest tests/test_validate_skill_graph.py -v 2>&1 | head -20
```

Expected: `ModuleNotFoundError: No module named 'validate_skill_graph'`

- [ ] **Step 3: Write the implementation (core functions only)**

Create `scripts/validate_skill_graph.py`:

```python
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
                        r'^\s*[—\-]\s*relationship:\s*(\S+)',
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
                r'^\s*[—\-]\s*relationship:\s*\S+', lines[j]
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
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
python3 -m pytest tests/test_validate_skill_graph.py -v 2>&1 | tail -10
```

Expected: `20 passed`

- [ ] **Step 5: Commit**

```bash
git add scripts/validate_skill_graph.py tests/test_validate_skill_graph.py
git commit -m "feat: add validate_skill_graph.py core parsing functions and unit tests"
```

---

## Task 2: run_checks, main, graph stats + integration tests

**Files:**
- Modify: `scripts/validate_skill_graph.py` (append `graph_stats`, `_count_components`, `format_stats`, `run_checks`, `main`)
- Modify: `tests/test_validate_skill_graph.py` (append 11 integration tests)

- [ ] **Step 1: Write the failing integration tests**

Append to `tests/test_validate_skill_graph.py`:

```python
# ── graph_stats ──────────────────────────────────────────────────────────────────

def test_graph_stats_basic():
    graph = {
        "skills/a.md": [Edge(target="skills/b.md", relationship="escalates_to", rationale="r")],
        "skills/b.md": [Edge(target="skills/a.md", relationship="alternative_to", rationale="r")],
    }
    stats = vsg.graph_stats(graph)
    assert stats["nodes"] == 2
    assert stats["edges"] == 2
    assert stats["orphans"] == []
    assert stats["components"] == 1

def test_graph_stats_orphan_detected():
    graph = {
        "skills/a.md": [Edge(target="skills/b.md", relationship="escalates_to", rationale="r")],
        "skills/b.md": [],
        "skills/c.md": [],  # c has no in-edges and no out-edges → orphan
    }
    stats = vsg.graph_stats(graph)
    assert "skills/c.md" in stats["orphans"]
    assert "skills/b.md" not in stats["orphans"]  # b has in-edge from a


# ── run_checks integration ────────────────────────────────────────────────────────

def test_run_checks_passes_all_valid(tmp_path):
    skills_dir = tmp_path / "skills"
    skills_dir.mkdir()
    a = skills_dir / "a.md"
    b = skills_dir / "b.md"
    _write_skill_with_edges(a, [("skills/b.md", "escalates_to", "a leads to b")])
    _write_skill_with_edges(b, [("skills/a.md", "alternative_to", "b is alternative to a")])
    cross_ref = tmp_path / "cross-reference-map.md"
    cross_ref.write_text(
        "## Skill Relationship Graph\n\n| `skills/a.md` |\n| `skills/b.md` |\n",
        encoding="utf-8",
    )
    errors, warnings, stats = vsg.run_checks(skills_dir=skills_dir, cross_ref_map=cross_ref)
    assert errors == []
    assert stats["nodes"] == 2
    assert stats["edges"] == 2

def test_run_checks_e1_missing_skills_dir(tmp_path):
    errors, warnings, stats = vsg.run_checks(
        skills_dir=tmp_path / "nonexistent",
        cross_ref_map=tmp_path / "map.md",
    )
    assert any("not found" in e for e in errors)
    assert stats == {}

def test_run_checks_e2_broken_path(tmp_path):
    skills_dir = tmp_path / "skills"
    skills_dir.mkdir()
    skill = skills_dir / "a.md"
    _write_skill_with_edges(skill, [("skills/missing.md", "escalates_to", "does not exist")])
    cross_ref = tmp_path / "map.md"
    cross_ref.write_text("## Skill Relationship Graph\n| `skills/a.md` |\n", encoding="utf-8")
    errors, _, _ = vsg.run_checks(skills_dir=skills_dir, cross_ref_map=cross_ref)
    assert any("not found" in e for e in errors)

def test_run_checks_e3_invalid_type(tmp_path):
    skills_dir = tmp_path / "skills"
    skills_dir.mkdir()
    b = skills_dir / "b.md"
    _write_skill_no_section(b)
    a = skills_dir / "a.md"
    a.write_text(
        "## Related skills / مهارات مرتبطة\n\n"
        "* [b.md](../skills/b.md)\n"
        "  — relationship: invented_type\n"
        "  — some rationale\n",
        encoding="utf-8",
    )
    cross_ref = tmp_path / "map.md"
    cross_ref.write_text("## Skill Relationship Graph\n", encoding="utf-8")
    errors, _, _ = vsg.run_checks(skills_dir=skills_dir, cross_ref_map=cross_ref)
    assert any("unknown relationship type" in e for e in errors)

def test_run_checks_e4_malformed_entry(tmp_path):
    skills_dir = tmp_path / "skills"
    skills_dir.mkdir()
    _write_skill_malformed_item(skills_dir / "a.md")
    cross_ref = tmp_path / "map.md"
    cross_ref.write_text("## Skill Relationship Graph\n| `skills/a.md` |\n", encoding="utf-8")
    errors, _, _ = vsg.run_checks(skills_dir=skills_dir, cross_ref_map=cross_ref)
    assert any("malformed entry" in e for e in errors)

def test_run_checks_e5_self_reference(tmp_path):
    skills_dir = tmp_path / "skills"
    skills_dir.mkdir()
    skill = skills_dir / "a.md"
    _write_skill_with_edges(skill, [("skills/a.md", "depends_on", "itself")])
    cross_ref = tmp_path / "map.md"
    cross_ref.write_text("## Skill Relationship Graph\n| `skills/a.md` |\n", encoding="utf-8")
    errors, _, _ = vsg.run_checks(skills_dir=skills_dir, cross_ref_map=cross_ref)
    assert any("self-reference" in e for e in errors)

def test_run_checks_w1_no_section(tmp_path):
    skills_dir = tmp_path / "skills"
    skills_dir.mkdir()
    _write_skill_no_section(skills_dir / "a.md")
    cross_ref = tmp_path / "map.md"
    cross_ref.write_text("## Skill Relationship Graph\n| `skills/a.md` |\n", encoding="utf-8")
    errors, warnings, _ = vsg.run_checks(skills_dir=skills_dir, cross_ref_map=cross_ref)
    assert errors == []
    assert any("no '## Related skills' section" in w for w in warnings)

def test_run_checks_w2_orphan(tmp_path):
    skills_dir = tmp_path / "skills"
    skills_dir.mkdir()
    a, b, c = skills_dir / "a.md", skills_dir / "b.md", skills_dir / "c.md"
    _write_skill_with_edges(a, [("skills/b.md", "escalates_to", "a leads to b")])
    _write_skill_with_edges(b, [("skills/a.md", "alternative_to", "b to a")])
    # c has a section but no valid entries → orphan
    c.write_text(
        "## Related skills / مهارات مرتبطة\n\n(no entries yet)\n",
        encoding="utf-8",
    )
    cross_ref = tmp_path / "map.md"
    cross_ref.write_text(
        "## Skill Relationship Graph\n"
        "| `skills/a.md` |\n| `skills/b.md` |\n| `skills/c.md` |\n",
        encoding="utf-8",
    )
    errors, warnings, _ = vsg.run_checks(skills_dir=skills_dir, cross_ref_map=cross_ref)
    assert errors == []
    assert any("orphan" in w for w in warnings)

def test_run_checks_w4_map_drift(tmp_path):
    skills_dir = tmp_path / "skills"
    skills_dir.mkdir()
    b = skills_dir / "b.md"
    _write_skill_no_section(b)
    a = skills_dir / "a.md"
    _write_skill_with_edges(a, [("skills/b.md", "escalates_to", "rationale")])
    # cross_ref map exists but has no Skill Relationship Graph section
    cross_ref = tmp_path / "map.md"
    cross_ref.write_text("## Some Other Section\n", encoding="utf-8")
    _, warnings, _ = vsg.run_checks(skills_dir=skills_dir, cross_ref_map=cross_ref)
    assert any("Skill Relationship Graph" in w for w in warnings)
```

Also add this import near the top of the test file, immediately after `import validate_skill_graph as vsg`:

```python
from validate_skill_graph import Edge
```

- [ ] **Step 2: Run tests to verify the new ones fail**

```bash
python3 -m pytest tests/test_validate_skill_graph.py -v 2>&1 | grep -E "PASSED|FAILED|ERROR" | tail -15
```

Expected: 20 PASSED (Task 1), 11 FAILED (Task 2 — `graph_stats` and `run_checks` not yet defined)

- [ ] **Step 3: Append the implementation to `scripts/validate_skill_graph.py`**

Append after the `parse_skill` function:

```python
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
    most_conn = ", ".join(stats["most_connected"]) if stats["most_connected"] else "—"
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
```

- [ ] **Step 4: Run all tests**

```bash
python3 -m pytest tests/test_validate_skill_graph.py -v 2>&1 | tail -15
```

Expected: `31 passed`

- [ ] **Step 5: Smoke-test the validator against the real repo**

```bash
python3 scripts/validate_skill_graph.py
```

Expected: W1 warnings for all 7 skill files (no `## Related skills` yet), stats block showing 7 orphan nodes, exit 0.

- [ ] **Step 6: Commit**

```bash
git add scripts/validate_skill_graph.py tests/test_validate_skill_graph.py
git commit -m "feat: add run_checks, graph_stats, and integration tests for validate_skill_graph"
```

---

## Task 3: Add ## Related skills sections to all 7 skill files

**Files:** Modify all 7 `skills/*.md` files.

The `## Related skills` section is inserted **before** the existing `## Related examples` section in each file. The match pattern for every file is the `---` separator line immediately preceding `## Related examples`.

After this task, running `python3 scripts/validate_skill_graph.py` should produce 0 errors. W3 (asymmetric) warnings are expected and non-blocking.

- [ ] **Step 1: Edit `skills/contract-review.md`**

Find and replace (the `---` immediately before `## Related examples`):

old_string:
```
---

## Related examples / أمثلة مرتبطة
```

new_string:
```
---

## Related skills / مهارات مرتبطة

* [commercial-dispute.md](../skills/commercial-dispute.md)
  — relationship: escalates_to
  — unresolved contract breach or contested clause may require Commercial Court proceedings

* [arbitration.md](../skills/arbitration.md)
  — relationship: escalates_to
  — an arbitration clause in the contract activates this path instead of court litigation

* [legal-drafting.md](../skills/legal-drafting.md)
  — relationship: precedes
  — review identifies gaps and red flags; legal-drafting is then used to address them

* [compliance-check.md](../skills/compliance-check.md)
  — relationship: cross_checks
  — contracts containing PDPL clauses, Nitaqat obligations, or WPS terms need compliance verification

---

## Related examples / أمثلة مرتبطة
```

- [ ] **Step 2: Edit `skills/commercial-dispute.md`**

old_string:
```
---

## Related examples / أمثلة مرتبطة
```

new_string:
```
---

## Related skills / مهارات مرتبطة

* [arbitration.md](../skills/arbitration.md)
  — relationship: alternative_to
  — arbitration replaces court litigation when a valid arbitration clause exists or parties agree

* [legal-drafting.md](../skills/legal-drafting.md)
  — relationship: precedes
  — formal demand notices must be drafted before court filing

---

## Related examples / أمثلة مرتبطة
```

- [ ] **Step 3: Edit `skills/arbitration.md`**

old_string:
```
---

## Related examples / أمثلة مرتبطة
```

new_string:
```
---

## Related skills / مهارات مرتبطة

* [commercial-dispute.md](../skills/commercial-dispute.md)
  — relationship: alternative_to
  — Commercial Court litigation is the fallback when arbitration is excluded, waived, or fails

* [legal-drafting.md](../skills/legal-drafting.md)
  — relationship: depends_on
  — arbitration requests, submissions, and award enforcement filings require legal drafting

---

## Related examples / أمثلة مرتبطة
```

- [ ] **Step 4: Edit `skills/compliance-check.md`**

old_string:
```
---

## Related examples / أمثلة مرتبطة
```

new_string:
```
---

## Related skills / مهارات مرتبطة

* [labor-law-analysis.md](../skills/labor-law-analysis.md)
  — relationship: cross_checks
  — Nitaqat (Saudization), WPS, and GOSI compliance are labor law sub-domains that require cross-verification

---

## Related examples / أمثلة مرتبطة
```

- [ ] **Step 5: Edit `skills/labor-law-analysis.md`**

old_string:
```
---

## Related examples / أمثلة مرتبطة
```

new_string:
```
---

## Related skills / مهارات مرتبطة

* [compliance-check.md](../skills/compliance-check.md)
  — relationship: cross_checks
  — employment compliance dimensions (PDPL over HR data, Saudization quotas) cross both domains

* [contract-review.md](../skills/contract-review.md)
  — relationship: depends_on
  — employment contracts are analysed using the contract-review methodology for clause-level risk

---

## Related examples / أمثلة مرتبطة
```

- [ ] **Step 6: Edit `skills/legal-drafting.md`**

old_string:
```
---

## Related examples / أمثلة مرتبطة
```

new_string:
```
---

## Related skills / مهارات مرتبطة

* [contract-review.md](../skills/contract-review.md)
  — relationship: depends_on
  — quality criteria for drafted documents are grounded in contract-review red flags and mandatory clause checklists

---

## Related examples / أمثلة مرتبطة
```

- [ ] **Step 7: Edit `skills/real-estate-contracts.md`**

old_string:
```
---

## Related examples / أمثلة مرتبطة
```

new_string:
```
---

## Related skills / مهارات مرتبطة

* [contract-review.md](../skills/contract-review.md)
  — relationship: specializes
  — real estate contracts are a domain-scoped application of the general contract review methodology

* [compliance-check.md](../skills/compliance-check.md)
  — relationship: depends_on
  — Ejar registration, municipal approvals, and REGA requirements are compliance obligations

---

## Related examples / أمثلة مرتبطة
```

- [ ] **Step 8: Run the validator to confirm 0 errors**

```bash
python3 scripts/validate_skill_graph.py
```

Expected output (W3 asymmetric warnings are expected on 8 one-directional edges, exit 0):

```
── Skill Graph Summary ─────────────────────────────────────
  Nodes (skills):        7
  Edges (relationships): 14
  Orphan skills:         none
  Most connected:        skills/contract-review.md, skills/legal-drafting.md, skills/arbitration.md
  Relationship types:    escalates_to×4  cross_checks×4  depends_on×4  alternative_to×2  precedes×2  specializes×1
  Connectivity:          1 component(s)
─────────────────────────────────────────────────────────────
WARNING: asymmetric — skills/contract-review.md → skills/commercial-dispute.md (escalates_to) has no reverse edge.
[... ~8 similar W3 lines ...]
✓ No errors. See warnings above.
```

Exit code: 0

- [ ] **Step 9: Run full test suite to confirm no regressions**

```bash
python3 -m pytest tests/ -v 2>&1 | tail -5
```

Expected: all tests pass (count will be prior 118 + 31 new = 149 total)

- [ ] **Step 10: Commit**

```bash
git add skills/arbitration.md skills/commercial-dispute.md skills/compliance-check.md \
        skills/contract-review.md skills/labor-law-analysis.md skills/legal-drafting.md \
        skills/real-estate-contracts.md
git commit -m "docs: add Related skills sections to all 7 skill files (14-edge typed graph)"
```

---

## Task 4: Update docs/cross-reference-map.md

**Files:** Modify `docs/cross-reference-map.md`

Insert the `## Skill Relationship Graph` section between `## Skill → Example Coverage` and `## 4. Sources ← → Regulations`.

- [ ] **Step 1: Edit `docs/cross-reference-map.md`**

Locate the `---` line at line 115 (between `## Skill → Example Coverage` and `## 4. Sources ← → Regulations`) and insert the new section before it.

old_string:
```
**Coverage rules:** 0 examples → Missing | 1 example → Partial | 2+ examples → Strong

---

## 4. Sources ← → Regulations / المصادر ← → الأنظمة
```

new_string:
```
**Coverage rules:** 0 examples → Missing | 1 example → Partial | 2+ examples → Strong

---

## Skill Relationship Graph

> هذا الجدول مُولَّد من `## Related skills` في كل ملف `skills/*.md`.
> يُشغَّل `scripts/validate_skill_graph.py` في كل push للتحقق منه.
> This table is derived from `## Related skills` in each `skills/*.md` file.
> `scripts/validate_skill_graph.py` runs on every push to verify it.

| Skill | Related Skills | Relationship Types | Graph Degree | Connectivity Status |
|---|---|---|---|---|
| `skills/arbitration.md` | `skills/commercial-dispute.md` · `skills/legal-drafting.md` | `alternative_to` · `depends_on` | 4 (2 out, 2 in) | Connected |
| `skills/commercial-dispute.md` | `skills/arbitration.md` · `skills/legal-drafting.md` | `alternative_to` · `precedes` | 4 (2 out, 2 in) | Connected |
| `skills/compliance-check.md` | `skills/labor-law-analysis.md` | `cross_checks` | 4 (1 out, 3 in) | Connected |
| `skills/contract-review.md` | `skills/commercial-dispute.md` · `skills/arbitration.md` · `skills/legal-drafting.md` · `skills/compliance-check.md` | `escalates_to` · `precedes` · `cross_checks` | 7 (4 out, 3 in) | Connected |
| `skills/labor-law-analysis.md` | `skills/compliance-check.md` · `skills/contract-review.md` | `cross_checks` · `depends_on` | 3 (2 out, 1 in) | Connected |
| `skills/legal-drafting.md` | `skills/contract-review.md` | `depends_on` | 4 (1 out, 3 in) | Connected |
| `skills/real-estate-contracts.md` | `skills/contract-review.md` · `skills/compliance-check.md` | `specializes` · `depends_on` | 2 (2 out, 0 in) | Connected |

**Allowed relationship types:** `escalates_to` · `alternative_to` · `cross_checks` · `depends_on` · `specializes` · `precedes` · `shares_sources_with` · `overlaps_with`

---

## 4. Sources ← → Regulations / المصادر ← → الأنظمة
```

- [ ] **Step 2: Run the validator to confirm W4 warnings are now gone**

```bash
python3 scripts/validate_skill_graph.py 2>&1 | grep "W4\|Skill Relationship Graph"
```

Expected: no output (all 7 rows present in map).

- [ ] **Step 3: Run full test suite**

```bash
python3 -m pytest tests/ -v 2>&1 | tail -5
```

Expected: all tests pass.

- [ ] **Step 4: Commit**

```bash
git add docs/cross-reference-map.md
git commit -m "docs: add Skill Relationship Graph section to cross-reference-map.md"
```

---

## Task 5: Wire validator into CI

**Files:** Modify `.github/workflows/validate-datasets.yml`

The new step goes after `Validate example coverage` and before `Validate main dataset`.

- [ ] **Step 1: Edit `.github/workflows/validate-datasets.yml`**

old_string:
```
      - name: Validate example coverage
        run: python3 scripts/validate_example_coverage.py

      - name: Validate main dataset
```

new_string:
```
      - name: Validate example coverage
        run: python3 scripts/validate_example_coverage.py

      - name: Validate skill graph
        run: python3 scripts/validate_skill_graph.py

      - name: Validate main dataset
```

- [ ] **Step 2: Run full test suite one final time**

```bash
python3 -m pytest tests/ -v 2>&1 | tail -5
```

Expected: all tests pass.

- [ ] **Step 3: Run all three validators in sequence (mirrors CI)**

```bash
python3 scripts/validate_cross_refs.py && \
python3 scripts/validate_example_coverage.py && \
python3 scripts/validate_skill_graph.py
```

Expected: all three exit 0. The skill graph validator prints the summary block followed by W3 asymmetric warnings; exit code 0.

- [ ] **Step 4: Commit**

```bash
git add .github/workflows/validate-datasets.yml
git commit -m "ci: add validate_skill_graph.py step after validate_example_coverage.py"
```

---

## Self-Review

**Spec coverage:**
- ✅ `## Related skills / مهارات مرتبطة` section added to every skill (Task 3)
- ✅ 3-line entry format (path, typed relationship, rationale) defined and parsed (Task 1)
- ✅ All 8 relationship types implemented in `ALLOWED_RELATIONSHIP_TYPES` (Task 1)
- ✅ Validator parses sections, validates paths, validates types, detects malformed entries, self-refs, orphans (Task 2)
- ✅ Graph summary stats (nodes, edges, orphans, most connected, type distribution, components) (Task 2)
- ✅ Tests: unit + integration, 31 tests (Tasks 1–2)
- ✅ `## Skill Relationship Graph` table in cross-reference-map.md (Task 4)
- ✅ CI wiring after `validate_example_coverage.py` (Task 5)
- ✅ No export stubs — JSON/DOT/Mermaid deferred to follow-up PR

**Type consistency check:** `Edge.target`, `Edge.relationship`, `Edge.rationale` used consistently across `_extract_skill_edges`, `parse_skill`, `run_checks`, `graph_stats`. `graph` dict type `dict[str, list[Edge]]` consistent throughout.

**Future visualization note:** The `graph_stats` return value is a plain `dict` containing an adjacency list and stats. A follow-up PR can add `--export-json`, `--export-dot`, or `--export-mermaid` flags to `main()` by serializing this dict — no changes to the core validator needed.
