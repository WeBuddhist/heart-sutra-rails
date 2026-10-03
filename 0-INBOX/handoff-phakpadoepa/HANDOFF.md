# HANDOFF — build this vault's sources from the Dzongsar exports

**For:** the Claude Code agent working in this repo (a Railroads vault made from `rails-template`).
**From:** the agent that built `heart-sutra-rails` on 2026-10-03, with every decision its vault owner made along the way.
**Goal:** turn the vault owner's folder of Dzongsar exports into finished `1-SOURCES/` files, with the same result as Heart Sūtra: the root text, its translations and its commentaries, each segmented by the human alignment rows, carrying a table of contents and TOC-driven block ids, with every alignment written as a transclusion, a no-loss verifier passing, and a review brief for the text expert.

Read this file to the end before touching anything. Then follow it without asking for each step. The vault owner has already decided everything in §3. Stop only for the cases in §4, and when you do, ask all your questions in one message.

---

## 1. What you are given

| Item | Where | What it is |
|---|---|---|
| This bundle | wherever the vault owner put `handoff-phakpadoepa/` (this file's folder) | `skills/` holds two skills `rails-template` lacks: `aligned-corpus-intake` and `wiki-toc-import`, with today's features. `commands/` holds their slash-command files. `example-heart-sutra/` holds the finished Heart Sūtra manifest, its two Wikisource outline files and its vault annex: a worked example of every field below. |
| The raw data | the vault owner's folder (ask for its path if it is not obvious) | Dzongsar Google Docs exported as **Markdown** (numbered lists, row N of one doc paired with row N of the other) and metadata sheets as **CSV**. Format: `skills/aligned-corpus-intake/references/md-export-format.md`. |
| The text sheet | a `.csv` in that folder | One row per text. Its Tibetan headers mean: ཨང་། number · གཞུང་མཚན། title · མཛད་པ་པོ། author · ཡིག་རྐྱང། plain-text name · ལས་ཀའི་གནས་བབ། status · **Wikisource Link** (the `Index:… .pdf` page, **the TOC source**) · ཡིག་རྐྱང་རྩོམ་སྒྲིག་མཁན། text editor · Transclusion Page Link (not used) · ལེགས་བཅོས་ཟིན་པ། proofread · Wikipedia link (not used) · status. Rows can be shifted: Heart Sūtra's sheet had a row with no number, so every later cell moved one column. Identify each column by its content (an `Index:` URL, a `wikisource.org/wiki/` URL, a `wikipedia.org` URL), not by position. |

---

## 2. Install the skills

1. Copy `skills/aligned-corpus-intake/` and `skills/wiki-toc-import/` into `4-SYSTEM/Skills/`, and `commands/*.md` into `.claude/commands/`.
   - If a folder of the same name already exists and differs, stop and ask: the bundle's copy has features the build needs (`toc.kind: outline`, `row_splits`, `supplement_rows`, `merge_rows`).
2. Register both skills, as `create-skill` requires:
   - append `skills/catalog-entries.md` to `4-SYSTEM/Skills/SKILLS-CATALOG.md` (intake under "Intake", wiki-toc-import under "Structure and table of contents");
   - add these rows to the §12 table of `4-SYSTEM/CLAUDE.md`:
     - `| Ingest a human-aligned corpus (OpenPecha API, Dzongsar docx/Markdown alignments) | aligned-corpus-intake |`
     - `| Apply a TOC taken from the text's Wikisource Index page (or Wikipedia) | wiki-toc-import |`
3. Check that `4-SYSTEM/Skills/toc-generate/scripts/toc_tree_ingest.py` exists. The intake build imports it, and it ships with `rails-template`.
4. Read both `SKILL.md` files in full: `aligned-corpus-intake` (Route B, `md_rows`) and `wiki-toc-import`. They are the procedure. This file adds the decisions and the order.

Python needs `pyyaml`. Run every script from the vault root.

---

## 3. Standing decisions — apply them, do not ask

The Heart Sūtra vault owner made these on 2026-10-03, some after trying the alternative. Apply them here by default. Wherever a manifest entry needs `decided_by`, write `vault owner — standing decision carried over from heart-sutra-rails (2026-10-03)`, plus the specifics.

| # | Decision | How it is written |
|---|---|---|
| D1 | **Direction.** The source-language text is the root: Sanskrit if present, else the Tibetan. The Tibetan is its translation. Everything the humans aligned to the Tibetan (Chinese or other translations, every commentary) points at the Tibetan: `root_text:`, `target:` and every transclusion. Nothing is re-pointed to the Sanskrit. | manifest `target:` |
| D2 | **One segmentation per text.** Each text is stored once, cut as its display doc cuts it. Every other cut of it (each commentary's own copy of the root, the Tibetan side of the Tibetan–Chinese pair) is carried onto that cut by letters. The build's concordance does this; never re-segment by hand. | `pair.own_side` / `pair.target_side` |
| D3 | **TOC before ids; ids from the TOC.** Headings `^<decimal path>-0` (full path, no cap; depth ≥ 6 bolded). Body blocks `^<top-level section>-<n>`, counting through deeper headings. Blocks before the first heading are `^0-<n>`, with no invented `## 0` heading. | `id_scheme: h2` |
| D4 | **Root and translation TOC = the text's Wikisource Index page.** Use the sheet's "Wikisource Link" (`Index:… .pdf`), **not** the Wikipedia article (a summary *about* the text) and **not** the transclusion page. Use the headings exactly where the Index's proofread pages place them. | `toc: {kind: outline, file: 2-RAILS/Sections/Raw/toc-wikisource/<id>.md}` on the root and every translation |
| D5 | **Headings in each file's own language.** The Tibetan headings are verbatim from Wikisource (numbers dropped). A Sanskrit, Chinese or other file gets editorial translations that use that text's own vocabulary. Never put Tibetan headings in a non-Tibetan file. | `labels: {bo, sa, zh, …}` per outline node |
| D6 | **Commentary TOC, in order of preference:** (a) its own Wikisource Index page, if the sheet has one and the commentary is in the raw data; (b) the Dzongsar TOC doc's labels (`toc.kind: labels`); (c) a `toc-generate` tree (`toc.kind: tree`); (d) none, with the reason, when the commentary announces no divisions. | manifest `toc:` |
| D7 | **A heading that falls inside an alignment row: split the row** there, at the exact Wikisource position. Each root segment the row transcluded is shown once, with the first part that comments on it. | `row_splits: [{row, at: [clause…], targets: [[i…]…], reason, decided_by, date}]`; outline `start_row: "N.k"` |
| D8 | **A TOC section whose text the corpus lacks** (Heart Sūtra: the translators' colophon) **is added** verbatim from the Wikisource proofread page, with page, revision and edition recorded. | `supplement_rows: [{row: <after last raw row>, text, source, edition, reason, decided_by, date}]` |
| D9 | **A translation cut much finer than the Tibetan** (so the same Tibetan segment is transcluded several times in a row) **is merged to one block per Tibetan segment.** The joiner is a space for Chinese (its own phrase separator) and whatever is natural for other languages. Only rows with exactly the same targets merge. | `merge_rows: {mode: by_target, joiner: ' ', reason, decided_by, date}` |
| D10 | **Square brackets in a source text** (an edition's editor-supplied words, which Obsidian renders like links) **are removed and the words kept.** | `text_corrections: [{row, find: '[…]', replace: '…', reason, decided_by, date}]` |
| D11 | **Commentaries in the sheet but not in the raw data are skipped** and reported. Never ingest a text here that has no raw export. | intake report |
| D12 | **Root ↔ translation pairing.** Read every short pair in full. Re-pair a row only where it is clearly wrong (a title line paired with an invocation, an off-by-one), with the reason. Mark these as Claude's for the expert to check. | `pair_corrections` with `decided_by: Claude (standing instruction "read it and fix if it really makes sense")` |
| D13 | **Never edit `1-SOURCES/` by hand.** Every change goes through the manifest or an outline file, followed by a rebuild. The build regenerates ids and every transclusion together. | — |

---

## 4. Stop and ask only when

- The raw data does not fit the shape in §1: no display doc for the root, a pair whose two files have different row counts, an unknown document kind.
- A text in the raw data has no row in the sheet, or two rows could be it.
- A Wikisource Index page has no inline headings, or a heading's text cannot be found in our rows (`UNMATCHED`) for a reason other than D8.
- A `1-SOURCES/` file already exists, or anything in `2-RAILS/` or `3-TRANSFORMATIONS/` cites one. A rebuild then changes cited ids, so it is a migration.
- Any file carries `protected: true` (CLAUDE.md: confirm before touching).

Everything else, decide by §3 and record it.

---

## 5. Procedure

Work in this order. Use Sonnet subagents in parallel for the independent judgement steps marked ∥, and spot-check their output yourself.

1. **Copy the raw data** into `0-INBOX/raw-data/`, unchanged. Never modify a raw file afterwards.
2. **Inventory.** List every file and run `python3 4-SYSTEM/Skills/aligned-corpus-intake/scripts/md_export.py <file>` on each, which lists rows (`--meta` for a CSV). Map every file to a work: the root display doc, each translation pair, each commentary pair (`…(root-com).md` style: the commentary and its own copy of the root, row for row), each TOC doc, each metadata CSV. Check that each pair has equal row counts and lines up at its start, middle and end. Match every work to its sheet row by title **and** author (D11).
3. **Read every short pair in full** (root ↔ each translation) and write any `pair_corrections` (D12). ∥ one subagent per pair.
4. **Write the manifest** `0-INBOX/raw-data/intake-manifest.yaml` in dependency order: root, its translations, then everything aligned to the Tibetan. Copy the shape of `example-heart-sutra/intake-manifest.yaml`. Frontmatter comes from the metadata CSVs, and `category_id` stays empty. **Quote every YAML value that contains a colon** (a `reason:` with a colon breaks the build).
5. **Register** every commentary's `registered_id`, and `1-SOURCES/Annotations/` as a typed folder, in `4-SYSTEM/Guidelines/vault-annex.md`, filling the annex placeholders (shape: `example-heart-sutra/vault-annex.md`).
6. **TOCs** (D4–D8):
   1. For the root, and for each commentary that has a Wikisource Index page:
      `python3 4-SYSTEM/Skills/wiki-toc-import/scripts/fetch_wiki_outline.py wikisource "<Index:… .pdf or its URL>" --id <outline-id> --placed-on <work key>`
      Place the root's outline on the stored Tibetan, and a commentary's on the commentary itself. The script pins revisions, finds each heading in our rows by letters, and marks `MID` nodes with a suggested `row_splits` entry. Apply D7 to `MID` nodes and D8 to `UNMATCHED` ones. Spot-check each start row with `grep -m1 "^N\. " <raw file>`. Wikisource rate-limits: the script waits and retries; do not run several fetches at once.
   2. ∥ One subagent per translation language: render the root's headings (D5), preferring words the translation itself uses, and cite its rows.
   3. Write each outline to `2-RAILS/Sections/Raw/toc-wikisource/<id>.md` (shape: the two example outline files, `status: complete`). Set `toc: {kind: outline, file: …, note: …}` on the root, each translation and each such commentary, and add any `row_splits` / `supplement_rows`.
   4. Other commentaries: use `labels` from a TOC doc, or run `toc-generate` exactly as Route B step 6 says (`--stage pre-toc`, Phases 0–C, placement, QC, `toc_rows.py promote`). ∥ the Phase A/B chunk scans per commentary. If no division is announced, use `kind: none` with the reason.
7. **Test build and verify** into a scratch folder:
   `python3 4-SYSTEM/Skills/aligned-corpus-intake/scripts/build_sources.py 0-INBOX/raw-data/intake-manifest.yaml --out <scratch> --report <scratch>/report.json`
   `python3 4-SYSTEM/Skills/aligned-corpus-intake/scripts/verify.py 0-INBOX/raw-data/intake-manifest.yaml --root <scratch>`
   Fix the manifest, never the output, until every work prints `OK … missing=0`, `aligned_ok n/n`, `content_ok n/n`.
8. **Look at the result, not just the numbers.** In the scratch copy:
   - read each file's headings and check that the translations break at the same passages as the Tibetan;
   - check that no non-Tibetan file has a Tibetan heading;
   - check that `[`…`]` appears nowhere in body text (D10);
   - count how often each Tibetan segment is transcluded in a row by each translation, and merge any translation that repeats them (D9).
9. **Build into the vault** (the same commands without `--out` / `--root`) and verify again.
10. **Coverage check.** For each commentary, list the Tibetan root segments it never transcludes, leaving out the title, homage and colophons:
    ```python
    import re, glob
    bo = open("<the Tibetan root file>").read()
    ids = [m.group(2) for l in bo.splitlines() if not l.startswith("#")
           for m in [re.match(r"(.*\S)\s+\^([0-9-]+)$", l)] if m]
    for f in sorted(glob.glob("1-SOURCES/Commentaries/*.md")):
        got = set(re.findall(r"<tibetan root file name>#\^([0-9-]+)\]\]", open(f).read()))
        print(f, [i for i in ids if i not in got])
    ```
    For each gap, read the commentary's rows around it. If the commentary is silent there (Heart Sūtra: Vimalamitra keeps the mantra secret), the gap is a review item only. If its comment sits in a neighbouring row and the human pairing slipped, it is a review item for the expert, not a fix you make.
11. **Independent review** by a fresh subagent, read-only: section starts across languages, the id sequence, each commentary's headings against its transclusions, leftover granular headings.

---

## 6. Deliverables

1. `1-SOURCES/` files and `1-SOURCES/Annotations/*.annotations.json`, built by the skill, with the verifier passing on the vault.
2. `0-INBOX/raw-data/intake-manifest.yaml`: every decision, with its reason, who decided and the date.
3. `2-RAILS/Sections/Raw/toc-wikisource/*.md` (and `toc-tree/` for generated trees).
4. The vault annex filled in: the text, the addressing scheme, the registered ids, the TOC source per file, every registered deviation (D4/D5 for the root, D7 splits, D8 added text) and the id log.
5. `0-INBOX/<corpus>-intake-report.md`: a works table, review items, what was not ingested and why, and the verifier output.
6. **A review brief for the text expert:** a Claude Docs doc if this environment has the Docs connector, otherwise `0-INBOX/review-brief.md`. Use the same five sections as Heart Sūtra's:
   - **At a glance:** a table per file with role, blocks, headings and their source, and transclusions.
   - **Checked automatically:** what the verifier proves.
   - **Review checklist:** `- [ ]` items, most important first. Cover the TOC placement, the translated headings, added text, Claude's pair corrections, splits, merges, bracket removals, coverage gaps and deep machine-built TOCs, each with file and block ids.
   - **Root passages some commentaries never transclude:** segment, passage and commentaries.
   - **Where to look:** paths.
7. A final message to the vault owner: what was built, the counts, the review items, and anything skipped.

Commit only if the vault owner asks.

---

## 7. Things that went wrong in Heart Sūtra, so they need not here

- **The wrong TOC page.** The sheet's Wikipedia link is an article *about* the text, with its own summary sections. The text's TOC is on the Wikisource Index page. It cost a full rebuild.
- **A commentary's *sa bcad* projected onto the root** gave an 8-level TOC for a one-page sūtra and Tibetan headings in the Sanskrit and Chinese. Do not use `toc.kind: projected` for a root when a Wikisource TOC exists.
- **Unquoted YAML** with a colon in a `reason:` stopped the build. Nothing was written, but the error is easy to miss in a long command.
- **Wikisource returns HTTP 429** under quick successive calls. The fetch script backs off; make one fetch at a time.
- **A merged translation changes its ids.** Do the merge before anything cites the file.
- **`git mv -k`** silently skips untracked files. Use plain `mv` for new folders.
