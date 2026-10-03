---
registered_id: prasastrasena-tika
source_file: 1-SOURCES/Commentaries/bo-prasastrasena-tika.md
pointer_source: 0-INBOX/temp/TOC-prasastrasena-tika/source.md
pointer_source_sha1: fa24a8a75ab7207822e30b808f541c8623647947
pointer_source_rebuild: python3 4-SYSTEM/Skills/aligned-corpus-intake/scripts/build_sources.py 0-INBOX/raw-data/intake-manifest.yaml --stage pre-toc --only bo-prasastrasena-tika
qc_reports: [2-RAILS/Sections/Raw/toc-qc/toc-tree-qc-prasastrasena-tika.md, 2-RAILS/Sections/Raw/toc-qc/toc-tree-qc-source-prasastrasena-tika.md]
status: complete
---

## དཀར་ཆག / Table of Contents

* 1. མདོ་སྡེ་འདི་བཤད་པ་ [[5]]
   * 1.1 ཤེས་རབ་ཀྱི་མིང་ [[5]]
   * 1.2 གླེང་གཞི་ [[7]]
   * 1.3 སྙོམས་པར་འཇུག་པ་ [[9]]
   * 1.4 གླེང་བསླབ་པ་བསྟན་པ་ [[11]]
   * 1.5 ཤེས་རབ་ལ་འཇུག་པ་ [[15]]
   * 1.6 ཤེས་རབ་ཀྱི་མཚན་ཉིད་ [[19]]
   * 1.7 ཤེས་རབ་ཀྱི་སྤྱོད་ཡུལ་ [[33]]
   * 1.8 ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ཡོན་ཏན་ [[99]]
   * 1.9 ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་འབྲས་བུ་ [[109]]
   * 1.10 ཤེས་རབ་ཀྱི་གཟུངས་ [[115]]

## Placement

Each node's `[[N]]` is the line, in `pointer_source`, of the row its heading stands before (rows are indivisible alignment units). Columns: decimal, line, where the opening clause sits in its row (START, END->NEXT, MID), the clause verbatim. Written by the placement pass (`4-SYSTEM/Skills/aligned-corpus-intake/prompts/place-toc-at-rows.md`).

```tsv
1	5	MID	མདོ་སྡེ་འདི་བཤད་པ་ལ་དོན་རྣམ་པ་བཅུས་གསལ་བར་བྱ་སྟེ།
1.1	5	MID	འདི་ནི་ཤེས་རབ་ཀྱི་མིང་སྟེ།
1.2	7	START	འདི་ནི་གླེང་གཞི།
1.3	9	START	འདི་ནི་སྙོམས་པར་འཇུག་པ་སྟེ།
1.4	11	START	འདི་ནི་གླེང་བསླབ་པ་བསྟན་པ་སྟེ།
1.5	15	START	འདི་ནི་ཤེས་རབ་ལ་འཇུག་པ་སྟེ།
1.6	19	START	འདི་ནི་ཤེས་རབ་ཀྱི་མཚན་ཉིད་དེ།
1.7	33	START	འདི་ནི་ཤེས་རབ་ཀྱི་སྤྱོད་ཡུལ་ཏེ།
1.8	99	MID	འདི་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ཡོན་ཏན།
1.9	109	START	འདི་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་འབྲས་བུ་སྟེ།
1.10	115	START	འདི་ནི་ཤེས་རབ་ཀྱི་གཟུངས་ཏེ།
```
