# Heart Sūtra — intake report (2026-10-03)

Skill: `aligned-corpus-intake`, Route B (`md_rows`). Manifest: `0-INBOX/raw-data/intake-manifest.yaml`. How-to for other texts: `4-SYSTEM/How-to guides/Ingest a row-aligned corpus.md`.

**Result:** 12 files in `1-SOURCES/` (1 root, 2 translations, 9 commentaries) plus one sidecar each in `1-SOURCES/Annotations/`. `verify.py` on the vault: **OK for all 12, no source letter missing, every row exactly one block, every transclusion equal to the human row pairing.** Publication dry run (linter + parser on copies): the only error is the empty `category_id` (left for you); text, edition, TOC and alignment payloads build for every file.

---

## 1. The design, in brief

- **One stored segmentation per text.** The Tibetan "display" doc (32 rows) is the Tibetan the library stores. Each commentary was aligned against its own cut of the root (`sherab-root-N`); the Chinese against another cut and edition (`sherab-root-bo(bo-zh)`). Those cuts are mapped onto the display segments by letters (`concordance.py`): no segmentation was changed — not the display's, not a commentary's, not the Chinese.
- **Directions** (your decision): Sanskrit = root; Tibetan = its translation; the Chinese and every commentary point at the Tibetan.
- **TOC first, then ids, then transclusions** (your decision). Commentary ids come from the sections (`^<top-level>-<n>`); headings carry their full path (`^2-2-3-0`). Texts with no TOC (Sanskrit, Tibetan, Chinese) keep the alignment doc's row number as the id (`^N`), so Tibetan `^N` and Sanskrit `^N` are the two halves of row N.
- Registered in the annex: commentary ids, the `Annotations/` folder, three id-scheme deviations.

## 2. What was built

| Work | File | Blocks | Headings | Transclusions | Unaligned blocks | Spanning 2–3 segments | Target rows with no counterpart | TOC |
|---|---|---|---|---|---|---|---|---|
| `sa-root` | `1-SOURCES/Text/sa-prajnaparamita-hrdaya.md` | 29 | 0 | 0 | — | — | — | — |
| `bo-display` | `1-SOURCES/Translations/bo-prajnaparamita-hrdaya.md` | 31 | 0 | 28 | 3 | 0 | 1 | — |
| `zh-translation` | `1-SOURCES/Translations/zh-prajnaparamita-hrdaya.md` | 111 | 0 | 111 | 0 | 0 | 0 | — |
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

Trees: `2-RAILS/Sections/Raw/toc-tree/<id>.md` (with a `## Placement` table: the row each heading stands before, and the opening clause), evidence in `toc-candidates/`, `toc-enumerations/`, `toc-qc/` (each QC report ends with the review). The pre-TOC texts the pointers count are rebuilt by `build_sources.py … --stage pre-toc`; the build refuses a tree whose sha1 no longer matches.

## 6. Review items for you

1. **Sanskrit pairing fixes** (§4) — rows 2, 5 and 15. Row 5 ↔ 2 is a functional pairing of two different homages; say if you prefer row 2 left unpaired.
2. **Vajrapāṇi's TOC scope** (§5) — its last section covers the mantra, approval and colophon by the text's own structure. Keep, or drop to `toc: none`.
3. **Lama Kunga 3.2.3.15** — the 15th topic announces three parts (line 137) but never opens the third ("summary"); possibly the advice at line 169 is meant. No heading invented.
4. **Tāranātha's TOC doc vs. the aligned commentary** — the doc has three of Tāranātha's own *sa bcad* sentences that the aligned rows lack (`གཉིས་པ་མདོ་སྡེ་ཆོས་འབྱུང་བའི་སྒོ་ནི།`, `དང་པོ་ལ་དྲིས་པ་དང་། ལན་བསྟན་པའོ།`, and two `དང་པོ་ནི།`). Not added: the commentary is the aligned doc. Labels `༡༽` and `༡༤༽` do not exist in the doc. A hierarchy can be added later if you want one; today it is flat.
5. **Chinese: 4 edition-variant rows** — rows 3 (`བྷ་ག་ཝ་ཏཱི…`, 79 % of letters in ^2), 65 (`དེ་བཞིན་དུ`, 84 %), 88 (`ཨོཾ` in the mantra, 89 %), 93 (the display's ^27 lacks `གཟིགས`, 90 %). Targets are right; the Tibetan editions differ.
6. **Rows spanning 2–3 display segments** — Vairocana 8, Vajrapāṇi 9, Tāranātha 8, Vimalamitra 10, Praśāstrasena 6 (^6+^7 — the display splits `འདི་སྐད་བདག་གིས་ཐོས་པ་དུས་གཅིག་ན།` from the setting) and 15 (^13+^15), Lobsang 11, 48, 50; Gendün 44, 47, 57; Lama Kunga 91, 92. Each transcludes all its segments.
7. **Human pairings kept as made** — e.g. Gendün's homage verses (row 1) face the sūtra's title row in the root copy, so they transclude ^1. Nothing was re-paired in the commentaries.
8. **`category_id`** is empty in every file — the library needs it before upload.
9. **Upload of the translations** — `translation-upload`'s script requires *identity* alignment (translation `^N` = root `^N`). That cannot hold here (translator-only rows ^2–^4, the corrected rows, a 111-row Chinese against a 32-row Tibetan); the parser builds the true pairs, the upload step needs to accept them.
10. **Library TOC depth** — the parser builds the TOC from Markdown heading levels (max 6), so Gendün's and Lama Kunga's levels 7–8 appear at level 6 there; the full path is in each heading id.

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
