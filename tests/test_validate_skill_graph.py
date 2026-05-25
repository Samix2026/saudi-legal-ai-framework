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
