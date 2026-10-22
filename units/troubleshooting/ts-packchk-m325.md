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
summary: "packchk found two board entries with the same name in the PDSC package description."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (message M325 with the %NAME%, %LINE% and %PATH% placeholders; source lines not available)"]
---

## Symptom

`M325`
`Board '%NAME%' redefined, already defined in Line %LINE%: '%PATH%'`

## Cause

packchk found two board entries with the same name in the PDSC package description. The second definition of the board named by the message's board name was reached after an earlier definition of that board, at the line and file shown in the message, so the duplicate board name is rejected.

## Fix

Open the PDSC file named in the message at the line given and compare it with the earlier board definition. Keep one <board> element for that board name and delete or rename the other, then run packchk again.

## Note

Source lines were not available, so the trigger condition is inferred from the message text and the README; the README cause and fix are consistent with it. The README uses the placeholders 'LINE' and 'PATH' quoted, while the message prints %LINE% and %PATH%, which is a formatting difference only.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (message M325 with the %NAME%, %LINE% and %PATH% placeholders; source lines not available)`
