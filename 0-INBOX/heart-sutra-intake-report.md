# Heart Sūtra — intake report (2026-10-03)

Skill: `aligned-corpus-intake`, Route B (`md_rows`). Manifest: `0-INBOX/raw-data/intake-manifest.yaml`. How-to for other texts: `4-SYSTEM/How-to guides/Ingest a row-aligned corpus.md`.

**Result** (rebuilt after the root TOC was added, same day): 12 files in `1-SOURCES/` (1 root, 2 translations, 9 commentaries) plus one sidecar each in `1-SOURCES/Annotations/`. `verify.py` on the vault: **OK for all 12, no source letter missing, every row exactly one block, every transclusion equal to the human row pairing.** Publication dry run (linter + parser on copies): the only error is the empty `category_id` (left for you); text, edition, TOC and alignment payloads build for every file.

---

## 1. The design, in brief

- **One stored segmentation per text.** The Tibetan "display" doc (32 rows) is the Tibetan the library stores. Each commentary was aligned against its own cut of the root (`sherab-root-N`); the Chinese against another cut and edition (`sherab-root-bo(bo-zh)`). Those cuts are mapped onto the display segments by letters (`concordance.py`): no segmentation was changed — not the display's, not a commentary's, not the Chinese.
- **Directions** (your decision): Sanskrit = root; Tibetan = its translation; the Chinese and every commentary point at the Tibetan.
- **TOC first, then ids, then transclusions** (your decision), in every file. Ids come from the sections (`^<top-level>-<n>`, the title line `^0-1`); headings carry their full path (`^1-3-2-0`).
- **The root's TOC** (your later instruction): the root has no outline of its own and the data has no TOC for it, so the Tibetan, Sanskrit and Chinese files carry **Lobsang Gyaltsen Sengge's outline, projected** through his human row alignment onto the display Tibetan, and from there through each pairing onto the Sanskrit and the Chinese (§5a).
- Registered in the annex: commentary ids, the `Annotations/` folder, three id-scheme deviations.

## 2. What was built

| Work | File | Blocks | Headings | Transclusions | Unaligned blocks | Spanning 2–3 segments | Target rows with no counterpart | TOC |
|---|---|---|---|---|---|---|---|---|
| `sa-root` | `1-SOURCES/Text/sa-prajnaparamita-hrdaya.md` | 29 | 24 | 0 | — | — | — | projected (Lobsang) |
| `bo-display` | `1-SOURCES/Translations/bo-prajnaparamita-hrdaya.md` | 31 | 25 | 28 | 3 | 0 | 1 | projected (Lobsang) |
| `zh-translation` | `1-SOURCES/Translations/zh-prajnaparamita-hrdaya.md` | 111 | 24 | 111 | 0 | 0 | 0 | projected (Lobsang) |
| `bo-vairocana-ngagsu-trelwa` | `1-SOURCES/Commentaries/bo-vairocana-ngagsu-trelwa.md` | 64 | 0 | 61 | 4 | 1 | 20 | none (no *sa bcad*) |
| `bo-vajrapani-dongyi-dronma` | `1-SOURCES/Commentaries/bo-vajrapani-dongyi-dronma.md` | 81 | 4 | 54 | 28 | 1 | 28 | `toc-generate` tree (4 nodes) |
| `bo-taranatha-tsikdrel` | `1-SOURCES/Commentaries/bo-taranatha-tsikdrel.md` | 79 | 23 | 62 | 19 | 1 | 5 | TOC-doc labels (23) |
| `bo-vimalamitra-tika` | `1-SOURCES/Commentaries/bo-vimalamitra-tika.md` | 62 | 9 | 56 | 7 | 1 | 7 | `toc-generate` tree (9) |
| `bo-ngawang-nyima-drelwa` | `1-SOURCES/Commentaries/bo-ngawang-nyima-drelwa.md` | 54 | 17 | 42 | 12 | 0 | 6 | `toc-generate` tree (17) |
| `bo-prasastrasena-tika` | `1-SOURCES/Commentaries/bo-prasastrasena-tika.md` | 70 | 11 | 59 | 13 | 2 | 15 | `toc-generate` tree (11) |
| `bo-lobzang-gyaltsen-senge-nyinje` | `1-SOURCES/Commentaries/bo-lobzang-gyaltsen-senge-nyinje.md` | 50 | 29 | 32 | 22 | 3 | 3 | `toc-generate` tree (29) |
| `bo-gendun-rinchen-migje` | `1-SOURCES/Commentaries/bo-gendun-rinchen-migje.md` | 62 | 34 | 40 | 25 | 3 | 6 | `toc-generate` tree (34) |
| `bo-lama-kunga-shebum` | `1-SOURCES/Commentaries/bo-lama-kunga-shebum.md` | 91 | 71 | 74 | 19 | 2 | 4 | `toc-generate` tree (71) |

