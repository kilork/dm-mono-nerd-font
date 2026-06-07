#!/usr/bin/env python3
"""
Add missing glyphs to DM Mono by copying from BlexMono Nerd Font.

BlexMono (based on IBM Plex Mono) has excellent coverage of glyphs that DM Mono
lacks: Cyrillic, arrows, box drawing, block elements, and other common symbols.
Both fonts share the same em=1000 and monospace width=600 metrics.

Glyphs added:
  - Cyrillic (U+0400-U+04FF, U+0500-U+052F) — 194 glyphs
  - Arrows (U+2190-U+21FF) — 22 glyphs
  - Box Drawing (U+2500-U+257F) — 128 glyphs
  - Block Elements (U+2580-U+259F) — 32 glyphs

Usage:
    fontforge -lang=py -script add-missing-glyphs.py

Note: This script is designed to run within FontForge's Python environment.
"""

import fontforge
import psMat
import os
import sys

# Source directories
DM_MONO_DIR = "dm-mono/exports"
# Path to BlexMono Nerd Font files.
# BlexMono (IBM Plex Mono derivative) is used as the source for missing glyphs.
# The default path points to the nerd-fonts submodule (git submodule update --init).
# Override via environment variable BLEX_MONO_DIR if using a different source.
BLEX_DIR = os.environ.get("BLEX_MONO_DIR", os.path.join("nerd-fonts", "patched-fonts", "IBMPlexMono", "Mono"))
OUTPUT_DIR = "dm-mono-extended"

# Weight/style mapping between DM Mono and BlexMono
FONT_VARIANTS = [
    ("DMMono-Regular.ttf",      "BlexMonoNerdFont-Regular.ttf",      "Regular"),
    ("DMMono-Italic.ttf",       "BlexMonoNerdFont-Italic.ttf",       "Italic"),
    ("DMMono-Light.ttf",        "BlexMonoNerdFont-Light.ttf",        "Light"),
    ("DMMono-LightItalic.ttf",  "BlexMonoNerdFont-LightItalic.ttf",  "LightItalic"),
    ("DMMono-Medium.ttf",       "BlexMonoNerdFont-Medium.ttf",       "Medium"),
    ("DMMono-MediumItalic.ttf", "BlexMonoNerdFont-MediumItalic.ttf", "MediumItalic"),
]

# Glyph ranges to copy, with their alignment strategy
# Each entry: (start, end, name, alignment_mode)
# alignment_mode: 'letter' = scale & baseline align, 'center' = center in cell, 'preserve' = keep original pos
GLYPH_RANGES = [
    # Cyrillic
    (0x0400, 0x04FF, "Cyrillic", "letter"),
    (0x0500, 0x052F, "Cyrillic Supplement", "letter"),
    # Arrows (centered symbols)
    (0x2190, 0x21FF, "Arrows", "center"),
    # Box Drawing (preserve exact positioning for connections)
    (0x2500, 0x257F, "Box Drawing", "preserve"),
    # Block Elements (preserve for progress bars etc.)
    (0x2580, 0x259F, "Block Elements", "preserve"),
]


def is_capital_cyrillic(cp):
    """Check if codepoint is a Cyrillic capital letter."""
    if 0x0410 <= cp <= 0x042F:
        return True
    if cp in (0x0400, 0x0401, 0x0402, 0x0403, 0x0404, 0x0405,
              0x0406, 0x0407, 0x0408, 0x0409, 0x040A, 0x040B,
              0x040C, 0x040D, 0x040E, 0x040F):
        return True
    if 0x0460 <= cp <= 0x0481 and cp % 2 == 0:
        return True
    if cp in (0x048A, 0x048C, 0x048E, 0x0490, 0x0492, 0x0494, 0x0496, 0x0498,
              0x049A, 0x049C, 0x049E, 0x04A0, 0x04A2, 0x04A4, 0x04A6, 0x04A8,
              0x04AA, 0x04AC, 0x04AE, 0x04B0, 0x04B2, 0x04B4, 0x04B6, 0x04B8,
              0x04BA, 0x04BC, 0x04BE, 0x04C0, 0x04C1, 0x04C3, 0x04C5, 0x04C7,
              0x04C9, 0x04CB, 0x04CD, 0x04D0, 0x04D2, 0x04D4, 0x04D6, 0x04D8,
              0x04DA, 0x04DC, 0x04DE, 0x04E0, 0x04E2, 0x04E4, 0x04E6, 0x04E8,
              0x04EA, 0x04EC, 0x04EE, 0x04F0, 0x04F2, 0x04F4, 0x04F6, 0x04F8,
              0x04FA, 0x04FC, 0x04FE):
        return True
    if 0x0500 <= cp <= 0x052F and cp % 2 == 0:
        return True
    return False


