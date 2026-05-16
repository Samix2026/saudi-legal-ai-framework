"""
build_dataset.py
Saudi Legal AI Framework — Dataset Build Script

يقرأ جميع ملفات CSV من datasets/contributions/** ويدمجها في ملف واحد.
Reads all CSVs from datasets/contributions/** and merges them into one file.

الاستخدام / Usage:
    python3 scripts/build_dataset.py
    python3 scripts/build_dataset.py --contributions-dir datasets/contributions
    python3 scripts/build_dataset.py --output datasets/build/custom-output.csv

ملاحظات / Notes:
    - IDs in contribution files are LOCAL — the build script reassigns sequential IDs in output.
    - The master dataset (datasets/saudi-contract-risk-dataset.csv) is NOT modified.
    - Run validate_dataset.py on the generated file after building.
    - datasets/build/ output is not committed to the repo (see .gitignore).
"""

import csv
import sys
import argparse
from pathlib import Path

# Keep in sync with validate_dataset.py
REQUIRED_COLUMNS = [
    "id",
    "contract_type",
    "clause_category",
    "clause_text",
    "risk_level",
    "risk_reason",
    "saudi_legal_note",
    "recommended_revision",
    "related_regulation",
    "requires_escalation",
    "language",
    "industry",
    "source_type",
    "reviewed_by_lawyer",
    "notes",
]

DEFAULT_CONTRIBUTIONS_DIR = Path("datasets/contributions")
DEFAULT_OUTPUT = Path("datasets/build/saudi-contract-risk-dataset.generated.csv")


def print_section(title: str) -> None:
    print(f"\n{'─' * 60}")
    print(f"  {title}")
    print(f"{'─' * 60}")


def find_csv_files(contributions_dir: Path) -> list[Path]:
    return sorted(
        p for p in contributions_dir.rglob("*.csv")
        if not p.name.startswith(".")
    )


def read_contribution(path: Path) -> tuple[list[dict], list[str]]:
    """Read one contribution CSV. Returns (rows, errors)."""
    errors: list[str] = []
    rows: list[dict] = []
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            header = list(reader.fieldnames or [])
            missing = [c for c in REQUIRED_COLUMNS if c not in header]
            if missing:
                errors.append(f"Missing required columns: {missing}")
                return rows, errors
            for row in reader:
                rows.append({col: row.get(col, "").strip() for col in REQUIRED_COLUMNS})
    except FileNotFoundError:
        errors.append(f"File not found: {path}")
    except UnicodeDecodeError:
        errors.append("File is not UTF-8. Save with UTF-8 encoding.")
    except Exception as exc:
        errors.append(str(exc))
    return rows, errors


def check_duplicate_ids(rows: list[dict]) -> list[str]:
    """Return duplicate id values found within a single contribution file."""
    ids: list[str] = [r.get("id", "").strip() for r in rows]
    seen: dict[str, int] = {}
    duplicates: list[str] = []
    for id_val in ids:
        if not id_val:
            continue
        if id_val in seen:
            if id_val not in duplicates:
                duplicates.append(id_val)
        seen[id_val] = 1
    return duplicates


def warn_duplicate_texts(all_rows: list[dict]) -> int:
    """Print warnings for identical clause_text across all merged rows. Returns warning count."""
    text_seen: dict[str, int] = {}
    count = 0
    for i, row in enumerate(all_rows):
        text = row.get("clause_text", "").strip()
        if not text:
            continue
        if text in text_seen:
            count += 1
            print(f"  ⚠️  Duplicate clause_text at merged rows {text_seen[text]} and {i + 1}:")
            print(f"       '{text[:80]}{'...' if len(text) > 80 else ''}'")
        else:
            text_seen[text] = i + 1
    return count


def build(contributions_dir: Path, output_path: Path) -> bool:
    # ── 1. Discovery ─────────────────────────────────────────────────────────────
    print_section("1 / 4  Discovery")
    csv_files = find_csv_files(contributions_dir)

    if not csv_files:
        print(f"  ⚠️  No CSV files found under {contributions_dir}")
        print(f"       Add contribution files to datasets/contributions/<domain>/<name>.csv")
        return False

    for p in csv_files:
        try:
            rel = p.relative_to(Path.cwd())
        except ValueError:
            rel = p
        print(f"  📄 {rel}")
    print(f"\n  Found {len(csv_files)} file(s).")

    # ── 2. Reading ───────────────────────────────────────────────────────────────
    print_section("2 / 4  Reading Contributions")
    all_rows: list[dict] = []
    failed_files: list[Path] = []

    for path in csv_files:
        rows, errors = read_contribution(path)
        if errors:
            failed_files.append(path)
            for e in errors:
                print(f"  ❌ {path.name}: {e}")
            continue

        dup_ids = check_duplicate_ids(rows)
        if dup_ids:
            failed_files.append(path)
            print(f"  ❌ {path.name}: duplicate id values within file: {dup_ids}")
            continue

        if not rows:
            print(f"  ⚠️  {path.name}: no data rows (header only) — skipped.")
            continue

        all_rows.extend(rows)
        print(f"  ✅ {path.name}: {len(rows)} row(s)")

    if failed_files:
        print(f"\n  ❌ Build aborted — {len(failed_files)} file(s) had errors.")
        print(f"     Run validate_dataset.py on each failing file for details.")
        return False

    if not all_rows:
        print("  ⚠️  All contribution files are empty — nothing to build.")
        return False

    # ── 3. Merge & ID Assignment ─────────────────────────────────────────────────
    print_section("3 / 4  Merge & ID Assignment")

    dup_text_count = warn_duplicate_texts(all_rows)
    if dup_text_count == 0:
        print("  ✅ No duplicate clause_text values detected across merged rows.")
    else:
        print(f"  ⚠️  {dup_text_count} duplicate clause_text warning(s) — review before promoting to master.")

    # Reassign IDs sequentially — contribution-file IDs are local only
    for i, row in enumerate(all_rows, start=1):
        row["id"] = str(i)

    print(f"  ✅ Assigned sequential IDs 1–{len(all_rows)} to {len(all_rows)} merged row(s).")

    # ── 4. Writing Output ────────────────────────────────────────────────────────
    print_section("4 / 4  Writing Output")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=REQUIRED_COLUMNS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(all_rows)

    try:
        rel_out = output_path.relative_to(Path.cwd())
    except ValueError:
        rel_out = output_path

    print(f"  ✅ Written: {rel_out}")
    print(f"\n{'─' * 60}")
    print(f"  Build complete")
    print(f"  Source files : {len(csv_files)}")
    print(f"  Total rows   : {len(all_rows)}")
    print(f"  Output       : {rel_out}")
    print(f"\n  Next step — validate the generated file:")
    print(f"    python3 scripts/validate_dataset.py --file {rel_out}")
    print(f"{'─' * 60}\n")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Merge contribution CSVs into a single generated dataset.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python3 scripts/build_dataset.py\n"
            "  python3 scripts/build_dataset.py --contributions-dir datasets/contributions\n"
            "  python3 scripts/build_dataset.py --output datasets/build/custom.csv\n"
        ),
    )
    parser.add_argument(
        "--contributions-dir",
        type=Path,
        default=DEFAULT_CONTRIBUTIONS_DIR,
        metavar="DIR",
        help=f"Root of contribution files (default: {DEFAULT_CONTRIBUTIONS_DIR})",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        metavar="PATH",
        help=f"Output path for generated dataset (default: {DEFAULT_OUTPUT})",
    )
    args = parser.parse_args()
    success = build(args.contributions_dir, args.output)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
