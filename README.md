# Enhanced internal Graphics (no ReShade) — **v3.0.0 fix**

Community fix for the **internal graphics XML** mod after a **game update**. The original full `renderpassshadow.xml` from older builds can **crash** the current client. v3 keeps **up-to-date** engine data and only applies the **shadow quality** tweaks plus the other safe pass files. This is **not** a ReShade preset.

**Original mod (author):** [Nexus Mods — Crimson Desert mod 651](https://www.nexusmods.com/crimsondesert/mods/651?tab=description) — this repo is a **fork/fix**; credit goes to the original pack author.

**Repository:** [github.com/evertongomesjob/Enhanced-internal-Graphics-no-reshade-](https://github.com/evertongomesjob/Enhanced-internal-Graphics-no-reshade-)

---

## Contents (same tree as the original mod)

```
files/
  0003/
    renderpass/
      renderpassshadow.xml
      renderpassssdm.xml
      renderpasspostprocess.xml
      renderpassglobalillumination.xml
      renderpassatmosphericscattering.xml
      renderpassfiltering.xml
      renderpasseffect.xml
      renderpassraytracing.xml
```

Install through your mod manager as a **file-based (RAW) mod** with a `files` folder at the mod root, like the original package.

---

## How to use (players)

1. **Back up** your mod profile and disable other graphics mods that override the same XMLs.
2. Drop this folder into your **Crimson mod manager** mod directory (path depends on the tool you use).
3. **Enable this mod** (or resolve conflicts if another mod touches the same files).
4. After a future game update, see “After a game patch” below.

---

## What broke and how v3 fixes it

### Symptom

- With the **old full pack** (v2.x on Nexus), the game could **fail to start** — crash on launch after a **client update**.

### Technical cause (short)

- A lot of render data lives inside `Crimson Desert\0003\0.paz` (not loose files in the game folder).
- The mod’s full **`renderpassshadow.xml`** came from an **old build**: **missing or extra** passes, **conditions**, and **attributes** that the **current** engine expects. Loading the old XML = invalid state = crash.
- Other parts of the mod (post-process, etc.) are often still **per-file compatible**; **shadow** was the worst offender when the entire file was replaced.

### v3 approach

1. **Extract** the **official** `renderpassshadow.xml` from your game under `0003\0.pamt` / `0.paz` (see tool below).
2. Apply only the **shadow “boost”** in the spirit of the classic mod: higher `MultiSampleCount` and `SlopeScaledDepthBias` aligned with the old mod, **without** stripping what a new patch added (new passes, element names, platform `Condition`, etc.).
3. Keep the **other seven** XMLs from the original mod in that tree; they have been **stable** on current clients — we do **not** ship full `renderpass.xml` / `rendererconfiguration.xml` / `featuresandextensions.xml` (that would raise crash risk again).

Extraction tool used for validation: **[CD.PAZ.Tool (Ekey)](https://github.com/Ekey/CD.PAZ.Tool)** — run `CD.Unpacker` on `0.pamt`.

Maintainer re-merge script: `tools/merge_renderpassshadow_from_vanilla.py` (reads vanilla, writes the mod’s `renderpassshadow.xml`).

---

## After a game patch (maintenance)

1. Verify game files / update the client.
2. Extract `renderpass/renderpassshadow.xml` from the game’s `0003` again.
3. Run:

   ```text
   python tools/merge_renderpassshadow_from_vanilla.py --input "path\to\renderpassshadow.xml" --output "files\0003\renderpass\renderpassshadow.xml"
   ```

4. If **any** of the other seven XMLs breaks, binary-search which file (disable one at a time) and open an **issue** with your build.

If vanilla line formatting **changes** slightly (whitespace, new bias values), you may need to update the `REPLACEMENTS` strings in the script — normal after Pearl Abyss engine updates.

---

## Credits and redistribution

- **Base graphics mod (original author):** [Nexus — mod 651](https://www.nexusmods.com/crimsondesert/mods/651?tab=description) — respect Nexus and the author’s license if you redistribute derivatives.
- **v3 fix / docs / merge script:** this repository’s maintainer; the script may be reused for the same purpose.
- **PAZ extraction:** [Ekey / CD.PAZ.Tool](https://github.com/Ekey/CD.PAZ.Tool)
- **Crimson Desert** and its assets are owned by **Pearl Abyss**; this repo does **not** ship game files—only mod override XMLs.

---

## First-time publish (empty remote)

From this folder (or a copy):

```bash
cd Enhanced-internal-Graphics-no-reshade
git init
git add .
git commit -m "Release v3.0.0 — fix post-update internal graphics"
git branch -M main
git remote add origin https://github.com/evertongomesjob/Enhanced-internal-Graphics-no-reshade-.git
git push -u origin main
```

**GitHub Release:** *Releases → Create a new release* → tag **`v3.0.0`** → attach a ZIP of the mod folder (or `files` + `README` only) if you prefer.

---

## Disclaimer

Mods can break on patches; test with a backup save. This is **not** official support from Pearl Abyss.