def is_lowercase_cyrillic(cp):
    """Check if codepoint is a Cyrillic lowercase letter."""
    if 0x0430 <= cp <= 0x044F:
        return True
    if cp in (0x0450, 0x0451, 0x0452, 0x0453, 0x0454, 0x0455,
              0x0456, 0x0457, 0x0458, 0x0459, 0x045A, 0x045B,
              0x045C, 0x045D, 0x045E, 0x045F):
        return True
    if 0x0461 <= cp <= 0x0481 and cp % 2 == 1:
        return True
    if cp in (0x048B, 0x048D, 0x048F, 0x0491, 0x0493, 0x0495, 0x0497, 0x0499,
              0x049B, 0x049D, 0x049F, 0x04A1, 0x04A3, 0x04A5, 0x04A7, 0x04A9,
              0x04AB, 0x04AD, 0x04AF, 0x04B1, 0x04B3, 0x04B5, 0x04B7, 0x04B9,
              0x04BB, 0x04BD, 0x04BF, 0x04C2, 0x04C4, 0x04C6, 0x04C8, 0x04CA,
              0x04CC, 0x04CE, 0x04CF, 0x04D1, 0x04D3, 0x04D5, 0x04D7, 0x04D9,
              0x04DB, 0x04DD, 0x04DF, 0x04E1, 0x04E3, 0x04E5, 0x04E7, 0x04E9,
              0x04EB, 0x04ED, 0x04EF, 0x04F1, 0x04F3, 0x04F5, 0x04F7, 0x04F9,
              0x04FB, 0x04FD, 0x04FF):
        return True
    if 0x0501 <= cp <= 0x052F and cp % 2 == 1:
        return True
    return False


def has_content(font, cp):
    """Check if a glyph at codepoint has actual visible content."""
    try:
        glyph = font[cp]
        if not glyph or not glyph.isWorthOutputting():
            return False
        bb = glyph.boundingBox()
        return bb[2] > bb[0] or bb[3] > bb[1]
    except:
        return False


