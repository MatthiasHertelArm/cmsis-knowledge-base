---
id: "ts-packchk-m331"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M331: Condition unused: '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M331"
symptoms: ["M331", "Condition unused: '%COND%'"]
symptom_regex: "^Condition unused: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The condition has been defined but not used further. Remove the condition or add condition rules. Refer to [/package/conditions/condition](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_conditions_pg.html#element_condition)."
summary: "A <condition> is defined in <conditions>, but no element refers to it through a condition attribute, neither directly nor through another condition."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:147", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckConditions.cpp:273-304", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckConditions.cpp:96-145", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:172", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:85-90"]
---

## Symptom

`M331`
`Condition unused: '%COND%'`

## Cause

A <condition> is defined in <conditions>, but no element refers to it through a condition attribute, neither directly nor through another condition.

## Fix

Delete the unused condition or reference it where intended, e.g. <component ... condition="MyCondition">; suppress with -x M331 if it is kept on purpose.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:147`
- `tools/packchk/src/CheckConditions.cpp:273-304`
- `tools/packchk/src/CheckConditions.cpp:96-145`
- `tools/packchk/README.md:172`
- `tools/packchk/README.md:85-90`
