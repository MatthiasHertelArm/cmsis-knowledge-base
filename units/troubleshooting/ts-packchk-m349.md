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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Example projects have been found for a board that was not defined. Correct the entry for the examples ([/package/examples/example/board](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_examples_pg.html#element_example_board)) or define the board ([/package/boards/board](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html#element_board))."
summary: "The PDSC contains example entries that reference a board through the example board attribute, but no board is described in the PDSC under the boards element. packchk reports this when examples are found and the board list is empty."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M349`
`Examples found, but no board description(s) found`

## Cause

The PDSC contains example entries that reference a board through the example board attribute, but no board is described in the PDSC under the boards element. packchk reports this when examples are found and the board list is empty.

## Fix

Either add a boards/board entry in the PDSC for each board the examples target, or correct the example entries so their board attribute names a board that is defined. Check the spelling of the board name in the example against the board element name.

## Note

Source lines were not available; the cause and fix rely on the message text and the README. The README points to the example board element and the board element of the PDSC spec as the two places to correct.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