*Unaligned blocks*: rows with text on this side and an empty counterpart (titles, homages, *sa bcad* rows, colophons, commentary-only passages) — kept, no transclusion. *Target rows with no counterpart*: root-copy rows the commentary has no text for (the commentator skipped them). A row that comments on part of a display segment repeats that segment's transclusion; the sidecar keeps the exact span.

## 3. Verification (`verify.py`, on the vault)

| Work | Letters | missing | rows | aligned_ok | content_ok | edition-variant rows | concordance: copy letters / matched / copy-only / target-only |
|---|---|---|---|---|---|---|---|
| `sa-root` | 2062 | 0 | 29 | — | — | — | — |
| `bo-display` | 2463 | 0 | 31 | 31/31 | 28/28 | 0 | 2062 / 2062 / 0 / 0 |
| `zh-translation` | 618 | 0 | 111 | 111/111 | 111/111 | 4 | 2424 / 2383 / 38 / 77 |
| `bo-vairocana-ngagsu-trelwa` | 8830 | 0 | 64 | 64/64 | 60/60 | 0 | 2453 / 2453 / 0 / 10 |
| `bo-vajrapani-dongyi-dronma` | 20529 | 0 | 81 | 81/81 | 53/53 | 0 | 2453 / 2453 / 0 / 10 |
| `bo-taranatha-tsikdrel` | 15877 | 0 | 80 | 79/79 | 61/61 | 0 | 2453 / 2453 / 0 / 10 |
| `bo-vimalamitra-tika` | 31434 | 0 | 62 | 62/62 | 55/55 | 0 | 2453 / 2453 / 0 / 10 |
| `bo-ngawang-nyima-drelwa` | 10780 | 0 | 54 | 54/54 | 42/42 | 0 | 2453 / 2453 / 0 / 10 |
| `bo-prasastrasena-tika` | 20235 | 0 | 70 | 70/70 | 57/57 | 0 | 2415 / 2415 / 0 / 48 |
| `bo-lobzang-gyaltsen-senge-nyinje` | 23369 | 0 | 50 | 50/50 | 28/28 | 0 | 2453 / 2453 / 0 / 10 |
| `bo-gendun-rinchen-migje` | 17861 | 0 | 62 | 62/62 | 37/37 | 0 | 2453 / 2453 / 0 / 10 |
| `bo-lama-kunga-shebum` | 25189 | 0 | 91 | 91/91 | 72/72 | 0 | 2453 / 2453 / 0 / 10 |

- *rows*: rows with letters in the source; equals the number of blocks (Tāranātha: 80 rows → 79 blocks, because row 85 was only a TOC label and became a heading).
- *aligned_ok*: every block's transclusions equal what its paired row gives (after the recorded corrections).
- *content_ok*: independently, each paired row's letters are found in the segments it transcludes.
- The ten "target-only" letters in each commentary copy are the display's `ཕྱིན་པ་` in ^9 and ^12, which all nine copies lack (Praśāstrasena's copy also lacks the title line: 48). They are recorded as variants on the rows concerned; no row after them shifted.

