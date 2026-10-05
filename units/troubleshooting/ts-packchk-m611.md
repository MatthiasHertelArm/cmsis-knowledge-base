---
id: "ts-packchk-m611"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M611: Multiple devices or variants defined by '[…] …'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M611"
symptoms: ["M611", "Multiple devices or variants defined by '[%VENDOR%] %MCU%'"]
symptom_regex: "^Multiple devices or variants defined by '\\[.+?\\] .+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "A <mountedDevice> of a <board> names a device that has <variant> children, so the board does not identify a single device."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:246", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:1741-1749", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1038-1076", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/data/RteTestBoard/ARM.RteTestBoard.pdsc:42", "Open-CMSIS-Pack/devtools@30f5e817:test/packs/ARM/RteTest_DFP/0.2.0/ARM.RteTest_DFP.pdsc:243-256"]
---

## Symptom

`M611`
`Multiple devices or variants defined by '[%VENDOR%] %MCU%'`

## Cause

A <mountedDevice> of a <board> names a device that has <variant> children, so the board does not identify a single device.

## Fix

Set Dname to the variant that is actually mounted, e.g. Dname="RteTest_ARMCM4_FP" instead of the parent device "RteTest_ARMCM4".

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:246`
- `tools/packchk/src/ValidateSyntax.cpp:1741-1749`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1038-1076`
- `tools/packchk/test/data/RteTestBoard/ARM.RteTestBoard.pdsc:42`
- `test/packs/ARM/RteTest_DFP/0.2.0/ARM.RteTest_DFP.pdsc:243-256`
