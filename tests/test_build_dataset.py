"""
tests/test_build_dataset.py
Saudi Legal AI Framework — Unit + integration tests for build_dataset.py
"""

import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

import build_dataset as bd

REQUIRED_COLUMNS = bd.REQUIRED_COLUMNS


# ── Helpers ────────────────────────────────────────────────────────────────────

def _make_valid_row(id: str = "1", clause_text: str = None, **overrides) -> dict:
    row = {
        "id": id,
        "contract_type": "SaaS Agreement",
        "clause_category": "Governing Law",
        "clause_text": clause_text or f"Governing law clause for row {id}.",
        "risk_level": "medium",
        "risk_reason": "US state law may not be upheld by Saudi courts.",
        "saudi_legal_note": "Saudi civil law applies to contracts performed in the Kingdom.",
        "recommended_revision": "Replace with Saudi law as governing law.",
        "related_regulation": "Saudi Civil Transactions Law (Royal Decree M/191 1443H) Art. 22",
        "requires_escalation": "no",
        "language": "en",
        "industry": "Technology",
        "source_type": "hypothetical",
        "reviewed_by_lawyer": "no",
        "notes": "",
    }
    row.update(overrides)
    return row


def _write_csv(path: Path, rows: list) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=REQUIRED_COLUMNS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _read_csv(path: Path) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


# ── check_duplicate_ids ───────────────────────────────────────────────────────

class TestCheckDuplicateIds:
    def test_unique_ids_returns_empty(self):
        rows = [_make_valid_row("1"), _make_valid_row("2"), _make_valid_row("3")]
        assert bd.check_duplicate_ids(rows) == []

    def test_duplicate_id_detected(self):
        rows = [_make_valid_row("1"), _make_valid_row("1")]
        assert "1" in bd.check_duplicate_ids(rows)

    def test_multiple_duplicate_ids_all_detected(self):
        rows = [
            _make_valid_row("1"), _make_valid_row("1"),
            _make_valid_row("2"), _make_valid_row("2"),
        ]
        dups = bd.check_duplicate_ids(rows)
        assert "1" in dups and "2" in dups

    def test_empty_id_not_flagged_as_duplicate(self):
        rows = [_make_valid_row(id=""), _make_valid_row(id="")]
        assert bd.check_duplicate_ids(rows) == []


# ── read_contribution ─────────────────────────────────────────────────────────

class TestReadContribution:
    def test_valid_file_returns_rows(self, tmp_path):
        path = tmp_path / "valid.csv"
        _write_csv(path, [_make_valid_row("1"), _make_valid_row("2")])
        rows, errors = bd.read_contribution(path)
        assert errors == []
        assert len(rows) == 2

    def test_strips_whitespace_from_values(self, tmp_path):
        path = tmp_path / "spaces.csv"
        row = _make_valid_row("1")
        row["risk_level"] = "  medium  "
        _write_csv(path, [row])
        rows, errors = bd.read_contribution(path)
        assert errors == []
        assert rows[0]["risk_level"] == "medium"

    def test_missing_column_returns_error(self, tmp_path):
        path = tmp_path / "bad.csv"
        bad_cols = [c for c in REQUIRED_COLUMNS if c != "risk_level"]
        with open(path, "w", newline="", encoding="utf-8") as f:
            csv.DictWriter(f, fieldnames=bad_cols).writeheader()
        rows, errors = bd.read_contribution(path)
        assert len(errors) > 0
        assert rows == []

    def test_nonexistent_file_returns_error(self, tmp_path):
        rows, errors = bd.read_contribution(tmp_path / "missing.csv")
        assert len(errors) > 0
        assert rows == []

    def test_output_contains_only_required_columns(self, tmp_path):
        path = tmp_path / "valid.csv"
        _write_csv(path, [_make_valid_row("1")])
        rows, _ = bd.read_contribution(path)
        assert set(rows[0].keys()) == set(REQUIRED_COLUMNS)


# ── build (integration) ───────────────────────────────────────────────────────

class TestBuild:
    def test_build_merges_multiple_files(self, tmp_path):
        contrib = tmp_path / "contributions"
        (contrib / "saas").mkdir(parents=True)
        output = tmp_path / "build" / "out.csv"

        _write_csv(contrib / "saas" / "file1.csv", [_make_valid_row("1")])
        _write_csv(contrib / "saas" / "file2.csv", [
            _make_valid_row("1", clause_text="Liability cap clause.")
        ])

        assert bd.build(contrib, output) is True
        assert output.exists()
        assert len(_read_csv(output)) == 2

    def test_build_assigns_sequential_ids(self, tmp_path):
        contrib = tmp_path / "contributions" / "general"
        contrib.mkdir(parents=True)
        output = tmp_path / "build" / "out.csv"

        _write_csv(contrib / "rows.csv", [
            _make_valid_row("99"),
            _make_valid_row("7", clause_text="Second clause here."),
            _make_valid_row("42", clause_text="Third clause here."),
        ])

        bd.build(tmp_path / "contributions", output)
        ids = [r["id"] for r in _read_csv(output)]
        assert ids == ["1", "2", "3"]

    def test_build_prevents_duplicate_ids_within_file(self, tmp_path):
        contrib = tmp_path / "contributions" / "general"
        contrib.mkdir(parents=True)
        output = tmp_path / "build" / "out.csv"

        _write_csv(contrib / "bad.csv", [
            _make_valid_row("1"),
            _make_valid_row("1", clause_text="Same id, different text."),
        ])

        assert bd.build(tmp_path / "contributions", output) is False
        assert not output.exists()

    def test_build_no_csv_files_fails(self, tmp_path):
        contrib = tmp_path / "contributions"
        contrib.mkdir()
        output = tmp_path / "build" / "out.csv"
        assert bd.build(contrib, output) is False

    def test_build_output_has_correct_columns(self, tmp_path):
        contrib = tmp_path / "contributions" / "saas"
        contrib.mkdir(parents=True)
        output = tmp_path / "build" / "out.csv"

        _write_csv(contrib / "file.csv", [_make_valid_row("1")])
        bd.build(tmp_path / "contributions", output)

        rows = _read_csv(output)
        assert list(rows[0].keys()) == REQUIRED_COLUMNS

    def test_build_skips_gitkeep_files(self, tmp_path):
        contrib = tmp_path / "contributions" / "empty"
        contrib.mkdir(parents=True)
        (contrib / ".gitkeep").write_text("")

        saas = tmp_path / "contributions" / "saas"
        saas.mkdir(parents=True)
        _write_csv(saas / "file.csv", [_make_valid_row("1")])

        output = tmp_path / "build" / "out.csv"
        assert bd.build(tmp_path / "contributions", output) is True
        assert len(_read_csv(output)) == 1

    def test_build_output_not_created_on_failure(self, tmp_path):
        contrib = tmp_path / "contributions" / "general"
        contrib.mkdir(parents=True)
        output = tmp_path / "build" / "out.csv"

        _write_csv(contrib / "dup.csv", [
            _make_valid_row("5"),
            _make_valid_row("5", clause_text="Duplicate id."),
        ])

        bd.build(tmp_path / "contributions", output)
        assert not output.exists()
