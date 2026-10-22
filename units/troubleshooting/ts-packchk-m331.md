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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The condition has been defined but not used further. Remove the condition or add condition rules. Refer to [/package/conditions/condition](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_conditions_pg.html#element_condition)."
summary: "packchk prints M331 when a condition is defined in the PDSC under /package/conditions but no component, device, or other condition references it."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (trigger not inspected; clone unavailable)"]
---

## Symptom

`M331`
`Condition unused: '%COND%'`

## Cause

packchk prints M331 when a condition is defined in the PDSC under /package/conditions but no component, device, or other condition references it. The %COND% placeholder is the condition's id. The README describes the same situation. Since the source is not available here, this reading comes from the message and the README text alone.

## Fix

Either delete the unused <condition id="%COND%"> element from the PDSC, or add a reference to it, for example by setting condition="%COND%" on the component or bundle that should use it, or by using it inside another condition that is used.

## Note

Source lines were not available, so the trigger condition was not verified. The README gives the same cause and fix. Whether the check considers references from other conditions as usage was not confirmed.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (trigger not inspected; clone unavailable)`
