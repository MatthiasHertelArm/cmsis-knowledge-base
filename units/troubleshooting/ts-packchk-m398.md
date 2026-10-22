---
id: "ts-packchk-m398"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M398: Attribute 'Dname' missing in expression using 'Pname=\"…\""
status: "draft"
tool: "packchk"
severity: "error"
code: "M398"
symptoms: ["M398", "Attribute 'Dname' missing in expression using 'Pname=\"%NAME%\""]
symptom_regex: "^Attribute 'Dname' missing in expression using 'Pname=\".+?\"$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "When using attribute Pname in the `<condition>` element the Dname attribue shall be present as well. Add attribute token{Dname} specifying the device name. Refer to [/package/conditions/condition](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_conditions_pg.html#element_condition)."
summary: "The PDSC contains a condition expression that uses the Pname attribute (device name) for the element named in the message, but the same expression does not carry the Dname attribute (device name variant) that the README says must accompany …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (trigger not available in the given lines; message text M398 and README cause used)"]
---

## Symptom

`M398`
`Attribute 'Dname' missing in expression using 'Pname="%NAME%"`

## Cause

The PDSC contains a condition expression that uses the Pname attribute (device name) for the element named in the message, but the same expression does not carry the Dname attribute (device name variant) that the README says must accompany Pname. packchk reports the missing Dname as M398 while checking the condition expression.

## Fix

Add a Dname attribute next to the Pname attribute in the affected <condition> element, using the device name that matches the Pname value, for example: <condition> <require Dname="<device-name>" Pname="%NAME%"/> </condition>. Then rerun packchk on the PDSC.

## Note

Source lines were not available, so the trigger condition is taken from the message text and the README only. The README cause says Dname shall be present when Pname is used in a <condition>; the exact placement of the check was not verified against the source.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (trigger not available in the given lines; message text M398 and README cause used)`
