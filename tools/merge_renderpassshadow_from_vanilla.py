# -*- coding: utf-8 -*-
"""
Reaplica o 'boost' de sombras (espírito do mod gráfico original) sobre
renderpassshadow.xml extraído do 0003/0.paz *actual* do jogo.

Uso (depois de extraíres 0.paz com CD.PAZ.Tool ou similar):
  python merge_renderpassshadow_from_vanilla.py --input "caminho/vanilla/renderpassshadow.xml" --output "caminho/saida/renderpassshadow.xml"
"""
from __future__ import annotations

import argparse
from pathlib import Path

REPLACEMENTS = [
    (
        '<Rasterizer MultiSampleEnable="True" MultiSampleCount="4" SlopeScaledDepthBias="1.0" MultisampleShadow="True"/>',
        '<Rasterizer MultiSampleEnable="True" MultiSampleCount="32" SlopeScaledDepthBias="4.0" MultisampleShadow="True"/>',
    ),
    (
        '<Rasterizer MultiSampleEnable="True" MultiSampleCount="4" SlopeScaledDepthBias="2.0" MultisampleShadow="True"/>',
        '<Rasterizer MultiSampleEnable="True" MultiSampleCount="32" SlopeScaledDepthBias="4.0" MultisampleShadow="True"/>',
    ),
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
    p.add_argument("--input", required=True, type=Path, help="renderpassshadow.xml do jogo (vanilla, extraído do paz)")
    p.add_argument("--output", required=True, type=Path, help="Ficheiro de saída a sobrescrever/criar")
    args = p.parse_args()
    text = args.input.read_text(encoding="utf-8")
    out = text
    for a, b in REPLACEMENTS:
        out = out.replace(a, b)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(out, encoding="utf-8")
    print("Wrote", args.output, "size", args.output.stat().st_size)
    if out == text:
        print("AVISO: nenhuma substituição bateu — confirma que o ficheiro é o vanilla esperado.")


if __name__ == "__main__":
    main()
