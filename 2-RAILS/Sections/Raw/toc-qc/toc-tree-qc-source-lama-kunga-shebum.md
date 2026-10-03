# TOC tree vs. source QC report

issues: 10

## Issues

- pointer [[3]] is shared by 4 nodes (1, 1.1, 1.2, 1.3) — repeated-pointer collision, the extractor likely lost its cursor partway through this run
- pointer [[5]] is shared by 6 nodes (1.4, 2, 3, 3.1, 3.1.1, 3.1.2) — repeated-pointer collision, the extractor likely lost its cursor partway through this run
- pointer [[19]] is shared by 3 nodes (3.2.1.2, 3.2.1.2.1, 3.2.1.2.2) — repeated-pointer collision, the extractor likely lost its cursor partway through this run
- pointer [[21]] is shared by 4 nodes (3.2.1.2.2.1, 3.2.1.2.2.1.1, 3.2.1.2.2.1.1.1, 3.2.1.2.2.1.1.2) — repeated-pointer collision, the extractor likely lost its cursor partway through this run
- pointer [[23]] is shared by 4 nodes (3.2.1.2.2.1.1.3, 3.2.1.2.2.1.1.4, 3.2.1.2.2.1.2, 3.2.1.2.2.1.2.1) — repeated-pointer collision, the extractor likely lost its cursor partway through this run
- pointer [[27]] is shared by 3 nodes (3.2.1.2.2.3, 3.2.1.2.2.3.1, 3.2.1.2.2.3.1.1) — repeated-pointer collision, the extractor likely lost its cursor partway through this run
- pointer [[33]] is shared by 3 nodes (3.2.1.2.2.3.2, 3.2.1.2.2.3.2.1, 3.2.1.2.2.3.2.2) — repeated-pointer collision, the extractor likely lost its cursor partway through this run
- 3.2.1.2 'གཉིས་པ་ཐུན་མོ་མ་པའི་གླེང་གཞི་': announcing text names a 3, 4-way division but the tree gives it 2 child(ren) — verify by hand which is right
- 3.2.1.2.2.3 'གསུམ་པ་ཆོས་སྣང་བའི་ཆོ་འཕྲུལ་བས': announcing text names a 3-way division but the tree gives it 2 child(ren) — verify by hand which is right
- 3.2.3.15 'བཅོ་ལྔ་པ་གསང་སྔགས་ཀྱི་ཐེག་པ་ཀུ': announcing text names a 3-way division but the tree gives it 2 child(ren) — verify by hand which is right

## Notes (not counted as issues)

- (none)

## Reviewed — accepted after one repair round (orchestrator, 2026-10-03)

Repair round 1 (isolated subagent, `pass4-qc-repair.md`) removed `3.2.3.15.3 དོན་བསྡུས་ཏེ་བསྟན་པ་` (it was `[[?]]`); every other line and pointer is unchanged (diff against `0-INBOX/temp/TOC-lama-kunga-shebum/toc-tree-placed-round1.md`; the round-1 report is `qc-source-round1.md` beside it). The remaining 10 flags, checked against `0-INBOX/temp/TOC-lama-kunga-shebum/source.md`:

1. **7 repeated-pointer collisions** ([[3]], [[5]], [[19]], [[21]], [[23]], [[27]], [[33]]) — several sections open inside one indivisible alignment row; their headings stand at that row boundary. Expected at row granularity.
2. **3.2.1.2 — not a mismatch.** Line 17: `གཉིས་པ་ཐུན་མོ་མ་པའི་གླེང་གཞི་ལ་གཉིས་ཏེ། གདན་བཤམ་པ་དང་། ཆོ་འཕྲུལ་བགྱེ་བའོ།` — two parts, as in the tree. The 3/4-way phrases the checker read belong to children that already have 3 and 4 children.
3. **3.2.1.2.2.3 — not a mismatch.** Line 27: `གསུམ་པ་ཆོས་སྣང་བའི་ཆོ་འཕྲུལ་བསྟན་པ་ནི་གཉིས་ཏེ། འཁོར་བསྡུ་བ་དང་ཆོས་སྣང་བ་དངོས་སོ།` — two parts, as in the tree.
4. **3.2.3.15 — the author's own inconsistency, for the human.** Line 137 announces three parts (`ཡུམ་སྔགས་ཀྱི་རང་བཞིན་དུ་བསྟན་པ་དང་། སྔགས་དངོས་བསྟན་པ་དང་། དོན་བསྡུས་ཏེ་བསྟན་པའོ།`), but the text never opens the third: line 169 (`དེ་ལ་སློབས་ཅིག་པར་གདམས་པ་ནི།`, placed as 3.2.3.15.2.3.3) is followed directly by line 171 (`སྤྱི་དོན་བཞི་པ་མཐུན་འགྱུར་བསྟན་པ་ནི།`). No heading is invented for the unopened part.

Also: `qc_check_tree.py` reports 3 spurious "unattested" titles when the tree carries `[[N]]` pointers (it does not strip them) and 0 on the same tree without pointers; the corpus report kept is the pointer-free run.

issues_after_review: 0
