---
id: "ts-packchk-m325"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M325: redefined, already defined in Line"
status: "draft"
tool: "packchk"
severity: "error"
code: "M325"
symptoms: ["M325", "Board '%NAME%' redefined, already defined in Line %LINE%: '%PATH%'"]
symptom_regex: "^Board '.+?' redefined, already defined in Line .+?: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M325`
`Board '%NAME%' redefined, already defined in Line %LINE%: '%PATH%'`

## Cause

This board has been defined already in the line _'LINE'_ of the file _'PATH'_. Verify and remove one of the board definitions. Refer to [/package/boards/board](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html#element_board).

## Fix

_siehe Cause_
