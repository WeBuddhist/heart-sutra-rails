---
registered_id: vimalamitra-tika
source_file: 1-SOURCES/Commentaries/bo-vimalamitra-tika.md
pointer_source: 0-INBOX/temp/TOC-vimalamitra-tika/source.md
pointer_source_sha1: 86bf41fdbf7c1a3c77d37692c7428738e61bc0ea
pointer_source_rebuild: python3 4-SYSTEM/Skills/aligned-corpus-intake/scripts/build_sources.py 0-INBOX/raw-data/intake-manifest.yaml --stage pre-toc --only bo-vimalamitra-tika
qc_reports: [2-RAILS/Sections/Raw/toc-qc/toc-tree-qc-vimalamitra-tika.md, 2-RAILS/Sections/Raw/toc-qc/toc-tree-qc-source-vimalamitra-tika.md]
status: complete
qc_accepted: "2 parts placed by the passage the announcing verse names (question, answer) — reviewed, see the source QC report"
---

## དཀར་ཆག / Table of Contents

* 1. རྒྱལ་བའི་ཡུམ་གྱི་སྙིང་པོ་ [[9]]
   * 1.1 གླེང་སློང་བ་ [[11]]
   * 1.2 སྐབས་ [[11]]
   * 1.3 བསྟན་པར་གཏོགས་པ་འདུས་པ་ [[13]]
   * 1.4 གླེང་གཞི་ [[13]]
   * 1.5 དྲིས་ [[19]]
   * 1.6 ལན་བཏབ་པ་ [[23]]
   * 1.7 རྗེས་སུ་མཐུན་པ་ [[101]]
   * 1.8 རྗེས་སུ་ཡི་རང་ [[113]]

## Placement

Each node's `[[N]]` is the line, in `pointer_source`, of the row its heading stands before (rows are indivisible alignment units). Columns: decimal, line, where the opening clause sits in its row (START, END->NEXT, MID), the clause verbatim. Written by the placement pass (`4-SYSTEM/Skills/aligned-corpus-intake/prompts/place-toc-at-rows.md`).

```tsv
1	9	MID	རྒྱལ་བའི་ཡུམ་གྱི་སྙིང་པོ་བཤད་པར་བྱ། །གླེང་སློང་བ་དང་སྐབས་དང་ནི། །བསྟན་པར་གཏོགས་པ་འདུས་པ་དང༌། །གླེང་གཞི་དྲིས་དང་ལན་བཏབ་པ།
1.1	11	START	བསྟན་པར་བྱ་བའི་དངོས་པོ་མདོར་བསྡུས་ནས། འདི་སྐད་ཅེས་འབྱུང་བ་ལ་སོགས་པ་དང་པོའི་ཚིག་གསུམ་གྱིས་གླེང་སློང་བར་བྱེད་དོ། །
1.2	11	MID	ད་ནི་ཐོས་པའི་རང་གི་ངོ་བོ་བསྟན་པའི་ཕྱིར། དུས་གཅིག་ན་ཞེས་འབྱུང་བ་ལ་སོགས་པ་སྐབས་རྩོམ་པར་བྱེད་དེ།
1.3	13	MID	དགེ་སློང་གི་དགེ་འདུན་ཆེན་པོ་དང་ཞེས་འབྱུང་བ་ལ་སོགས་པ་ནི་བསྟན་པར་གཏོགས་པ་འདུས་པར་སྟོན་ཏེ།
1.4	13	START	གླེང་གཞི་གང་གིས་བསྟན་པ་འདི་འཇུག་པའི་གླེང་གཞི་དེ་བཤད་པའི་ཕྱིར། དེའི་ཚེ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ།
1.5	19	START	དེ་ནས་ཞེས་འབྱུང་བ་ནི་སྐབས་འདིར་དེ་མ་ཐག་ཏུའོ། །སངས་རྒྱས་ཀྱི་མཛད་པའི་མཐུ་ནི་སངས་རྒྱས་ཀྱི་མཐུས་ཏེ།
1.6	23	START	དེ་སྐད་ཅེས་ཞེས་འབྱུང་བ་ནི་རྣམ་པ་སྔ་མ་ལ་བྱའོ། །སྨྲས་པ་དང་ཞེས་འབྱུང་བ་ནི་བརྗོད་པ་དང་ཞེས་བྱའོ། །
1.7	101	START	དེ་ནས་ཞེས་འབྱུང་བ་ནི་སྐབས་འདིར་བར་མ་ཆད་པར་རོ། །ཏིང་ངེ་འཛིན་དེ་ལས་འབྱུང་བ་ནི་སྔར་བསྟན་པ་ལས་སོ། །
1.8	113	START	དེ་ལྟར་བཅོམ་ལྡན་འདས་ཀྱིས་འཕགས་པ་སྤྱན་རས་གཟིགས་དབང་ཕྱུག་གིས་བསྟན་པ་ལ་རང་གི་རྗེས་སུ་མཐུན་པ་བསྟན་ནས།
```
