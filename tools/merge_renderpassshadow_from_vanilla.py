# -*- coding: utf-8 -*-
"""
Reapply the classic graphics mod "shadow boost" on top of a vanilla
renderpassshadow.xml extracted from the current 0003/0.paz.

After unpacking 0.paz (e.g. CD.PAZ.Tool):
  python merge_renderpassshadow_from_vanilla.py --input "path/to/vanilla/renderpassshadow.xml" --output "path/to/output/renderpassshadow.xml"
"""
from __future__ import annotations

import argparse
from pathlib import Path

# Pairs: (vanilla line fragment, modded replacement). Keep in sync with game XML after patches.
REPLACEMENTS = [
    (
        '<Rasterizer MultiSampleEnable="True" MultiSampleCount="4" SlopeScaledDepthBias="1.0" MultisampleShadow="True"/>',
        '<Rasterizer MultiSampleEnable="True" MultiSampleCount="32" SlopeScaledDepthBias="4.0" MultisampleShadow="True"/>',
    ),
    (
        '<Rasterizer MultiSampleEnable="True" MultiSampleCount="4" SlopeScaledDepthBias="2.0" MultisampleShadow="True"/>',
        '<Rasterizer MultiSampleEnable="True" MultiSampleCount="32" SlopeScaledDepthBias="4.0" MultisampleShadow="True"/>',
    ),
    # Terrain: vanilla uses strong 15.0 bias — only raise MS count; keep bias as shipped.
    (
        '<Rasterizer MultiSampleEnable="True" MultiSampleCount="4" SlopeScaledDepthBias="15.0" MultisampleShadow="True"/>',
        '<Rasterizer MultiSampleEnable="True" MultiSampleCount="32" SlopeScaledDepthBias="15.0" MultisampleShadow="True"/>',
    ),
    (
        '<Rasterizer SlopeScaledDepthBias="2.0"/>',
        '<Rasterizer SlopeScaledDepthBias="4.0"/>',
    ),
]


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--input",
        required=True,
        type=Path,
        help="Vanilla renderpassshadow.xml (extracted from the .paz)",
    )
    p.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Output path to write (overwrites if present)",
    )
    args = p.parse_args()
    text = args.input.read_text(encoding="utf-8")
    out = text
    for a, b in REPLACEMENTS:
        out = out.replace(a, b)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(out, encoding="utf-8")
    print("Wrote", args.output, "size", args.output.stat().st_size)
    if out == text:
        print("WARNING: no replacements matched — check that the input is the expected vanilla file.")


if __name__ == "__main__":
    main()
