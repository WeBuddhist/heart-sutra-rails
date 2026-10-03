# Vault Annex — heart-sutra conventions

The methodology guidelines (`0-VAULT-Structure.md`, `../../1-SOURCES/About Sources.md`, `../../2-RAILS/About Rails.md`, `../../3-TRANSFORMATIONS/About Transformations.md`) are **text-agnostic** — they apply to any Railroads vault built on any classical text. This annex records the conventions that are specific to *this* vault: **the Heart Sūtra — བཅོམ་ལྡན་འདས་མ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་སྙིང་པོ། / प्रज्ञापारमिताहृदय**.

When the Guidelines and this annex disagree on a vault-specific detail, this annex wins — **for the points it actually states**. Everything it does not state follows the defaults unchanged.

Sections 1–3 and 7 were filled at the first intake of the corpus (2026-10-03, `aligned-corpus-intake`, Route B); the intake report is `0-INBOX/heart-sutra-intake-report.md`.

---

## 1. The text

This vault serves **the Heart Sūtra** in its long recension — the Sanskrit text, its Tibetan translation, a Chinese translation made from the Tibetan, and nine Tibetan commentaries, all segmented and aligned by hand by the Dzongsar team.

| Order | Text | Role | File |
| ----- | ---- | ---- | ---- |
| 1 | प्रज्ञापारमिताहृदय | **Root** (Sanskrit) | `1-SOURCES/Text/sa-prajnaparamita-hrdaya.md` |
| 2 | བཅོམ་ལྡན་འདས་མ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་སྙིང་པོ། | Translation of 1 — **the stored Tibetan text** (the "display" segmentation) | `1-SOURCES/Translations/bo-prajnaparamita-hrdaya.md` |
| 3 | 般若波羅密多心經 | Translation of 2 | `1-SOURCES/Translations/zh-prajnaparamita-hrdaya.md` |

**Direction of every relation (decision of the vault owner, 2026-10-03).** The Sanskrit came first, so it is the root and the Tibetan is its translation. Everything that was aligned to the Tibetan — the Chinese and every commentary — points at the Tibetan file (`root_text:` and every transclusion) and is uploaded that way. Nothing is re-pointed to the Sanskrit: data stays true to what the humans aligned.

**One segmentation per text.** The library stores each text once, with one segmentation. Every other cut of the same text in the raw data (each commentary's own copy of the root, the Tibetan side of the Tibetan–Chinese pair) is carried onto the stored segmentation by letters (`4-SYSTEM/Skills/aligned-corpus-intake/scripts/concordance.py`) and kept only as evidence in the sidecars.

---

## 2. Addressing scheme

### Root and translations — `verse_id_format: section-paragraph`

Ids are **dictated by the table of contents**, like the commentaries' (decision of the vault owner, 2026-10-03): headings `^<decimal-path>-0`, body blocks `^<top-level>-<n>`, the title line before the first heading `^0-1`.

The root has no outline of its own, and the Dzongsar data has no TOC for it. Its TOC is the **table of contents of the Derge Kangyur Heart Sūtra on Wikisource** (Index:ཤེས་རབ་སྙིང་པོ། སྡེ་དགེ།.pdf, revision 1228972) — three sections: མདོའི་གླེང་གཞི། · མདོ་དོན་དངོས། · མཇུག་བྱང་། (`2-RAILS/Sections/Raw/toc-wikisource/prajnaparamita-hrdaya.md`). Each heading stands where the Index's proofread pages put it, found by letters in the rows of the Tibetan display text (section 1 opens at རྒྱ་གར་སྐད་དུ, section 2 at Śāriputra's question), and is carried onto the Sanskrit and the Chinese through their own row pairings; each file carries the headings **in its own language** — the Tibetan verbatim from Wikisource, the Sanskrit (निदानम् · सूत्रार्थः · अनुवादकपुष्पिका) and Chinese (序分 · 正宗分 · 譯跋) as editorial renderings in each text's own vocabulary. The document's own title line precedes the first heading (`^0-1`). Section 3 is the translators' colophon, which the Dzongsar text lacks: on the vault owner's instruction it is **added to the Tibetan from the Wikisource Derge page** (manifest `supplement_rows`, row 33, provenance in its sidecar entry); the Sanskrit and Chinese have no counterpart and show sections 1–2. Built by `wiki-toc-import` through the manifest setting `toc: {kind: outline}`.

