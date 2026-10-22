---
id: "ts-packchk-m325"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M325: Board '…' redefined, already defined in Line …: '…'"
status: "draft"
tool: "packchk"
severity: "error"
code: "M325"
symptoms: ["M325", "Board '%NAME%' redefined, already defined in Line %LINE%: '%PATH%'"]
symptom_regex: "^Board '.+?' redefined, already defined in Line .+?: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "This board has been defined already in the line _'LINE'_ of the file _'PATH'_. Verify and remove one of the board definitions. Refer to [/package/boards/board](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html#element_board)."
summary: "Two <board> elements in the checked PDSC have the same name and revision."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:141", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:1584-1608", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteBoard.cpp:32-39", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteBoard.cpp:246-249", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:166"]
---

## Symptom

`M325`
`Board '%NAME%' redefined, already defined in Line %LINE%: '%PATH%'`

## Cause

Two <board> elements in the checked PDSC have the same name and revision. The line numbers are swapped: the message is reported at the earlier board and its 'Line' names the later one.

## Fix

Remove the duplicate <board>, or give the boards different name or revision values.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:141`
- `tools/packchk/src/ValidateSyntax.cpp:1584-1608`
- `libs/rtemodel/src/RteBoard.cpp:32-39`
- `libs/rtemodel/src/RteBoard.cpp:246-249`
- `tools/packchk/README.md:166`