def copy_missing_glyphs(dm_font, blex_font):
    """
    Copy missing glyphs from BlexMono into DM Mono.
    Handles different glyph types with appropriate alignment strategies.
    """
    # Get reference Latin character metrics from DM Mono
    ref_cap = ord('A')
    ref_lc = ord('a')

    dm_ref_cap = dm_font[ref_cap]
    dm_cap_bb = dm_ref_cap.boundingBox()
    dm_cap_top = dm_cap_bb[3]
    dm_cap_bottom = dm_cap_bb[1]
    dm_mono_width = dm_ref_cap.width

    dm_ref_lc = dm_font[ref_lc]
    dm_lc_bb = dm_ref_lc.boundingBox()
    dm_lc_top = dm_lc_bb[3]
    dm_lc_bottom = dm_lc_bb[1]

    # Reference metrics from BlexMono
    blex_ref_cap = blex_font[ref_cap]
    blex_cap_bb = blex_ref_cap.boundingBox()
    blex_cap_top = blex_cap_bb[3]
    blex_cap_bottom = blex_cap_bb[1]

    blex_ref_lc = blex_font[ref_lc]
    blex_lc_bb = blex_ref_lc.boundingBox()
    blex_lc_top = blex_lc_bb[3]
    blex_lc_bottom = blex_lc_bb[1]

    # Calculate scale factors for letters
    cap_scale_y = (dm_cap_top - dm_cap_bottom) / (blex_cap_top - blex_cap_bottom)
    lc_scale_y = (dm_lc_top - dm_lc_bottom) / (blex_lc_top - blex_lc_bottom)

    # Calculate the vertical center of DM Mono's cell
    # The cell spans from dm_cap_top to the descender limit
    dm_cell_center = (dm_cap_top + (-250)) / 2

    # The center of BlexMono's glyph area
    blex_cell_center = (blex_cap_top + (-250)) / 2

    print("  DM Mono:  cap top={}, cap bottom={}, lc top={}, lc bottom={}, width={}".format(
        dm_cap_top, dm_cap_bottom, dm_lc_top, dm_lc_bottom, dm_mono_width))
    print("  BlexMono: cap top={}, cap bottom={}, lc top={}, lc bottom={}".format(
        blex_cap_top, blex_cap_bottom, blex_lc_top, blex_lc_bottom))
    print("  Scale factors: capitals={:.4f}, lowercase={:.4f}".format(cap_scale_y, lc_scale_y))

    # Ensure Unicode encoding
    dm_font.encoding = 'UnicodeFull'
    blex_font.encoding = 'UnicodeFull'

    total_copied = 0
    caps = 0
    lc = 0
    center_aligned = 0
    preserved = 0
    skipped = 0

    for start, end, range_name, align_mode in GLYPH_RANGES:
        range_count = 0

        for cp in range(start, end + 1):
            # Skip if already exists and has content in DM Mono
            try:
                if cp in dm_font and has_content(dm_font, cp):
                    skipped += 1
                    continue
            except:
                pass

            # Check if exists and has content in BlexMono
            try:
                if cp not in blex_font or not has_content(blex_font, cp):
                    continue
            except:
                continue

            # Verify the glyph slot exists in BlexMono
            blex_glyph = blex_font[cp]
            if not blex_glyph or not blex_glyph.isWorthOutputting():
                continue

            # Get original BlexMono bounding box before any operations
            try:
                orig_bb = blex_glyph.boundingBox()
            except:
                continue

            # Select and copy from BlexMono
            blex_font.selection.select(cp)
            blex_font.copy()

            # Create glyph slot in DM Mono if needed
            try:
                if cp not in dm_font:
                    dm_font.createChar(cp)
            except:
                continue

            # Paste into DM Mono
            dm_font.selection.select(cp)
            dm_font.paste()

            dm_glyph = dm_font[cp]
            if not dm_glyph or not dm_glyph.isWorthOutputting():
                continue

            # Get bounding box after paste
            try:
                bb = dm_glyph.boundingBox()
            except:
                continue

            if bb[2] <= bb[0] and bb[3] <= bb[1]:
                continue

            # Apply alignment based on mode
            if align_mode == "letter":
                # Scale and baseline-align for letters
                if is_capital_cyrillic(cp):
                    is_cap = True
                    is_lc = False
                elif is_lowercase_cyrillic(cp):
                    is_cap = False
                    is_lc = True
                else:
                    # Guess from bounding box
                    glyph_height = bb[3] - bb[1]
                    is_cap = glyph_height > (dm_cap_top - dm_cap_bottom) * 0.6
                    is_lc = not is_cap

                y_scale = cap_scale_y if is_cap else lc_scale_y

                if abs(y_scale - 1.0) > 0.001:
                    dm_glyph.transform(psMat.scale(1.0, y_scale))

                try:
                    post_bb = dm_glyph.boundingBox()
                except:
                    continue

                has_descender = bb[1] < -30

                if has_descender:
                    y_offset = 0
                elif is_cap:
                    y_offset = -post_bb[1]
                else:
                    y_offset = dm_lc_bottom - post_bb[1]

                if abs(y_offset) > 0.5:
                    dm_glyph.transform(psMat.translate(0, y_offset))

                if is_cap:
                    caps += 1
                elif is_lc:
                    lc += 1

            elif align_mode == "center":
                # Center vertically in the cell for symbols (arrows, etc.)
                # BlexMono and DM Mono have similar cell heights, so just center
                glyph_center = (bb[3] + bb[1]) / 2
                # Center between cap height top and descender bottom
                cell_center = (dm_cap_top + dm_lc_bottom - 200) / 2
                y_offset = cell_center - glyph_center

                if abs(y_offset) > 0.5:
                    dm_glyph.transform(psMat.translate(0, y_offset))

                center_aligned += 1

            else:  # "preserve"
                # Keep original positioning — for box drawing and block elements
                # that need exact positions to connect properly
                preserved += 1

            # Set monospace width
            dm_glyph.width = dm_mono_width
            range_count += 1
            total_copied += 1

        print("    {} (U+{:04X}-U+{:04X}): {} glyphs ({})".format(
            range_name, start, end, range_count, align_mode))

    return total_copied, caps, lc, center_aligned, preserved


