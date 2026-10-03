### `aligned-corpus-intake` **[exists]**
Converts a human-segmented, human-aligned corpus — OpenPecha API downloads and Dzongsar-style Google-Docs exports (Tsadel/Tsadrel line-parallel alignments, sentence segmentations, citation and *sa bcad* TOC docs, numbered alignment references, metadata sheets) — into publishable `1-SOURCES/` root texts, translations and commentaries with headings, block ids and transclusions, plus a lossless annotation sidecar per file. Manifest-driven; a verifier proves no source letter was lost. **Route B** (`md_rows`) takes the same Docs downloaded as Markdown row-for-row pairs plus CSV metadata and carries every commentary's and translation's row alignment onto the one stored segmentation of the root by letters, without changing any segmentation: TOC first (TOC-doc labels, or a `toc-generate` tree placed at row boundaries), then section ids, then transclusions.
**Inputs:** raw data in `0-INBOX/raw-data/` and an intake manifest listing each work and its raw files.
**Outputs:** `1-SOURCES/{Text,Translations,Commentaries}/*.md`, `1-SOURCES/Annotations/*.annotations.json`, an intake report in `0-INBOX/`.
→ [`aligned-corpus-intake/SKILL.md`](aligned-corpus-intake/SKILL.md)

### `wiki-toc-import` **[exists]**
**Purpose:** Take a text's table of contents from its proofread Wikisource Index page (or, on request, its Wikipedia article) and apply it to the root, its translations (headings in each file's own language) and any commentary with its own Index page, replacing a missing or over-granular TOC.
**Inputs:** Wikisource Index page (or Wikipedia) links for the text and its commentaries, and an `aligned-corpus-intake` manifest of row-aligned works.
**Outputs:** `2-RAILS/Sections/Raw/toc-wikisource/<id>.md` (revision-pinned outline placed on rows, labels per language), the manifest's `toc: {kind: outline}` plus any human-decided `row_splits` / `supplement_rows`, and the rebuilt `1-SOURCES/` files with ids and transclusions regenerated.
→ [`wiki-toc-import/SKILL.md`](wiki-toc-import/SKILL.md)
