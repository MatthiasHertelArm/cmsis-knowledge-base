---
id: "ts-packchk-m349"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M349: Examples found, but no board description(s) found"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M349"
symptoms: ["M349", "Examples found, but no board description(s) found"]
symptom_regex: "^Examples found, but no board description\\(s\\) found$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M349`
`Examples found, but no board description(s) found`

## Cause

Example projects have been found for a board that was not defined. Correct the entry for the examples ([/package/examples/example/board](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_examples_pg.html#element_example_board)) or define the board ([/package/boards/board](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html#element_board)).

## Fix

_siehe Cause_
