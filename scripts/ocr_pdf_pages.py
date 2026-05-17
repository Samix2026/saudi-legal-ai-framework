"""
scripts/ocr_pdf_pages.py
Saudi Legal AI Framework — Production OCR extractor

يحوّل صفحات محددة من PDF قضائي إلى نص خام قابل للمراجعة البشرية.
Converts specific pages from a judicial PDF to raw OCR text for human review.

الاستخدام / Usage:
    python3 scripts/ocr_pdf_pages.py \\
        --pdf  sources/judicial-decisions/1435/1.pdf \\
        --pages 18-20 \\
        --out  experiments/ocr-production-test/1pdf-pages-18-20/ \\
        --lang ara \\
        --dpi  300

حالة المخرج / Output status:
    جميع المخرجات بحالة ocr_draft — لا تنظيف، لا تعديل.
    يُراجَع النص بشريًا مقابل الصورة الأصلية قبل أي استخدام تحليلي.

    All output carries status ocr_draft — no cleaning, no modification.
    Text must be reviewed by a human against the original image before any analytical use.
"""

import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


# ── Helpers ────────────────────────────────────────────────────────────────────

def parse_pages(pages_str: str) -> list:
    """Parse '18-20' or '18,19,20' or '18-19,22' into a sorted list of ints."""
    pages = []
    for part in pages_str.split(","):
        part = part.strip()
        if "-" in part:
            start, end = part.split("-", 1)
            pages.extend(range(int(start.strip()), int(end.strip()) + 1))
        else:
            pages.append(int(part))
    return sorted(set(pages))


def get_tool_versions() -> dict:
    """Return installed version strings for pdftoppm and tesseract."""
    versions = {}
    for tool, use_stderr in (("pdftoppm", True), ("tesseract", False)):
        try:
            result = subprocess.run(
                [tool, "--version"] if tool == "tesseract" else [tool, "-v"],
                capture_output=True,
                text=True,
            )
            stream = result.stderr if use_stderr else result.stdout
            versions[tool] = (stream or result.stdout).splitlines()[0].strip()
        except Exception as exc:
            versions[tool] = f"error: {exc}"
    return versions


def check_tools():
    for tool in ("pdftoppm", "tesseract"):
        if not shutil.which(tool):
            print(f"ERROR: '{tool}' not found in PATH.", file=sys.stderr)
            sys.exit(1)


# ── Core pipeline ──────────────────────────────────────────────────────────────

def run_pdftoppm(pdf_path: Path, page: int, images_dir: Path, dpi: int) -> Path:
    """
    Convert a single PDF page to PNG.
    Uses before/after glob diff to find the created file, regardless of
    how pdftoppm pads the page number (depends on total PDF page count).
    """
    prefix = str(images_dir / "page")
    before = set(images_dir.glob("page-*.png"))

    cmd = [
        "pdftoppm",
        "-r", str(dpi),
        "-png",
        "-f", str(page),
        "-l", str(page),
        str(pdf_path),
        prefix,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(
            f"pdftoppm failed for page {page}:\n{result.stderr.strip()}"
        )

    after = set(images_dir.glob("page-*.png"))
    new_files = after - before
    if not new_files:
        raise RuntimeError(
            f"pdftoppm produced no output file for page {page}."
        )
    return sorted(new_files)[0]


def run_tesseract(image_path: Path, text_dir: Path, lang: str) -> Path:
    """
    Run tesseract on a PNG image. Returns path of the generated .txt file.
    No post-processing — raw output only.
    """
    out_stem = text_dir / image_path.stem
    cmd = [
        "tesseract",
        str(image_path),
        str(out_stem),
        "-l", lang,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(
            f"tesseract failed for {image_path.name}:\n{result.stderr.strip()}"
        )
    txt_path = out_stem.with_suffix(".txt")
    if not txt_path.exists():
        raise RuntimeError(
            f"tesseract produced no .txt file for {image_path.name}."
        )
    return txt_path


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description=(
            "Extract raw OCR text from specific PDF pages. "
            "All output is ocr_draft — no cleaning applied."
        )
    )
    parser.add_argument("--pdf", required=True, type=Path,
                        help="Path to the source PDF file")
    parser.add_argument("--pages", required=True,
                        help="Pages to process: '18-20' or '18,19,20' or '18-19,22'")
    parser.add_argument("--out", required=True, type=Path,
                        help="Output directory (created if it does not exist)")
    parser.add_argument("--lang", default="ara",
                        help="Tesseract language code (default: ara)")
    parser.add_argument("--dpi", default=300, type=int,
                        help="Rendering resolution for pdftoppm in DPI (default: 300)")
    args = parser.parse_args()

    if not args.pdf.exists():
        print(f"ERROR: PDF not found: {args.pdf}", file=sys.stderr)
        sys.exit(1)

    check_tools()

    pages = parse_pages(args.pages)

    images_dir = args.out / "images"
    text_dir = args.out / "text"
    images_dir.mkdir(parents=True, exist_ok=True)
    text_dir.mkdir(parents=True, exist_ok=True)

    print(f"source_pdf : {args.pdf}")
    print(f"pages      : {pages}")
    print(f"dpi        : {args.dpi}")
    print(f"lang       : {args.lang}")
    print(f"output     : {args.out}")
    print(f"status     : ocr_draft")
    print()

    output_files = []
    for page in pages:
        print(f"  [page {page:>4}]  pdftoppm", end="", flush=True)
        img_path = run_pdftoppm(args.pdf, page, images_dir, args.dpi)
        print(f" → {img_path.name}   tesseract", end="", flush=True)
        txt_path = run_tesseract(img_path, text_dir, args.lang)
        print(f" → {txt_path.name}")
        output_files.append({
            "page": page,
            "image": str(img_path.relative_to(args.out)),
            "text": str(txt_path.relative_to(args.out)),
        })

    metadata = {
        "source_pdf": str(args.pdf),
        "pages": pages,
        "lang": args.lang,
        "dpi": args.dpi,
        "tool_versions": get_tool_versions(),
        "output_status": "ocr_draft",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "output_files": output_files,
    }
    metadata_path = args.out / "metadata.json"
    with open(metadata_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)

    print()
    print(f"  metadata  → {metadata_path}")
    print()
    print("Done. Output is ocr_draft — review against original PDF before any use.")


if __name__ == "__main__":
    main()
