---
registered_id: vajrapani-dongyi-dronma
source_file: 1-SOURCES/Commentaries/bo-vajrapani-dongyi-dronma.md
pointer_source: 0-INBOX/temp/TOC-vajrapani-dongyi-dronma/source.md
pointer_source_sha1: 12e4b513199107dbdd5c052317fa56b6d704bb13
pointer_source_rebuild: python3 4-SYSTEM/Skills/aligned-corpus-intake/scripts/build_sources.py 0-INBOX/raw-data/intake-manifest.yaml --stage pre-toc --only bo-vajrapani-dongyi-dronma
qc_reports: [2-RAILS/Sections/Raw/toc-qc/toc-tree-qc-vajrapani-dongyi-dronma.md, 2-RAILS/Sections/Raw/toc-qc/toc-tree-qc-source-vajrapani-dongyi-dronma.md]
status: complete
qc_accepted: "1 closing-formula title (node 1.1), reviewed — see the source QC report"
---

## དཀར་ཆག / Table of Contents

* 1. ཟབ་མོའི་ཆོས་ཉིད་ལ་བརྟེན་པ་སོ་སོའི་སྐྱེ་བོའི་སྤྱོད་ཡུལ་མ་ཡིན་པ་ [[39]]
   * 1.1 སྟོང་པ་ཉིད་རབ་ཏུ་མི་གནས་པ་སྟོང་པ་ཉིད་ཀྱི་ཏིང་ངེ་འཛིན་ཡིད་ཀྱི་མངོན་སུམ་གྱིས་གཏན་ལ་ཕབ་པ་ [[55]]
   * 1.2 བཏང་སྙོམས་རབ་ཏུ་མི་གནས་པའི་མཚན་མ་མེད་པའི་ཏིང་ངེ་འཛིན་རང་རིག་པའི་མངོན་སུམ་གྱིས་གཏན་ལ་དབབ་པ་ [[99]]
   * 1.3 རྒྱུན་ཆད་རབ་ཏུ་མི་གནས་པ་རྣལ་འབྱོར་གྱིས་མངོན་སུམ་བློའི་སྤྱོད་ཡུལ་མ་ཡིན་པ་སྨོན་པ་མེད་པ་མེད་པའི་ཏིང་ངེ་འཛིན་བསྟན་པ་ [[101]]

## Placement

Each node's `[[N]]` is the line, in `pointer_source`, of the row its heading stands before (rows are indivisible alignment units). Columns: decimal, line, where the opening clause sits in its row (START, END->NEXT, MID), the clause verbatim. Written by the placement pass (`4-SYSTEM/Skills/aligned-corpus-intake/prompts/place-toc-at-rows.md`).

```tsv
1	39	START	ད་ནི་ཟབ་མོའི་ཆོས་ཉིད་ལ་བརྟེན་པ་སོ་སོའི་སྐྱེ་བོའི་སྤྱོད་ཡུལ་མ་ཡིན་པ་དྲན་པ་མེད་པ་དང་། སྐྱེ་བ་མེད་པ་དང་། བློའི་སྤྱོད་ཡུལ་
1.1	55	START	དེ་གསལ་བར་བྱེད་པ་ནི་དྲན་པས་མ་གོས་པ་ཡིད་ལ་མ་བྱས་པ་སྟོང་པ་ཉིད་དོ། །
1.2	99	START	ད་ནི་ཀུན་ནས་ཉོན་མོངས་པའི་ཆོས་རྣམས་དང་། རྣམ་པར་བྱང་བའི་ཆོས་རྣམས་ཀྱི་བདེན་པ་བཞི་མི་གནས་པས་ན་བཏང་སྙོམས་རབ་ཏུ་མི་གནས་པའི་
1.3	101	START	ད་ནི་རྒྱུན་ཆད་རབ་ཏུ་མི་གནས་པ་རྣལ་འབྱོར་གྱིས་མངོན་སུམ་བློའི་སྤྱོད་ཡུལ་མ་ཡིན་པ་སྨོན་པ་མེད་པ་མེད་པའི་ཏིང་ངེ་འཛིན་བསྟན་པར་
```
