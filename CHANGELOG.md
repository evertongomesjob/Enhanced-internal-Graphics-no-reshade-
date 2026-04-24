# Changelog

## v3.0.0 (2026)

- **Compatibilidade pós-atualização do jogo:** o `renderpassshadow.xml` do mod original (Nexus) era de uma build antiga: ao substituir o ficheiro completo, o jogo podia *crashar* ao arranque. A v3 usa o ficheiro **atual** extraído de `Crimson Desert\0003\0.paz` e aplica só os ajustes de qualidade de sombra (amostras MS e bias) alinhados ao intuito do mod antigo.
- Inclui os outros passes gráficos testados (pós-processo, GI, RT, filtro, efeitos, atmosfera, SSDM) a partir do pacote v2.1 do autor, **sem** os ficheiros de núcleo `renderpass.xml` / `rendererconfiguration.xml` / `featuresandextensions.xml` (mantêm o vanilla no `0.paz`).
- Guia e script de manutenção em `tools/` para repetir o merge após futuros patches.

**Mod de referência (autor):** [Crimson Desert – Nexus Mods 651](https://www.nexusmods.com/crimsondesert/mods/651?tab=description) — a v3 é um *fork/fix*; crédito ao autor original.

**Repositório do fix:** [evertongomesjob/Enhanced-internal-Graphics-no-reshade-](https://github.com/evertongomesjob/Enhanced-internal-Graphics-no-reshade-)
