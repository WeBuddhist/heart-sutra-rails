# TOC tree vs. source QC report

issues: 10

## Issues

- 3.2.3.15.3 དོན་བསྡུས་ཏེ་བསྟན་པ་: pointer is [[?]] — unresolved anchor, not a clean tree
- pointer [[3]] is shared by 4 nodes (1, 1.1, 1.2, 1.3) — repeated-pointer collision, the extractor likely lost its cursor partway through this run
- pointer [[5]] is shared by 6 nodes (1.4, 2, 3, 3.1, 3.1.1, 3.1.2) — repeated-pointer collision, the extractor likely lost its cursor partway through this run
- pointer [[19]] is shared by 3 nodes (3.2.1.2, 3.2.1.2.1, 3.2.1.2.2) — repeated-pointer collision, the extractor likely lost its cursor partway through this run
- pointer [[21]] is shared by 4 nodes (3.2.1.2.2.1, 3.2.1.2.2.1.1, 3.2.1.2.2.1.1.1, 3.2.1.2.2.1.1.2) — repeated-pointer collision, the extractor likely lost its cursor partway through this run
- pointer [[23]] is shared by 4 nodes (3.2.1.2.2.1.1.3, 3.2.1.2.2.1.1.4, 3.2.1.2.2.1.2, 3.2.1.2.2.1.2.1) — repeated-pointer collision, the extractor likely lost its cursor partway through this run
- pointer [[27]] is shared by 3 nodes (3.2.1.2.2.3, 3.2.1.2.2.3.1, 3.2.1.2.2.3.1.1) — repeated-pointer collision, the extractor likely lost its cursor partway through this run
- pointer [[33]] is shared by 3 nodes (3.2.1.2.2.3.2, 3.2.1.2.2.3.2.1, 3.2.1.2.2.3.2.2) — repeated-pointer collision, the extractor likely lost its cursor partway through this run
- 3.2.1.2 'གཉིས་པ་ཐུན་མོ་མ་པའི་གླེང་གཞི་': announcing text names a 3, 4-way division but the tree gives it 2 child(ren) — verify by hand which is right
- 3.2.1.2.2.3 'གསུམ་པ་ཆོས་སྣང་བའི་ཆོ་འཕྲུལ་བས': announcing text names a 3-way division but the tree gives it 2 child(ren) — verify by hand which is right

## Notes (not counted as issues)

- (none)

## Reviewed by the orchestrator before repair (2026-10-03)

- **Not to be repaired — the 7 repeated-pointer collisions** ([[3]], [[5]], [[19]], [[21]], [[23]], [[27]], [[33]]). The source is segmented into indivisible alignment rows; where several nested or sibling sections open inside one row, all their headings stand at that row boundary. Lama Kunga's preliminary section and the start of his main section all fall in the first two rows (lines 3 and 5). These pointers come from the placement pass and are expected at row granularity; they are not cursor loss.
- **To repair (tree structure, against the source):**
  1. `3.2.3.15.3 དོན་བསྡུས་ཏེ་བསྟན་པ་` — no opening clause was found anywhere in the source (`[[?]]`). Keep the node only if the source attests it; otherwise remove it.
  2. `3.2.1.2 གཉིས་པ་ཐུན་མོ་མ་པའི་གླེང་གཞི་` — its announcing text names a 3- or 4-way division; the tree gives it 2 children.
  3. `3.2.1.2.2.3 གསུམ་པ་ཆོས་སྣང་བའི་ཆོ་འཕྲུལ་བས` — its announcing text names a 3-way division; the tree gives it 2 children.
