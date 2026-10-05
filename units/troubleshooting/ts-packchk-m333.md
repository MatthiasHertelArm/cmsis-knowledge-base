---
id: "ts-packchk-m333"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M333: Component has no condition: 'Cclass=…, Cgroup=…, Csub=…, Cversion=…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M333"
symptoms: ["M333", "Component has no condition: 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Csub=%CSUB%, Cversion=%CVER%'"]
symptom_regex: "^Component has no condition: 'Cclass=.+?, Cgroup=.+?, Csub=.+?, Cversion=.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:149", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:54", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:174"]
---

## Symptom

`M333`
`Component has no condition: 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Csub=%CSUB%, Cversion=%CVER%'`

## Cause

The component defined has no condition. If the component has restrictions, then add a condition to the component definition. Refer to [/package/components/.../component](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_component).

## Fix

If the component only applies to certain devices, compilers or other components, add a condition attribute naming a <condition> that expresses this; otherwise no change is needed.

## Note

No raise site for M333 at 30f5e81 (only the progress message M085 'Checking if Component has Condition' exists in the table). Fix inferred from the message and README.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:149`
- `tools/packchk/src/PackChk_Msgs.cpp:54`
- `tools/packchk/README.md:174`
