# TOC tree vs. source QC report

issues: 7

## Issues

- 2.2.2 གཉིས་པ་གང་ལ་བྱིན་གྱིས་བརླབ་པར་བྱ་བའི་གང་: title attested in the source but not near pointer [[30]] (found near line 26) — possible cursor loss
- 2.2.2.2 གཉིས་པ་ཤཱ་རིའི་བུ་ལ་བྱིན་གྱིས་རློབ་ཚུལ་: title attested in the source but not near pointer [[36]] (found near line 30) — possible cursor loss
- 2.2.3.2.1.1.2.2 གཉིས་པ་ཆོས་ཀྱི་རང་བཞིན་བརྒྱད་དུ་དབྱེ་བ་: title attested in the source but not near pointer [[62]] (found near line 52) — possible cursor loss
- 2.2.3.2.1.2.2 གཉིས་པ་སྐྱེས་མཆེད་བཅུ་གཉིས་: title attested in the source but not near pointer [[78]] (found near line 74) — possible cursor loss
- 2.2.3.2.1.3.2 གཉིས་པ་ལམ་འཕགས་པའི་བདེན་པ་བཞི་: title attested in the source but not near pointer [[86]] (found near line 82) — possible cursor loss
- 2.2.3.2.1.3.3 གསུམ་པ་འབྲས་བུ་སངས་རྒྱས་ཀྱི་ཡེ་ཤེས་བཤད་པ: title attested in the source but not near pointer [[88]] (found near line 82) — possible cursor loss
- 2.2.3.2.4.1.2 གཉིས་པ་སྔགས་དོན་བཤད་པ་: title attested in the source but not near pointer [[104]] (found near line 100) — possible cursor loss

## Notes (not counted as issues)

- (none)

## Reviewed — accepted (orchestrator, 2026-10-03)

All 7 issues are the same pattern, checked line by line against `0-INBOX/temp/TOC-gendun-rinchen-migje/source.md`: the node's full title is stated only in its parent's enumeration row (the line the checker names), and the section itself opens later on a row that begins with a bare ordinal. The pointer is on that opening row, which is correct; the checker's ±3-line title window cannot see the enumeration row.

| Node | Pointer | Opening row (verbatim start) |
|---|---|---|
| 2.2.2 | 30 | གཉིས་པ་ལ་གཉིས། སྤྱན་རས་གཟིགས་ལ་བྱིན་གྱིས་རློབ་ཚུལ་… |
| 2.2.2.2 | 36 | གཉིས་པ་ནི། དེ་ནས་སངས་རྒྱས་ཀྱི་མཐུས་… |
| 2.2.3.2.1.1.2.2 | 62 | གཉིས་པ་ནི། ཤཱ་རིའི་བུ། དེ་ལྟར་ཆོས་ཐམས་ཅད་སྟོང་པ་ཉིད་… |
| 2.2.3.2.1.2.2 | 78 | གཉིས་པ་ནི། མིག་མེད། རྣ་བ་མེད། … |
| 2.2.3.2.1.3.2 | 86 | གཉིས་པ་ནི། དེ་བཞིན་དུ་སྡུག་བསྔལ་བ་དང་། … |
| 2.2.3.2.1.3.3 | 88 | གསུམ་པ་ནི། ཡེ་ཤེས་མེད། ཐོབ་པ་མེད། … |
| 2.2.3.2.4.1.2 | 104 | གཉིས་པ་ནི། ཏདྱ་ཐཱ། ཨོཾ་ག་ཏེ་… |

issues_after_review: 0