### Commentaries — `verse_id_format: section-paragraph`

Ids are **dictated by the table of contents**, which is applied before any id or transclusion is written (decision of the vault owner, 2026-10-03):

| Markdown | Role | Anchor |
| -------- | ---- | ------ |
| `#` | The title | `^0` |
| `##` … `######` | TOC node, depth 1 … | `^<decimal-path>-0`, e.g. `^2-1-3-0` (full path, no cap; depth ≥ 6 bolded) |
| body block | One human row of the alignment doc | `^<top-level>-<n>` — n counts the blocks under the current top-level heading, through deeper headings, restarting at each top-level heading |
| body block before the first heading | — | `^0-<n>` |

Where each commentary's TOC comes from is recorded in its `intake` frontmatter and in the manifest: the Dzongsar TOC doc's labels (Tāranātha), the commentary's table of contents on its Wikisource Index page (Vimalamitra — `2-RAILS/Sections/Raw/toc-wikisource/<id>.md`), a `toc-generate` tree (`2-RAILS/Sections/Raw/toc-tree/<id>.md`), or none (with the reason).

### Verse numbering rule

Not applicable: the root is one short text without verses or chapters. Ids follow rows (root, translations) or sections (commentaries) as above.

### ⚑ Registered deviations — overrides of the default conventions

#### ⚑ Root and translation TOC taken from Wikisource — overrides `annotation-conventions.md` §1–§2 (registered 2026-10-03, revised the same day)

