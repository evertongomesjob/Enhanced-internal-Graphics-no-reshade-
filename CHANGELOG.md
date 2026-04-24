# Changelog

## v3.0.0 (2026)

- **Post-update compatibility:** the original mod’s (Nexus) `renderpassshadow.xml` targeted an old build; replacing the file wholesale could **crash** on launch. v3 uses the **current** file extracted from `Crimson Desert\0003\0.paz` and applies only the shadow quality boosts (MS samples and depth bias) matching the old mod’s intent.
- Includes the other vetted pass files (post-process, GI, RT, filter, effects, atmosphere, SSDM) from the author’s v2.1 pack, **without** the core `renderpass.xml` / `rendererconfiguration.xml` / `featuresandextensions.xml` (vanilla in `0.paz` stays authoritative there).
- Maintenance guide and script under `tools/` to re-run the merge after future patches.

**Original mod (author):** [Crimson Desert — Nexus Mods 651](https://www.nexusmods.com/crimsondesert/mods/651?tab=description) — v3 is a **fork/fix**; credit the original author.

**Fix repository:** [evertongomesjob/Enhanced-internal-Graphics-no-reshade-](https://github.com/evertongomesjob/Enhanced-internal-Graphics-no-reshade-)
