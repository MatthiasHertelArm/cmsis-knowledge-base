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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "Add attribute Capiversion specifying the API version that is implemented in the component described in the message."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:197", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSemantic.cpp:924-938", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:216"]
---

## Symptom

`M378`
`Component 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Csub=%CSUB%, Cversion=%CVER%, implements the API defined in '%NAME%' but does not attribute 'Capiversion' specifying the version it implements.`

## Cause

Add attribute Capiversion specifying the API version that is implemented in the component described in the message. Refer to [/package/components/.../component](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_component).

## Fix

Add Capiversion with the API version the component implements, e.g. <component Cclass="CMSIS Driver" Cgroup="USART" Capiversion="2.4.0" ...>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:197`
- `tools/packchk/src/ValidateSemantic.cpp:924-938`
- `tools/packchk/README.md:216`
