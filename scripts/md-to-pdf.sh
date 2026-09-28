#!/usr/bin/env bash
# Convert Markdown files to PDF (pandoc + tectonic). Each PDF is written next to its source.
# Usage: md-to-pdf.sh [file.md ...]   (defaults to first-interview/*.md)
set -euo pipefail

files=("$@")
[ ${#files[@]} -eq 0 ] && files=(first-interview/*.md)

for md in "${files[@]}"; do
  pdf="${md%.md}.pdf"
  pandoc "$md" -o "$pdf" \
    --pdf-engine=tectonic \
    -V geometry:margin=2cm \
    -V fontsize=10pt \
    -V colorlinks=true
  echo "✔ $pdf"
done
