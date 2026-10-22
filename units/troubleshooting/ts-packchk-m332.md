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
doc_cause: "A condition has been used but not defined. Correct the name of the condition or define the missing condition. Refer to [/package/conditions/condition](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_conditions_pg.html#element_condition)."
summary: "A component or device reference in the PDSC names a condition with a <condition id=...> reference that has no matching <condition> definition in the same pack."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M332`
`Condition undefined: '%COND%'`

## Cause

A component or device reference in the PDSC names a condition with a <condition id=...> reference that has no matching <condition> definition in the same pack. The %COND% placeholder is the condition id the user wrote.

## Fix

Find the condition id printed in the message and either correct its spelling to match an existing <condition id="..."> under /package/conditions, or add the missing <condition> element with that id. Refer to the CMSIS-Pack specification for the condition element.

## Note

The source lines were not available, so the trigger and handling are inferred from the message text and the README only; verify against the source before relying on the exact trigger.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
