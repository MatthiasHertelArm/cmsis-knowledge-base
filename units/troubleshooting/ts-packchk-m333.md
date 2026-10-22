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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The component defined has no condition. If the component has restrictions, then add a condition to the component definition. Refer to [/package/components/.../component](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_component)."
summary: "packchk prints this warning for a PDSC component element that does not reference any condition, so the component is not restricted by a condition."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M333`
`Component has no condition: 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Csub=%CSUB%, Cversion=%CVER%'`

## Cause

packchk prints this warning for a PDSC component element that does not reference any condition, so the component is not restricted by a condition. The variable parts (Cclass, Cgroup, Csub, Cversion) identify the component that has no condition. The README states the same cause; the source lines were not available to confirm the exact trigger.

## Fix

Open the PDSC file, find the component with the given Cclass, Cgroup, Csub and Cversion, and add a condition reference to it if it has restrictions, for example <condition>...</condition> pointing to a condition defined under <conditions> that lists the required components. If the component really needs no restriction, the warning can be accepted.

## Note

Only the message text, README and trigger description were available; the source lines were not checked, so the exact trigger condition is not confirmed. The README wording says the component 'has restrictions' before adding a condition, so the warning is advisory for components that genuinely need no condition.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
