#!/bin/bash
set -e

echo "=== DM Mono Nerd Font Builder ==="
echo ""

# Read version from VERSION file
VERSION=$(cat VERSION | tr -d '[:space:]')
echo "Building version: ${VERSION}"
echo ""

# Step 1: Add missing glyphs (Cyrillic, arrows, box drawing, etc.) from BlexMono
echo "Step 1: Adding missing glyphs from BlexMono..."
echo "  Source: BlexMono Nerd Font (IBM Plex Mono derivative)"
echo "  Output: dm-mono-extended/"
fontforge -quiet -lang=py -script add-missing-glyphs.py 2>/dev/null
echo "  Done."
echo ""

# Step 2: Apply Nerd Fonts patcher to extended fonts
echo "Step 2: Applying Nerd Fonts patcher..."
echo ""

INPUT_DIR="dm-mono-extended"
OUTPUT_DIR="dm-mono-nerd-font"

# Clean output directory
rm -rf "$OUTPUT_DIR"
mkdir -p "$OUTPUT_DIR"

for file in "$INPUT_DIR"/DMMonoExtended-*.ttf; do
    base_name=$(basename "$file")
    echo "  Patching: $base_name"
    fontforge -quiet -script ./nerd-fonts/font-patcher -c "$file" -out "$OUTPUT_DIR" 2>/dev/null
done

echo ""
echo "Step 3: Verifying output fonts..."
echo ""

for file in "$OUTPUT_DIR"/DMMonoNerdFont-*.ttf; do
    size=$(du -h "$file" | cut -f1)
    echo "  $(basename "$file")  (${size})"
done

echo ""
echo "=== Complete! ==="
echo "Built DM Mono Nerd Font v${VERSION}"
echo "Output fonts are in: $OUTPUT_DIR/"
echo ""
echo "To install on macOS:"
echo "  cp $OUTPUT_DIR/*.ttf ~/Library/Fonts/"
echo "  fc-cache -f -v"
echo ""
echo "To install on Linux:"
echo "  mkdir -p ~/.local/share/fonts"
echo "  cp $OUTPUT_DIR/*.ttf ~/.local/share/fonts/"
echo "  fc-cache -f -v"
echo ""
echo "To create a release archive:"
echo "  cd $OUTPUT_DIR && tar -czf dm-mono-nerd-font-${VERSION}.tar.gz *.ttf"
