---
id: "ts-packchk-m324"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M324: Board referenced in Example"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M324"
symptoms: ["M324", "Board referenced in Example '%EXAMPLE%' not found: '[%VENDOR%] %BOARD%'"]
symptom_regex: "^Board referenced in Example '.+?' not found: '\\[.+?\\] .+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M324`
`Board referenced in Example '%EXAMPLE%' not found: '[%VENDOR%] %BOARD%'`

## Cause

The definition of the board referenced in the example application could not be found. Define the board ([/package/boards/board](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html#element_board)) or correct the reference information ([/package/examples/example/board](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_examples_pg.html#element_example_board)).

## Fix

_siehe Cause_