**Publication dry run** (copies, `translation-upload` linter + parser): segments / TOC nodes / alignments built for every file — sa 29/1/–, bo 31/1/28, zh 111/1/111, and for the commentaries the alignment count equals the transclusion count above. Linter errors: only `category_id`. Warnings: missing alt titles; English author names without an id.

## 4. Decisions recorded in the manifest

| Where | What | Who |
|---|---|---|
| Tibetan ↔ Sanskrit row 2 | Unpaired. Tibetan row 2 is the Sanskrit title (`རྒྱ་གར་སྐད་དུ། …`); the Sanskrit row it faced (`॥नमः सर्वज्ञाय॥`) is the opening invocation. | Claude, on your instruction |
| Tibetan row 5 ↔ Sanskrit row 2 | Paired: both are the opening homage — a functional, not literal, counterpart (the Bhagavatī Prajñāpāramitā / the Omniscient One). | Claude, on your instruction |
| Tibetan row 15 ↔ Sanskrit row 14 | Re-paired: `གཟུགས་ལས་སྟོང་པ་ཉིད་གཞན་མ་ཡིན། …` translates `रूपान्न पृथक् शून्यता …`. Sanskrit row 15 (`यद्रूपं सा शून्यता …`) has no counterpart in this Tibetan. | Claude, on your instruction |
| Vairocana row 83 | The lone `s` removed (stray keystroke opposite the root's colophon); the root colophon is now unaligned. | you |
| Display `ཕྱིན་པ་` (^9, ^12) | Display text kept; the commentary copies' missing `ཕྱིན་པ་` is a recorded variant. | you |

Every correction keeps the original human pairing/text in the sidecar.

## 5. Tables of contents

| Commentary | Source | Checkers | Reviewed flags (all checked line by line against the source) |
|---|---|---|---|
| Tāranātha | Your TOC doc: 23 labels, verbatim, in order | — | Flat: the doc's numbers are one running count (`༢༽`, `༼༡༽`…`༼༣༽`, `༤༽`…`༢༡༽`) and do not state the nesting. Labels inside rows were moved out into the headings (the author's words stay in the row). |
| Vairocana | none | — | Phase A found one candidate — the five excellences, a doctrinal list on the opening — and Phase B no division announcement. No outline is built from a doctrinal list. |
| Vajrapāṇi | tree, 4 nodes | 0 / 1 → accepted | Closing formula at line 97. **Scope:** the commentary announces one division (three samādhis, from row 39 on) and nothing after the third — its mantra, approval and colophon rows fall under heading 1.3. |
| Vimalamitra | tree, 9 nodes | 0 / 2 → accepted | The eight parts are announced once, in a verse; "question" and "answer" were placed at the passages they name (rows 14, 16). |
| Ngawang Nyima | tree, 17 nodes | 0 / 0 | — |
| Praśāstrasena | tree, 11 nodes | 0 / 0 | — |
| Lobsang Gyaltsen Sengge | tree, 29 nodes | 0 / 4 → accepted | Bare-ordinal openers; one row announcing a chain; three sections (teacher, place, retinue) opening inside one long row — their headings stand at the next row boundary. |
| Gendün Rinchen | tree, 34 nodes | 0 / 7 → accepted | Sections opening with a bare ordinal (`གཉིས་པ་ནི།`); titles only in the parents' enumerations. |
| Lama Kunga | tree, 71 nodes | 0 / 10 → accepted after 1 repair | Repair removed an announced-but-never-opened node (3.2.3.15.3 `དོན་བསྡུས་ཏེ་བསྟན་པ`). Remaining: row-level stacking, two false division-count flags (the text says `གཉིས་ཏེ`), and the author's own three-announced / two-opened division at 3.2.3.15. |

### 5a. The root's TOC (Sanskrit, Tibetan, Chinese)

No TOC for the root exists in the data (none in the new exports, none among the old Drive files). The outline used is Lobsang Gyaltsen Sengge's, measured against the alternatives by projecting each commentary's outline onto the 31 display segments:

