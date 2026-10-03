# TOC tree vs. source QC report

issues: 4

## Issues

- 1.3.2.2.1.1.2 གཉིས་པ་གཟུགས་ཕུང་གི་རང་བཞིན་ལ་ཇི་ལྟར་སློ: title attested in the source but not near pointer [[39]] (found near line 35) — possible cursor loss
- 1.3.2.4 བཞི་པ་འཁོར་རྣམས་དགའ་ནས་འཛིན་པར་དམ་བཅས་པ་: title attested in the source but not near pointer [[93]] (found near line 27) — possible cursor loss
- pointer [[15]] is shared by 3 nodes (1.3, 1.3.1, 1.3.1.1) — repeated-pointer collision, the extractor likely lost its cursor partway through this run
- pointer [[19]] is shared by 4 nodes (1.3.1.1.2, 1.3.1.1.3, 1.3.1.1.4, 1.3.1.2) — repeated-pointer collision, the extractor likely lost its cursor partway through this run

## Notes (not counted as issues)

- (none)

## Reviewed — accepted (orchestrator, 2026-10-03)

Checked against `0-INBOX/temp/TOC-lobzang-gyaltsen-senge-nyinje/source.md`:

1. **1.3.2.2.1.1.2 at [[39]]** and **1.3.2.4 at [[93]]** — the sections open on rows that are only a bare ordinal (`གཉིས་པ་ནི།`, `བཞི་པ་ནི་`); the full titles stand in the parents' enumerations (lines 35 and 27). Pointers correct.
2. **[[15]] shared by 1.3, 1.3.1, 1.3.1.1** — one row states the whole chain (གསུམ་པ་གཞུང་གི་དོན་ལ་གཉིས། … དང་པོ་ལ་གླེང་གཞི་ཐུན་མོང་བ་དང་ཐུན་མོང་མ་ཡིན་གཉིས། … དང་པོ་ལ་བཞི། …): stacked headings, correct.
3. **[[19]] shared by 1.3.1.1.2, 1.3.1.1.3, 1.3.1.1.4, 1.3.1.2** — the teacher, place and retinue excellences all open *inside* the single row at line 17 (character offsets 1994, 3154 and 3630 of 4783); line 19 is the row `གཉིས་པ་ཐུན་མོང་མ་ཡིན་པའི་གླེང་གཞི་ནི།`. Rows are indivisible alignment units, so those three headings stand at the next row boundary, stacked before line 19, with no block of their own; their true positions are kept in the placement TSV and the sidecar. Putting them before line 17 would put them ahead of the time excellence's text.

issues_after_review: 0
