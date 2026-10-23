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
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "The definition of the board referenced in the example application could not be found."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:140", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:1507-1548", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:198-229", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:165"]
---

## Symptom

`M324`
`Board referenced in Example '%EXAMPLE%' not found: '[%VENDOR%] %BOARD%'`

## Cause

The definition of the board referenced in the example application could not be found. Define the board ([/package/boards/board](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html#element_board)) or correct the reference information ([/package/examples/example/board](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_examples_pg.html#element_example_board)).

## Fix

Make the example's <board name="..." vendor="..."/> match a <board> defined in this pack, or pass the BSP pack that defines the board with -i.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:140`
- `tools/packchk/src/ValidateSyntax.cpp:1507-1548`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:198-229`
- `tools/packchk/README.md:165`
