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
doc_cause: "The condition has been defined already in a previous line. Correct the condition name, or remove the duplicate. Refer to [/package/conditions/condition](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_conditions_pg.html#element_condition)."
summary: "The PDSC contains two condition elements with the same id, so packchk reports the second one as redefining the first. %COND% is the duplicated condition name and %LINE% is the line in the PDSC where that name was first defined."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M330`
`Condition redefined: '%COND%', already defined in Line %LINE%`

## Cause

The PDSC contains two condition elements with the same id, so packchk reports the second one as redefining the first. %COND% is the duplicated condition name and %LINE% is the line in the PDSC where that name was first defined. The source lines were not available, so this reading comes from the message text and the README.

## Fix

Open the PDSC at the line of the second definition and either rename that condition so its id is unique, or delete the duplicate if both definitions are the same. Then update any component or device condition references that were meant to point to the intended definition.

## Note

Source lines were not available; the cause and fix are taken from the message text and the README entry, not from the trigger code.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
