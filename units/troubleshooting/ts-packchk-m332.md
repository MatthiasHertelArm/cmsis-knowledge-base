---
id: "ts-packchk-m332"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M332: Condition undefined: '…'"
status: "draft"
tool: "packchk"
severity: "error"
code: "M332"
symptoms: ["M332", "Condition undefined: '%COND%'"]
symptom_regex: "^Condition undefined: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "A condition has been used but not defined."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:148", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckConditions.cpp:223-267", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1201-1247", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:173"]
---

## Symptom

`M332`
`Condition undefined: '%COND%'`

## Cause

A condition has been used but not defined. Correct the name of the condition or define the missing condition. Refer to [/package/conditions/condition](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_conditions_pg.html#element_condition).

## Fix

Define <condition id="..."> with exactly the referenced id (spelling and case), or change the condition attribute to an existing id.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:148`
- `tools/packchk/src/CheckConditions.cpp:223-267`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1201-1247`
- `tools/packchk/README.md:173`
