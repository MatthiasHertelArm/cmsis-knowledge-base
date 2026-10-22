---
id: "ts-packchk-m378"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M378: Component 'Cclass=…, Cgroup=…, Csub=…, Cversion=…, implements the API defined in '…' but does not …"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M378"
symptoms: ["M378", "Component 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Csub=%CSUB%, Cversion=%CVER%, implements the API defined in '%NAME%' but does not attribute 'Capiversion' specifying the version it implements."]
symptom_regex: "^Component 'Cclass=.+?, Cgroup=.+?, Csub=.+?, Cversion=.+?, implements the API defined in '.+?' but does not attribute 'Capiversion' specifying the version it implements\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Add attribute Capiversion specifying the API version that is implemented in the component described in the message. Refer to [/package/components/.../component](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_component)."
summary: "The component in the PDSC declares an API through its Capiversion-related setup, i.e. it implements the API named in %NAME% (the component carries an api reference) but its component element has no Capiversion attribute stating which API version it implements."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (message M378 text; trigger lines not available in this session)"]
---

## Symptom

`M378`
`Component 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Csub=%CSUB%, Cversion=%CVER%, implements the API defined in '%NAME%' but does not attribute 'Capiversion' specifying the version it implements.`

## Cause

The component in the PDSC declares an API through its Capiversion-related setup, i.e. it implements the API named in %NAME% (the component carries an api reference) but its component element has no Capiversion attribute stating which API version it implements. Cclass, Cgroup, Csub and Cversion in the message identify the component that lacks the attribute.

## Fix

Add the Capiversion attribute to the component element in the PDSC file, set to the version of the API the component implements, for example <component Cclass="..." Cgroup="..." Capiversion="<api version>" .../>, then rerun packchk.

## Note

Source lines were not available, so the trigger condition is inferred from the message text and the README; the exact check in the source was not verified.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (message M378 text; trigger lines not available in this session)`
