---
id: "ts-packchk-m390"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M390: Condition '…': Direct or indirect recursion detected. …"
status: "draft"
tool: "packchk"
severity: "error"
code: "M390"
symptoms: ["M390", "Condition '%NAME%': Direct or indirect recursion detected. %MSG%"]
symptom_regex: "^Condition '.+?': Direct or indirect recursion detected\\. .+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "Evaluating a <condition> failed because it refers to itself, directly or through a chain of condition=\"...\" references in its <require>, <accept> or <deny> expressions."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:209", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckConditions.cpp:42-55", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteCondition.cpp:501-506", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteCondition.cpp:889-904", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteCondition.cpp:955-956"]
---

## Symptom

`M390`
`Condition '%NAME%': Direct or indirect recursion detected. %MSG%`

## Cause

Evaluating a <condition> failed because it refers to itself, directly or through a chain of condition="..." references in its <require>, <accept> or <deny> expressions. The same evaluation error, and so the same message, occurs when such a condition attribute names a condition id that is not defined. packchk skips the condition in later checks.

## Fix

Follow the condition="..." references from the named condition, break the loop, and make sure every referenced condition id is defined in <conditions>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:209`
- `tools/packchk/src/CheckConditions.cpp:42-55`
- `libs/rtemodel/src/RteCondition.cpp:501-506`
- `libs/rtemodel/src/RteCondition.cpp:889-904`
- `libs/rtemodel/src/RteCondition.cpp:955-956`
