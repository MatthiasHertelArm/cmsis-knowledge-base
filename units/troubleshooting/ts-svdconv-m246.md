---
id: "ts-svdconv-m246"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M246: C Expression: Only one Item allowed!"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M246"
symptoms: ["M246", "C Expression: Only one Item allowed!"]
symptom_regex: "^C Expression: Only one Item allowed!$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:147", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:154", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:159", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCExpressionParser.cpp:198", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:113"]
---

## Symptom

`M246`
`C Expression: Only one Item allowed!`

## Cause

A peripheral contains more than one <disableCondition>; only one is allowed (the schema also allows at most one) and svdconv ignores the extra one. The message carries no line number or peripheral name.

## Fix

Keep a single <disableCondition> per peripheral and combine several conditions in it with && or ||.

## Note

LogMsg("M246") is called without a line number, so the output does not say which peripheral is affected; search the file for <disableCondition>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:147`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:154`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:159`
- `tools/svdconv/SVDModel/src/SvdCExpressionParser.cpp:198`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:113`
