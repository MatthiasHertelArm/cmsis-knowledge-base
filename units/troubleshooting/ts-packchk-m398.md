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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "When using attribute Pname in the `<condition>` element the Dname attribue shall be present as well."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:217", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckConditions.cpp:152-164", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:232"]
---

## Symptom

`M398`
`Attribute 'Dname' missing in expression using 'Pname="%NAME%"`

## Cause

When using attribute Pname in the `<condition>` element the Dname attribue shall be present as well. Add attribute token{Dname} specifying the device name. Refer to [/package/conditions/condition](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_conditions_pg.html#element_condition).

## Fix

Add Dname to the same expression that uses Pname, e.g. <require Dname="MyDevice" Pname="cm4"/>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:217`
- `tools/packchk/src/CheckConditions.cpp:152-164`
- `tools/packchk/README.md:232`
