#!/usr/bin/env bash
# Download the 1435H judicial decision PDFs from the GitHub Release into
# sources/judicial-decisions/1435/ and verify their checksums.
# تحميل ملفات أحكام 1435هـ من إصدار GitHub والتحقق من سلامتها.
set -euo pipefail
REPO="Samix2026/saudi-legal-ai-framework"
TAG="judicial-decisions-1435"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$ROOT/sources/judicial-decisions/1435"
mkdir -p "$DEST"
for n in $(seq 1 14); do
  f="$DEST/$n.pdf"
  [ -s "$f" ] && continue
  echo "Downloading $n.pdf"
  curl -fL --retry 3 -o "$f" "https://github.com/$REPO/releases/download/$TAG/$n.pdf"
done
cd "$DEST"
if command -v sha256sum >/dev/null; then sha256sum -c ../1435.SHA256SUMS
else shasum -a 256 -c ../1435.SHA256SUMS; fi