def process_variant(dm_filename, blex_filename, variant_name):
    """Process a single DM Mono/BlexMono variant pair."""
    dm_path = os.path.join(DM_MONO_DIR, dm_filename)
    blex_path = os.path.join(BLEX_DIR, blex_filename)
    output_filename = "DMMonoExtended-{}.ttf".format(variant_name)
    output_path = os.path.join(OUTPUT_DIR, output_filename)

    print("\n=== Processing {} ===".format(variant_name))
    print("  Source: {}".format(dm_path))
    print("  Source: {}".format(blex_path))
    print("  Output: {}".format(output_path))

    if not os.path.exists(dm_path):
        print("  ERROR: DM Mono not found: {}".format(dm_path))
        return False
    if not os.path.exists(blex_path):
        print("  ERROR: BlexMono not found: {}".format(blex_path))
        return False

    # Open fonts
    dm_font = fontforge.open(dm_path)
    blex_font = fontforge.open(blex_path)

    # Count glyphs
    dm_count = len([g for g in dm_font.glyphs()])
    blex_count = len([g for g in blex_font.glyphs()])
    print("  DM Mono glyphs: {}, BlexMono glyphs: {}".format(dm_count, blex_count))

    # Copy missing glyphs
    total, caps, lc, centered, preserved = copy_missing_glyphs(dm_font, blex_font)

    print("  Copied: {} total".format(total))
    print("    Letters: {} caps + {} lowercase".format(caps, lc))
    print("    Center-aligned symbols: {}".format(centered))
    print("    Preserved-position glyphs: {}".format(preserved))

    # Save
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    dm_font.generate(output_path)
    print("  Saved: {}".format(output_path))

    # Clean up
    dm_font.close()
    blex_font.close()
    return True


def main():
    """Main entry point."""
    print("=" * 60)
    print("DM Mono Glyph Extension")
    print("=" * 60)
    print("Adding missing glyphs from BlexMono:")

    for start, end, name, mode in GLYPH_RANGES:
        print("  {} (U+{:04X}-U+{:04X})".format(name, start, end))

    success = 0
    for dm_file, blex_file, variant_name in FONT_VARIANTS:
        try:
            if process_variant(dm_file, blex_file, variant_name):
                success += 1
        except Exception as e:
            print("  ERROR {}: {}".format(variant_name, e))
            import traceback
            traceback.print_exc()

    print("\n{0}".format("=" * 60))
    print("Done: {}/{} variants processed".format(success, len(FONT_VARIANTS)))
    print("Output: {}/".format(OUTPUT_DIR))
    print("Next step: run patch.sh to add Nerd Font icons")
    print("{0}".format("=" * 60))


if __name__ == "__main__":
    main()