| Outline | Covers title → colophon | Fit |
|---|---|---|
| **Lobsang Gyaltsen Sengge** (chosen) | yes: title ^2, translator's homage ^5, text ^6–^31, conclusion ^32 | 29 nodes; 25 land on distinct segments, in order |
| Ngawang Nyima | title and text; no homage or colophon node | 17 nodes |
| Gendün Rinchen | title and text; its conclusion node reaches no root segment | 34 nodes, deeper than the root |
| Praśāstrasena | from ^3; everything after ^24 falls under "dhāraṇī" | 11 nodes |
| Tāranātha | no title part (his ༡༽ label is missing) | flat |
| Vimalamitra | narrative parts only, no title or colophon | 9 nodes |

How it is carried: a heading stands before the first root segment its section comments on (through the commentary's own row alignment); the Sanskrit and the Chinese take it through their pairing with the Tibetan. A node that reaches no segment of a file gets no heading there — in the Tibetan: the teacher, place and retinue excellences (all inside ^7) and "the connection" before the form passage (1.3.2.2.1.1.1); the Sanskrit also lacks "title meaning" (it has no title rows of its own; `[विस्तरमातृका]` pairs with the Tibetan title line, section 0); the Chinese lacks "conclusion" (no colophon). Headings: Tibetan 25, Sanskrit 24, Chinese 24. Ids: `^0-1` for the title line, then `^1-1` … (the outline has one top node).

Trees: `2-RAILS/Sections/Raw/toc-tree/<id>.md` (with a `## Placement` table: the row each heading stands before, and the opening clause), evidence in `toc-candidates/`, `toc-enumerations/`, `toc-qc/` (each QC report ends with the review). The pre-TOC texts the pointers count are rebuilt by `build_sources.py … --stage pre-toc`; the build refuses a tree whose sha1 no longer matches.

## 6. Review items for you

1. **The root's TOC source** (§5a) — Lobsang Gyaltsen Sengge's outline, including his five-paths division of the answer (a Gelug reading). To use another commentary's outline, change `toc.source_work` for `sa-root`, `bo-display` and `zh-translation` in the manifest and rebuild; nothing else changes. Display segment ^12 holds the end of Śāriputra's question and the start of Avalokiteśvara's answer, so it sits under "question" in all three files; "answer" begins at ^13.
2. **Sanskrit pairing fixes** (§4) — rows 2, 5 and 15. Row 5 ↔ 2 is a functional pairing of two different homages; say if you prefer row 2 left unpaired.
3. **Vajrapāṇi's TOC scope** (§5) — its last section covers the mantra, approval and colophon by the text's own structure. Keep, or drop to `toc: none`.
4. **Lama Kunga 3.2.3.15** — the 15th topic announces three parts (line 137) but never opens the third ("summary"); possibly the advice at line 169 is meant. No heading invented.
5. **Tāranātha's TOC doc vs. the aligned commentary** — the doc has three of Tāranātha's own *sa bcad* sentences that the aligned rows lack (`གཉིས་པ་མདོ་སྡེ་ཆོས་འབྱུང་བའི་སྒོ་ནི།`, `དང་པོ་ལ་དྲིས་པ་དང་། ལན་བསྟན་པའོ།`, and two `དང་པོ་ནི།`). Not added: the commentary is the aligned doc. Labels `༡༽` and `༡༤༽` do not exist in the doc. A hierarchy can be added later if you want one; today it is flat.
6. **Chinese: 4 edition-variant rows** — rows 3 (`བྷ་ག་ཝ་ཏཱི…`, 79 % of letters in ^2), 65 (`དེ་བཞིན་དུ`, 84 %), 88 (`ཨོཾ` in the mantra, 89 %), 93 (the display's ^27 lacks `གཟིགས`, 90 %). Targets are right; the Tibetan editions differ.
7. **Rows spanning 2–3 display segments** — Vairocana 8, Vajrapāṇi 9, Tāranātha 8, Vimalamitra 10, Praśāstrasena 6 (^6+^7 — the display splits `འདི་སྐད་བདག་གིས་ཐོས་པ་དུས་གཅིག་ན།` from the setting) and 15 (^13+^15), Lobsang 11, 48, 50; Gendün 44, 47, 57; Lama Kunga 91, 92. Each transcludes all its segments.
8. **Human pairings kept as made** — e.g. Gendün's homage verses (row 1) face the sūtra's title row in the root copy, so they transclude the display title line (`^0-1`). Nothing was re-paired in the commentaries.
9. **`category_id`** is empty in every file — the library needs it before upload.
10. **Upload of the translations** — `translation-upload`'s script requires *identity* alignment (translation `^N` = root `^N`). That cannot hold here (translator-only rows, the corrected rows, files that each carry their own section ids, a 111-row Chinese against a 31-segment Tibetan); the parser builds the true pairs, the upload step needs to accept them.
11. **Library TOC depth** — the parser builds the TOC from Markdown heading levels (max 6), so Gendün's and Lama Kunga's levels 7–8 appear at level 6 there; the full path is in each heading id.

## 7. Not ingested

| Raw file | Why |
|---|---|
| `sherab-comm-1(toc).md` | No headings (colour-coded *sa bcad*, if any, is lost in a Markdown export); a slightly different edit of the commentary (11 spelling differences) carrying the old 80-segment alignment numbers and bold lemmas. Vairocana's TOC question was settled by `toc-generate`. |
| `sherab-comm-2(toc).md` | No headings; the same text as the commentary plus the author line. Vajrapāṇi's TOC came from `toc-generate`. |

Every other raw file is a work's `text`, a `pair` side or its `meta` sheet (listed with its sha1 in each file's `raw_sources`).

## 8. Rebuild

```bash
python3 4-SYSTEM/Skills/aligned-corpus-intake/scripts/build_sources.py 0-INBOX/raw-data/intake-manifest.yaml
python3 4-SYSTEM/Skills/aligned-corpus-intake/scripts/verify.py 0-INBOX/raw-data/intake-manifest.yaml
```

Build and verify JSON for this run: `0-INBOX/temp/intake-build-report.json`, `0-INBOX/temp/intake-verify.json`. Once anything in `2-RAILS/` cites these block ids, re-segmenting is a migration (annex §2 log).


---

## 9. Addendum 2026-10-04 — three translations from the OpenPecha API

**What was added.** Three human translations of the Tibetan, each aligned by transclusion to `1-SOURCES/Translations/bo-prajnaparamita-hrdaya.md`:

| File | OpenPecha text / instance | Language (lang_tag) | Licence | Blocks | Headings | Transclusions |
|---|---|---|---|---|---|---|
| `1-SOURCES/Translations/en-prajnaparamita-hrdaya.md` | `MrsRfx7ML8QZxQPnhGesn` / `1EENMb457ICcq3d2DwQBs` (lotsawahouse.org) | English (`en`) | `cc-by-nc` | 25 | 2 + title | 31 |
| `1-SOURCES/Translations/tib-prajnaparamita-hrdaya.md` | `ysb3nzBwYpMPcS9Jm064y` / `88UIsXzJTkawquPqwKgBu` (openpecha.org) | Tibetan, colloquial (`tib`) | `public` (Public Domain Mark) | 25 | 2 + title | 31 |
| `1-SOURCES/Translations/tibphono-prajnaparamita-hrdaya.md` | `8LbtYe5XRXQODfqkBkKJy` / `rj2dtxUr9tSKn7P6qfL0g` (www.openpecha.org) | Tibetan phonetics (`tibphono`) | `public` (Public Domain Mark) | 25 | 2 + title | 31 |

Sidecars: `1-SOURCES/Annotations/{en,tib,tibphono}-prajnaparamita-hrdaya.annotations.json` (each block's OpenPecha segment id and span, the old-Tibetan span it is aligned to, the letters it covers in each display block, the merged segments).

**Raw data.** `0-INBOX/raw-data/openpecha-api/`: the three texts and their parent `BdfDD44nDSOqa13HgTvd7` (instance `FsrpfLxgRL9UniIrc7c5o`, 27 segments), fetched 2026-10-04 from `https://api-aq25662yyq-uc.a.run.app` as received (31 files; `tree.json` and `manifest.json` are indexes written by the download). Every API file is content-identical to the 2026-10-02 download of the same texts (in git history).

**How the alignment was made.** Each translation segment is aligned upstream, one to one, to an old-Tibetan segment (27 ↔ 27). That old Tibetan is letter-identical to the display Tibetan (2,463 of 2,463 letters matched; the display's extra 179 letters are the translators' colophon added from Wikisource), so each segment transcludes the display blocks its counterpart's letters fall in. Mapping (identical for all three files): 0-1→0-1, 1-1→1-1+1-2, 1-2→1-3, 1-3→1-4, 1-4→1-5+1-6, 1-5→1-7, 1-6→1-8+1-9, 2-1→2-1, 2-2→2-2, 2-3→2-3+2-4, 2-4→2-5, 2-5→2-6, 2-6→2-7, 2-7→2-8, 2-8→2-9, 2-9→2-10+2-11, 2-10→2-12, 2-11→2-13, 2-12→2-14, 2-13→2-15, 2-14→2-16, 2-15→2-17+2-18, 2-16→2-19, 2-17→2-20, 2-18→2-21. Each file covers 31 of the 32 display blocks; the only one unaligned is `^3-1`, the translators' colophon (none of the three has it).

**Decisions** (in the manifest, `decided_by: Claude (instructed by vault owner 2026-10-04)`):
- D2 — carried onto the display Tibetan by letters, no segmentation changed.
- D9 — in each file segments 9+10 fall inside display `^2-2` and segments 16+17 inside `^2-9`; each pair is merged (joined with a space) so no display block is transcluded twice in a row: 27 segments → 25 blocks.
- D5 — headings from the root's Wikisource outline (labels added to `2-RAILS/Sections/Raw/toc-wikisource/prajnaparamita-hrdaya.md`): English *The Setting of the Sūtra* / *The Main Body of the Sūtra* (/ *Translators' Colophon*, not shown); colloquial Tibetan: the Tibetan headings verbatim (same language and script, no human colloquial rendering exists); phonetics: *do i lengzhi* / *do dön ngö* (/ *jukjang*), transcribed in the text's own phonetic spelling. Sections open at segments 2 and 8, where they open in the Tibetan; no split needed (D7).
- D10 — no brackets in any of the three texts.

**Tooling change** (`aligned-corpus-intake`, vault copy): `md_export.read_source_rows` reads `openpecha:<text_id>` (row k = segment k) and `openpecha:<text_id>#parent` (row k = the parent span the upstream alignment pairs with segment k) as md_rows row sources, used by `md_adapter` and `verify.py`; `build_sources.py --write-only <keys>` writes only the listed works. Existing works build byte-identically (bodies and sidecars checked against the vault before writing).

**Review items for you**
1. **Language codes.** The WeBuddhist library (`GET https://library.webuddhist.com/v2/languages`, 2026-10-04) accepts bo, en, fr, hi, i9 (a probe entry), ja, lzh, mn, mr, ne, pi, ru, sa, th, vi, zh — **not `tib` or `tibphono`**. The two files carry OpenPecha's codes and cannot be uploaded until a code is chosen or added. (`references/pecha-conventions.md` says such a text is "reported, not built"; built here on your instruction.) `About Sources.md` §12 has no tag for either.
2. **Headings** — check the English renderings and the phonetic transcriptions (`do i lengzhi`, `do dön ngö`, `jukjang`) and the choice of verbatim Tibetan for the colloquial file.
3. **D9 merges** — in each of the three files, block `^2-2` (segments 9+10, transcludes Tibetan `^2-2`) and block `^2-8` (segments 16+17, transcludes Tibetan `^2-9`).
4. **Phonetics defects upstream**, reproduced verbatim: syllables with diacritic letters are missing (e.g. `^2-2` " i bu" for Śāriputra, the mantra `^2-12` "   ga té ga té  ra ga té …", `^1-1` "gawa ti dra  ra mi  hré ya"); its last segment's span ends one character past the content.
5. **English translator** — the Lotsawa House page credits "Adam Pearcey, 2019" (CC BY-NC 4.0); the OpenPecha record has no contributor, so the frontmatter has no `translator`.
6. **Upload** — like the Chinese, these files do not have identity alignment (translation `^N` ≠ Tibetan `^N`), which `translation-upload` requires (item 10 above).
7. **Tibetan `related_translations`** does not list the three files (the Tibetan file was deliberately not rewritten); the next full rebuild adds them.
8. **Manifest vs vault** — six commentaries in the vault have `category_id: null` while the manifest has `uGpinx0GZlvU1uw44RyYS` (Vairocana, Vajrapāṇi, Ngawang Nyima, Lobzang Gyaltsen Senge, Gendün Rinchen, Lama Kunga); a full rebuild would write the manifest value.

**Verifier output** (on the vault, 2026-10-04):

```
OK  sa-root                          blocks=   29 headings=  3 transclusions=    0 letters=   2062 missing=0 extra=0 rows=29
OK  bo-display                       blocks=   32 headings=  4 transclusions=   28 letters=   2642 missing=0 extra=0 rows=32 aligned_ok=32/32 content_ok=28/28
OK  zh-translation                   blocks=   30 headings=  3 transclusions=   30 letters=    618 missing=0 extra=0 rows=111 aligned_ok=30/30 content_ok=30/30 edition_variant_rows=2
OK  bo-vairocana-ngagsu-trelwa       blocks=   64 headings=  1 transclusions=   61 letters=   8830 missing=0 extra=0 rows=64 aligned_ok=64/64 content_ok=60/60
OK  bo-vajrapani-dongyi-dronma       blocks=   81 headings=  5 transclusions=   54 letters=  20529 missing=0 extra=0 rows=81 aligned_ok=81/81 content_ok=53/53
OK  bo-taranatha-tsikdrel            blocks=   79 headings= 24 transclusions=   62 letters=  15877 missing=0 extra=0 rows=80 aligned_ok=79/79 content_ok=61/61
OK  bo-vimalamitra-tika              blocks=   65 headings=  9 transclusions=   56 letters=  31434 missing=0 extra=0 rows=62 aligned_ok=65/65 content_ok=55/55
OK  bo-ngawang-nyima-drelwa          blocks=   54 headings= 18 transclusions=   42 letters=  10780 missing=0 extra=0 rows=54 aligned_ok=54/54 content_ok=42/42
OK  bo-prasastrasena-tika            blocks=   70 headings= 12 transclusions=   59 letters=  20235 missing=0 extra=0 rows=70 aligned_ok=70/70 content_ok=57/57
OK  bo-lobzang-gyaltsen-senge-nyinje blocks=   50 headings= 30 transclusions=   32 letters=  23369 missing=0 extra=0 rows=50 aligned_ok=50/50 content_ok=28/28
OK  bo-gendun-rinchen-migje          blocks=   62 headings= 35 transclusions=   40 letters=  17861 missing=0 extra=0 rows=62 aligned_ok=62/62 content_ok=37/37
OK  bo-lama-kunga-shebum             blocks=   91 headings= 72 transclusions=   74 letters=  25189 missing=0 extra=0 rows=91 aligned_ok=91/91 content_ok=72/72
OK  en-translation-lotsawahouse      blocks=   25 headings=  3 transclusions=   31 letters=   3113 missing=0 extra=0 rows=27 aligned_ok=25/25 content_ok=25/25
OK  tib-translation-colloquial       blocks=   25 headings=  3 transclusions=   31 letters=   2368 missing=0 extra=0 rows=27 aligned_ok=25/25 content_ok=25/25
OK  tibphono-translation             blocks=   25 headings=  3 transclusions=   31 letters=   2558 missing=0 extra=0 rows=27 aligned_ok=25/25 content_ok=25/25
```