Files: the three files in §1. The default gives a root text the headings of its own structure (its author's TOC). The Heart Sūtra has none; its headings are the table of contents of the Derge Kangyur edition on Wikisource, placed through the human row alignment (see "Root and translations" above), and the Sanskrit and Chinese headings are editorial renderings of the Tibetan ones. **Why:** the vault owner directed that the root texts carry a TOC and that their segment ids follow it, and chose the Wikisource Index's table of contents. Two earlier versions the same day were replaced on the vault owner's instruction: a projection of Lobsang Gyaltsen Sengge's `toc-generate` outline (far too granular, and Tibetan headings in the Sanskrit and Chinese files), then a six-part summary outline from the Tibetan Wikipedia article.

#### ⚑ Text added to the Tibetan root from another edition — overrides `About Sources.md` (one source per file) (registered 2026-10-03)

File: `1-SOURCES/Translations/bo-prajnaparamita-hrdaya.md`, block `^3-1`. The translators' colophon (རྒྱ་གར་གྱི་མཁན་པོ་བི་མ་ལ་མི་ཏྲ་དང་། ལོཙྪ་བ་དགེ་སློང་རིན་ཆེན་སྡེས་བསྒྱུར་…) is absent from the Dzongsar text and was added verbatim from the Derge Kangyur on Wikisource (Page:ཤེས་རབ་སྙིང་པོ། སྡེ་དགེ།.pdf/3, revision 1239769). **Why:** the vault owner asked for it so that the Wikisource TOC's section 3, མཇུག་བྱང་།, has its text. Its provenance (page, revision, edition, who decided) is in the manifest and in the block's sidecar entry (`source.supplement`).

#### ⚑ Two alignment rows of Vimalamitra's commentary split — overrides the intake's one-row-one-block rule (registered 2026-10-03)

File: `1-SOURCES/Commentaries/bo-vimalamitra-tika.md`. Wikisource puts three of the commentary's eight headings inside Dzongsar alignment rows: row 10 is cut into three blocks (before ད་ནི་ཐོས་པའི་རང་གི་ངོ་བོ་བསྟན་པའི་ཕྱིར། and before དགེ་སློང་གི་དགེ་འདུན་ཆེན་པོ་དང་ཞེས་…), row 12 into two (before དོན་དམ་པའི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་). Every letter stays; each part keeps its row number in the sidecar; each root segment the row transcluded is shown once, before the first part that comments on it. **Why:** the vault owner chose to split the rows so that every heading stands exactly where Wikisource has it (manifest `row_splits`).

#### ⚑ Commentary `##` labels come from the TOC, not from a hand-written label — overrides `annotation-conventions.md` §3 (registered 2026-10-03)

Files: `1-SOURCES/Commentaries/*.md`. The default has a contributor write each `##` heading's label by hand. Here the label is the TOC node's number (the order of the Dzongsar TOC doc's labels, or the `toc-generate` tree's decimal path). **Why:** the vault owner directed that segment ids be dictated by the TOC sections; the TOCs come from the human TOC doc or from the commentary's own *sa bcad*, so the numbering is attested, not invented.

#### ⚑ Blocks before the first heading are section 0 without a `## 0` heading — overrides `add-block-ids` Mode 1 rule 6 (registered 2026-10-03)

Files: `1-SOURCES/Commentaries/*.md`. A commentary's title line and opening verses usually precede its first TOC node; they take `^0-1`, `^0-2`, … under the `#` title rather than an invented `## 0. Introduction` heading. A commentary with no TOC (see §3) is section 0 throughout.

### Re-segmentation and ID-migration log

**2026-10-03 — first intake.** No migration. An earlier, docx-based intake attempt of 2026-10-02 was superseded before anything cited it (its manifest is in git history).

**2026-10-03 (later the same day) — root and translation ids re-keyed.** The Sanskrit, Tibetan and Chinese files first carried flat ids (`^N` = alignment-row number); on the vault owner's instruction they now carry a TOC and section ids (`^1-12`). Every transclusion into them (Tibetan → Sanskrit, Chinese → Tibetan, all nine commentaries → Tibetan) was regenerated by the same build. Nothing in `2-RAILS/` cited those ids, so nothing else had to be re-checked. The row number of every block remains in its sidecar entry (`source.row`).

**2026-10-03 (later still) — root, translation and Vimalamitra TOCs replaced; their ids re-keyed.** On the vault owner's instruction, the root's TOC (projected from Lobsang Gyaltsen Sengge's outline) and Vimalamitra's `toc-generate` tree were replaced by the tables of contents on their Wikisource Index pages (Derge; `2-RAILS/Sections/Raw/toc-wikisource/`). An intermediate version taken from the Tibetan Wikipedia articles (six summary sections for the root, 4+5 for Vimalamitra) was built and replaced the same day; nothing cited it. Ids changed in the Sanskrit, Tibetan and Chinese files (e.g. the Tibetan `^1-12` གཟུགས་སྟོང་པའོ… is now `^2-3`) and in `bo-vimalamitra-tika.md`, which also gained three blocks from the two split rows; the Tibetan gained `^3-1`, the translators' colophon added from Wikisource. Every transclusion into the root files — Tibetan → Sanskrit, Chinese → Tibetan, all nine commentaries → Tibetan — was regenerated by the same build, and each changed link was checked to resolve to the same text as before; the other eight commentaries' own ids did not change. Nothing in `2-RAILS/` or `3-TRANSFORMATIONS/` cited the changed ids. Of the five commentaries the vault owner's sheet lists, only Vimalamitra's is in this vault; Alak Shaten Dar's, Mahājana's, Atiśa's and Rongtön's are not, and were skipped. The superseded Vimalamitra tree stays in `2-RAILS/Sections/Raw/toc-tree/` as evidence.

**2026-10-03 (last) — Chinese rows merged to one block per Tibetan segment.** On the vault owner's instruction, consecutive rows of `zh-prajnaparamita-hrdaya.md` that transclude the same Tibetan segment were joined into one block (manifest `merge_rows: by_target`, joined with a space, the Chinese text's own phrase separator): 111 blocks became 30, one per Tibetan segment the Chinese translates — the Tibetan's closing title (`^2-21`) and translators' colophon (`^3-1`) have no Chinese. The Chinese ids now coincide with the Tibetan ones they transclude (zh `^2-3` ↔ bo `^2-3`). The Chinese text is unchanged apart from the joining spaces, the Tibetan segments shown are the same and in the same order, and every row with its own alignment stays in the sidecar (`source.merged_rows`). Nothing cited the Chinese ids.

**2026-10-03 — Sanskrit editorial brackets removed (no id change).** On the vault owner's instruction, the three square-bracket pairs of the Sanskrit edition (words its editor supplied: `^0-1` विस्तरमातृका, `^2-1` वा कुलदुहिता वा अस्यां, `^2-2` अस्यां) were removed and the words kept (manifest `text_corrections`), because Obsidian rendered them like link syntax. The bracketed originals stay in the manifest and the sidecar (`source.corrections`).

---

## 2a. Canonical spine slots — *not yet defined*

The claims pipeline has not been run in this vault. When it is, register the spine here first.

---

## 3. Registered commentary IDs

Every commentary file in `1-SOURCES/Commentaries/` declares a `registered_id` in its frontmatter. That short ID is the only string used to attribute claims to the commentary throughout `2-RAILS/`. Once assigned, a `registered_id` never changes.

| `registered_id` | Author / Title | School or tradition | BDRC work | Language | TOC source | File |
| --------------- | -------------- | ------------------- | --------- | -------- | ---------- | ---- |
| `vairocana-ngagsu-trelwa` | ལོ་ཆེན་བཻ་རོ་ཙ་ན། — ཤེས་རབ་སྙིང་པོའི་འགྲེལ་པ་སྔགས་སུ་བཀྲལ་པ། | — | WA0XLEABEC8EFB500 | Tibetan | none (no *sa bcad*) | `1-SOURCES/Commentaries/bo-vairocana-ngagsu-trelwa.md` |
| `vajrapani-dongyi-dronma` | ཕྱག་ན་རྡོ་རྗེ། — …སྙིང་པོའི་འགྲེལ་པ་དོན་གྱི་སྒྲོན་མ་ཞེས་བྱ་བ། | — | WA0RT3165 | Tibetan | `toc-generate` tree (one announced division) | `1-SOURCES/Commentaries/bo-vajrapani-dongyi-dronma.md` |
| `taranatha-tsikdrel` | ཇོ་ནང་རྗེ་བཙུན་ཏཱ་ར་ནཱ་ཐ། — ཤེར་ཕྱིན་སྙིང་པོའི་མདོའི་ཚིག་འགྲེལ་རྨད་དུ་བྱུང་བ་བཞུགས། | Jonang | WA0XLBC8FE150050C | Tibetan | Dzongsar TOC doc labels | `1-SOURCES/Commentaries/bo-taranatha-tsikdrel.md` |
| `vimalamitra-tika` | པཎ་ཆེན་དྲི་མེད་བཤེས་གཉེན། — ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་སྙིང་པོའི་རྒྱ་ཆེར་བཤད་པ། | — | WA0RT3163 | Tibetan | Wikisource Index TOC (Derge, revision 1239856) | `1-SOURCES/Commentaries/bo-vimalamitra-tika.md` |
| `ngawang-nyima-drelwa` | སྒོ་མང་མཁན་ཟུར་ངག་དབང་ཉི་མ། — ཤེས་རབ་སྙིང་པོའི་འགྲེལ་བ། | — | WA0XLB18EA1811A74 | Tibetan | `toc-generate` tree | `1-SOURCES/Commentaries/bo-ngawang-nyima-drelwa.md` |
| `prasastrasena-tika` | སློབ་དཔོན་པྲ་ཤཱ་སྟྲ་སེ། — འཕགས་པ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་སྙིང་པོའི་རྒྱ་ཆེར་འགྲེལ་པ། | — | WA0RT3166 | Tibetan | `toc-generate` tree | `1-SOURCES/Commentaries/bo-prasastrasena-tika.md` |
| `lobzang-gyaltsen-senge-nyinje` | གཙོས་ཁྲི་སྤྲུལ ༠༢་བློ་བཟང་རྒྱལ་མཚན་སེངྒེ། — གཞུང་མཆོག་ཤེས་རབ་སྙིང་པོའི་རྣམ་བཤད་ཟབ་དོན་པད་དཀར་བཞད་པའི་ཉིན་བྱེད། | — | WA0XL9624A799C650 | Tibetan | `toc-generate` tree | `1-SOURCES/Commentaries/bo-lobzang-gyaltsen-senge-nyinje.md` |
| `gendun-rinchen-migje` | འབྲུག་རྗེ་མཁན་པོ ༦༩་དགེ་འདུན་རིན་ཆེན། — ཤེས་རབ་སྙིང་པོའི་རྣམ་བཤད་ཡང་དག་ལྟ་བའི་མིག | — | WA0XL29B7CCC47F6B | Tibetan | `toc-generate` tree | `1-SOURCES/Commentaries/bo-gendun-rinchen-migje.md` |
| `lama-kunga-shebum` | བླ་མ་ཀུན་དགའ། — འཕྲ་ཏིག་དང་པོ། ཤེས་རབ་སྙིང་པོའི་བཤད་འབུམ། | — | WA0XLBA22F3396909 | Tibetan | `toc-generate` tree | `1-SOURCES/Commentaries/bo-lama-kunga-shebum.md` |

School is left blank where the raw data does not record it (the Jonang attribution of Tāranātha is in his name as recorded, ཇོ་ནང་རྗེ་བཙུན་).

**Tier ordering.** These are independent works, not a root commentary with sub-commentaries. Present them in the order of this roster (the order of the Dzongsar catalogue). Do not invent a hierarchy.

### Typed folder — `1-SOURCES/Annotations/`

One `<stem>.annotations.json` sidecar per source file, written only by `aligned-corpus-intake`. It keeps what markdown cannot: each block's alignment-doc row and raw export text, emphasis spans, the paired row's text, every target segment with the letters and character span it covers, the variants between editions, human corrections with the original pairing, and where each heading's label really sat. Machine data: rails cite the source block, never the sidecar.

---

## 4. Language tracks

| Tag | Language | Role | Translation track | Plan stream |
| --- | -------- | ---- | ----------------- | ----------- |
| `sa` | Sanskrit | Root (source) | — | — |
| `bo` | Tibetan | Translation of the root; the text the commentaries comment on | — | — |
| `zh` | Chinese (Traditional) | Translation of the Tibetan | — | — |

No transformation tracks exist yet.

### Analysis language per rail section

The default: Traditional Interpretation paraphrases and Translation Notes in English, everything else in the original language. No departures recorded.

---

## 5. Bilingual glossary pairs

None yet.

---

## 6. Active transformation tracks

None yet.

---

## 7. Source-language tags used in this vault

| Tag | Script / System | Use in this vault |
| --- | --------------- | ----------------- |
| `-sa` | Devanāgarī | The Sanskrit root |
| `-bo` | Unicode Tibetan | The Tibetan translation and all commentaries |
| `-zh` | Unicode Traditional Chinese | The Chinese translation |

---

## 8. Where to look next

- [`0-VAULT-Structure.md`](0-VAULT-Structure.md) — the architecture in full.
- [`../../1-SOURCES/About Sources.md`](../../1-SOURCES/About%20Sources.md) — source-file rules.
- [`../../2-RAILS/About Rails.md`](../../2-RAILS/About%20Rails.md) — rails schema.
- [`../../3-TRANSFORMATIONS/About Transformations.md`](../../3-TRANSFORMATIONS/About%20Transformations.md) — track and output rules.
- [`annotation-conventions.md`](annotation-conventions.md) — the default block-ID conventions this annex registers deviations from.
- [`../How-to guides/Ingest a row-aligned corpus.md`](../How-to%20guides/Ingest%20a%20row-aligned%20corpus.md) — how this corpus was ingested, step by step.
- [`../CLAUDE.md`](../CLAUDE.md) — the operational quick-reference. *This annex overrides it on the points recorded above.*
- [Top-level `README.md`](../../README.md) — pipeline overview and reading paths.
