"""
tests/test_validate_dataset.py
Saudi Legal AI Framework — Unit + integration tests for validate_dataset.py
"""

import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

import validate_dataset as vd

REQUIRED_COLUMNS = vd.REQUIRED_COLUMNS


# ── Helpers ────────────────────────────────────────────────────────────────────

def _make_valid_row(**overrides) -> dict:
    row = {
        "id": "1",
        "contract_type": "SaaS Agreement",
        "clause_category": "Jurisdiction & Dispute Resolution",
        "clause_text": "Disputes shall be resolved by SCCA arbitration in Riyadh.",
        "risk_level": "high",
        "risk_reason": "Foreign jurisdiction creates an enforcement barrier.",
        "saudi_legal_note": "Saudi courts may assert jurisdiction regardless of clause.",
        "recommended_revision": "Replace with Riyadh arbitration under SCCA rules.",
        "related_regulation": "Saudi Commercial Courts Law (Royal Decree M/93 1441H)",
        "requires_escalation": "no",
        "language": "en",
        "industry": "Technology",
        "source_type": "hypothetical",
        "reviewed_by_lawyer": "no",
        "notes": "",
    }
    row.update(overrides)
    return row


def _write_csv(path: Path, rows: list, columns: list = None) -> None:
    if columns is None:
        columns = REQUIRED_COLUMNS
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


# ── check_header ───────────────────────────────────────────────────────────────

class TestCheckHeader:
    def test_valid_header_passes(self):
        assert vd.check_header(REQUIRED_COLUMNS) == []

    def test_missing_column_fails(self):
        header = [c for c in REQUIRED_COLUMNS if c != "risk_level"]
        errors = vd.check_header(header)
        assert any("risk_level" in str(e) for e in errors)

    def test_extra_column_fails(self):
        errors = vd.check_header(REQUIRED_COLUMNS + ["extra_col"])
        assert any("extra_col" in str(e) for e in errors)

    def test_wrong_order_fails(self):
        errors = vd.check_header(list(reversed(REQUIRED_COLUMNS)))
        assert len(errors) > 0


# ── check_row ─────────────────────────────────────────────────────────────────

class TestCheckRow:
    def test_valid_row_passes(self):
        assert vd.check_row(_make_valid_row(), row_num=2) == []

    def test_invalid_risk_level_fails(self):
        errors = vd.check_row(_make_valid_row(risk_level="extreme"), row_num=2)
        assert any("risk_level" in str(e) for e in errors)

    def test_invalid_industry_fails(self):
        errors = vd.check_row(_make_valid_row(industry="Aerospace"), row_num=2)
        assert any("industry" in str(e) for e in errors)

    def test_invalid_clause_category_fails(self):
        errors = vd.check_row(_make_valid_row(clause_category="Random Category"), row_num=2)
        assert any("clause_category" in str(e) for e in errors)

    def test_invalid_contract_type_fails(self):
        errors = vd.check_row(_make_valid_row(contract_type="Mystery Agreement"), row_num=2)
        assert any("contract_type" in str(e) for e in errors)

    def test_non_integer_id_fails(self):
        errors = vd.check_row(_make_valid_row(id="abc"), row_num=2)
        assert any("id" in str(e) for e in errors)

    def test_empty_clause_text_fails(self):
        errors = vd.check_row(_make_valid_row(clause_text=""), row_num=2)
        assert any("clause_text" in str(e) for e in errors)

    def test_invalid_requires_escalation_fails(self):
        errors = vd.check_row(_make_valid_row(requires_escalation="maybe"), row_num=2)
        assert any("requires_escalation" in str(e) for e in errors)

    def test_case_mismatch_risk_level_fails(self):
        # Enum is lowercase-only; "High" must fail
        errors = vd.check_row(_make_valid_row(risk_level="High"), row_num=2)
        assert any("risk_level" in str(e) for e in errors)

    def test_invalid_reviewed_by_lawyer_fails(self):
        errors = vd.check_row(_make_valid_row(reviewed_by_lawyer="true"), row_num=2)
        assert any("reviewed_by_lawyer" in str(e) for e in errors)

    def test_invalid_language_fails(self):
        errors = vd.check_row(_make_valid_row(language="fr"), row_num=2)
        assert any("language" in str(e) for e in errors)

    def test_invalid_source_type_fails(self):
        errors = vd.check_row(_make_valid_row(source_type="real"), row_num=2)
        assert any("source_type" in str(e) for e in errors)


# ── validate (integration) ────────────────────────────────────────────────────

class TestValidate:
    def test_valid_csv_passes(self, tmp_path):
        csv_file = tmp_path / "valid.csv"
        _write_csv(csv_file, [_make_valid_row()])
        assert vd.validate(csv_file) is True

    def test_multiple_valid_rows_pass(self, tmp_path):
        csv_file = tmp_path / "multi.csv"
        rows = [
            _make_valid_row(id="1"),
            _make_valid_row(id="2", clause_text="Second clause text here.", risk_level="medium"),
            _make_valid_row(id="3", clause_text="Third clause text here.", risk_level="low"),
        ]
        _write_csv(csv_file, rows)
        assert vd.validate(csv_file) is True

    def test_missing_columns_fails(self, tmp_path):
        csv_file = tmp_path / "bad_header.csv"
        bad_cols = [c for c in REQUIRED_COLUMNS if c not in ("risk_level", "industry")]
        _write_csv(csv_file, [], columns=bad_cols)
        assert vd.validate(csv_file) is False

    def test_duplicate_ids_fail(self, tmp_path):
        csv_file = tmp_path / "dup_ids.csv"
        rows = [
            _make_valid_row(id="1"),
            _make_valid_row(id="1", clause_text="Different text to avoid other errors."),
        ]
        _write_csv(csv_file, rows)
        assert vd.validate(csv_file) is False

    def test_file_not_found_fails(self, tmp_path):
        assert vd.validate(tmp_path / "nonexistent.csv") is False

    def test_invalid_row_in_otherwise_valid_csv_fails(self, tmp_path):
        csv_file = tmp_path / "mixed.csv"
        rows = [
            _make_valid_row(id="1"),
            _make_valid_row(id="2", risk_level="INVALID", clause_text="Second clause."),
        ]
        _write_csv(csv_file, rows)
        assert vd.validate(csv_file) is False
