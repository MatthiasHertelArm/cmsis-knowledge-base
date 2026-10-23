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
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "Example projects have been found for a board that was not defined."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:167", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:190"]
---

## Symptom

`M349`
`Examples found, but no board description(s) found`

## Cause

Example projects have been found for a board that was not defined. Correct the entry for the examples ([/package/examples/example/board](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_examples_pg.html#element_example_board)) or define the board ([/package/boards/board](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html#element_board)).

## Fix

Define the boards that the examples reference with <boards><board name="..." vendor="..."> in this pack, or pass the BSP that defines them with -i; otherwise correct the example's <board> reference.

## Note

No raise site for M349 at 30f5e81; fix inferred from the message and README. Missing boards for examples are reported per example as M324.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:167`
- `tools/packchk/README.md:190`
