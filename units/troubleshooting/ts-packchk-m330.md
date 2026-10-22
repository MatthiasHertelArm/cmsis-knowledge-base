---
id: "ts-packchk-m330"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M330: Condition redefined: '…', already defined in Line …"
status: "draft"
tool: "packchk"
severity: "error"
code: "M330"
symptoms: ["M330", "Condition redefined: '%COND%', already defined in Line %LINE%"]
symptom_regex: "^Condition redefined: '.+?', already defined in Line .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "The condition has been defined already in a previous line."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:146", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckConditions.cpp:195-216", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:171"]
---

## Symptom

`M330`
`Condition redefined: '%COND%', already defined in Line %LINE%`

## Cause

The condition has been defined already in a previous line. Correct the condition name, or remove the duplicate. Refer to [/package/conditions/condition](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_conditions_pg.html#element_condition).

## Fix

Give one of the conditions a unique id (and update the condition attributes meant to use it), or delete the duplicate.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:146`
- `tools/packchk/src/CheckConditions.cpp:195-216`
- `tools/packchk/README.md:171`
