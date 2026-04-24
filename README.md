# Enhanced internal Graphics (no ReShade) — **v3.0.0 fix**

**EN (short):** Community fix for the internal graphics XML mod after a **game update**. The original full `renderpassshadow.xml` from older builds **crashes** the current client. v3 keeps **current** engine data and only applies the **shadow quality** tweaks + the other safe pass files. **Not** a ReShade preset.

**Mod original (autor):** [Nexus Mods — Crimson Desert mod 651](https://www.nexusmods.com/crimsondesert/mods/651?tab=description) — este repositório é um **fork/fix**; créditos ao autor do pacote base.

**Repo:** [github.com/evertongomesjob/Enhanced-internal-Graphics-no-reshade-](https://github.com/evertongomesjob/Enhanced-internal-Graphics-no-reshade-)

---

## Conteúdo (mesma árvore que o mod original)

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

Instala no mod manager como **mod RAW** de ficheiros (pasta `files` na raiz do mod), tal como o pacote original.

---

## Como usar (jogador)

1. Faz **backup** do perfil de mods / desactiva outros mods gráficos que touquem nos mesmos XMLs.
2. Coloca esta pasta no directório de mods do **Crimson / mod manager** que usas (o caminho depende da ferramenta).
3. **Activa só este mod** (ou resolve conflitos se outro mod editar os mesmos ficheiros).
4. Se o jogo actualizar de novo: vê a secção “Após um patch do jogo” abaixo.

---

## O que estava a falhar (e como foi resolvido)

### Sintoma

- Com o **pacote completo antigo** (v2.x do Nexus), o jogo podia **nem abrir** — crash no arranque após uma **atualização** do cliente.

### Causa técnica (resumida)

- Muitos dados de renderização estão dentro de `Crimson Desert\0003\0.paz` (não são ficheiros soltos na pasta do jogo).
- O ficheiro **`renderpassshadow.xml` completo** do mod era de uma **build antiga**: faltavam ou sobravam **passes**, **condições** e **atributos** que o motor **actual** espera. Carregar o XML antigo = estado inválido = crash.
- O resto do mod (pós-processo, etc.) em muitos casos continua **compatível** por ficheiro; o **shadow** era o que mais “partia” com o ficheiro inteiro trocado.

### Solução da v3

1. **Extrair** o `renderpassshadow.xml` **oficial** do teu jogo a partir de `0003\0.pam` + `0.paz` (ver ferramenta abaixo).
2. Aplicar **só** o “reforço” de sombras no espírito do mod clássico: sobretudo `MultiSampleCount` mais alto e `SlopeScaledDepthBias` alinhado ao que o mod antigo fazia, **sem** apagar o que o patch novo acrescentou (passes novos, nomes de elementos, `Condition` por plataforma, etc.).
3. Manter os **outros 7** XMLs do mod original nessa árvore, que na prática se mostraram **estáveis** com o cliente actual — **sem** forçar de volta o `renderpass.xml` / `rendererconfiguration.xml` / `featuresandextensions.xml` completos (isso voltaria a levantar o risco de crash).

Ferramenta de extração usada na validação: **[CD.PAZ.Tool (Ekey)](https://github.com/Ekey/CD.PAZ.Tool)** — `CD.Unpacker` com o caminho do `0.pamt`.

Script de re-merge para maintainers: `tools/merge_renderpassshadow_from_vanilla.py` (lê o vanilla, escreve o ficheiro a usar no mod).

---

## Após um patch do jogo (manutenção)

1. Verifica ficheiros do jogo / actualiza o cliente.
2. Extrai de novo o `renderpass/renderpassshadow.xml` de `0003` do jogo.
3. Corre:

   ```text
   python tools/merge_renderpassshadow_from_vanilla.py --input "...\renderpassshadow.xml" --output "files\0003\renderpass\renderpassshadow.xml"
   ```

4. Se **algum** dos outros 7 XMLs deixar de funcionar, volta a isolar o culpado (desactiva um a um) e abre *issue* neste repositório com a tua build.

Se as linhas do vanilla **mudarem** ligeiramente (espaços, novos biases), podes ter de ajustar as *strings* em `REPLACEMENTS` no script — é normal após rewrites da Pearl Abyss.

---

## Créditos e licença de conteúdo

- **Mod gráfico base (autor original):** [Nexus — mod 651](https://www.nexusmods.com/crimsondesert/mods/651?tab=description) — cumpre a licença / termos do Nexus e do autor se redistribuíres ficheiros derivados.
- **Fix v3 / documentação / script de merge:** mantenedor deste repositório; o código do script pode ser reutilizado livremente para o mesmo fim.
- **Extração PAZ:** [Ekey / CD.PAZ.Tool](https://github.com/Ekey/CD.PAZ.Tool)
- O jogo **Crimson Desert** e os activos originais pertencem à **Pearl Abyss**; este repositório **não** contém ficheiros do jogo, apenas XMLs de *override* de mods.

---

## Subir o v3 para o GitHub (para quem clonou vazio o repo)

No PC, a partir desta pasta (ou onde a copiaste):

```bash
cd Enhanced-internal-Graphics-no-reshade
git init
git add .
git commit -m "Release v3.0.0 — fix post-update internal graphics"
git branch -M main
git remote add origin https://github.com/evertongomesjob/Enhanced-internal-Graphics-no-reshade-.git
git push -u origin main
```

**Release no GitHub:** *Releases → Create a new release → Tag* `v3.0.0` *→ anexa um ZIP* com a pasta (ou só `files` + `README`, conforme preferires partilhar).

---

## Aviso

Mods podem ser desactualizados por patches; testa com conta / save de backup. Este pacote **não** é suporte oficial da Pearl Abyss.
