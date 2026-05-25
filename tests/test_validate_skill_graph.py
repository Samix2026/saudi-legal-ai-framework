# tests/test_validate_skill_graph.py
"""Tests for scripts/validate_skill_graph.py — Saudi Legal AI Framework"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

import validate_skill_graph as vsg
from validate_skill_graph import Edge


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


def test_extract_skill_edges_invalid_relationship_token_rejected():
    # A token with trailing punctuation is not a valid relationship type
    section = (
        "* [foo.md](../skills/foo.md)\n"
        "  — relationship: escalates_to.\n"
        "  — some rationale\n"
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


def test_run_checks_w3_asymmetric(tmp_path):
    skills_dir = tmp_path / "skills"
    skills_dir.mkdir()
    a = skills_dir / "a.md"
    b = skills_dir / "b.md"
    # a → b (escalates_to), no reverse edge from b → a
    _write_skill_with_edges(a, [("skills/b.md", "escalates_to", "a leads to b")])
    _write_skill_with_edges(b, [])  # b has section but no out-edges
    cross_ref = tmp_path / "map.md"
    cross_ref.write_text(
        "## Skill Relationship Graph\n| `skills/a.md` |\n| `skills/b.md` |\n",
        encoding="utf-8",
    )
    errors, warnings, _ = vsg.run_checks(skills_dir=skills_dir, cross_ref_map=cross_ref)
    assert errors == []
    assert any("asymmetric" in w for w in warnings)
