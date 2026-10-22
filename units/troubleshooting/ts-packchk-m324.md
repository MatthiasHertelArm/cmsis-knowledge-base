---
id: "ts-packchk-m324"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M324: Board referenced in Example '…' not found: '[…] …'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M324"
symptoms: ["M324", "Board referenced in Example '%EXAMPLE%' not found: '[%VENDOR%] %BOARD%'"]
symptom_regex: "^Board referenced in Example '.+?' not found: '\\[.+?\\] .+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The definition of the board referenced in the example application could not be found. Define the board ([/package/boards/board](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html#element_board)) or correct the reference information ([/package/examples/example/board](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_examples_pg.html#element_example_board))."
summary: "packchk found an example in the PDSC whose board reference (the vendor and board name in its board element) does not match any board defined in the pack."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (trigger not inspected; clone unavailable)"]
---

## Symptom

`M324`
`Board referenced in Example '%EXAMPLE%' not found: '[%VENDOR%] %BOARD%'`

## Cause

packchk found an example in the PDSC whose board reference (the vendor and board name in its board element) does not match any board defined in the pack. The %EXAMPLE% is the example's name, %VENDOR% and %BOARD% are the reference values as written in the example.

## Fix

Either add a board element for the referenced board under /package/boards in the PDSC, or correct the vendor and board name in the example's board element under /package/examples/example so that it matches an existing board definition exactly.

## Note

Answered from the message text and README only; the source trigger was not available to confirm the exact comparison (for example whether vendor and board name are matched case-sensitively).

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (trigger not inspected; clone unavailable)`
