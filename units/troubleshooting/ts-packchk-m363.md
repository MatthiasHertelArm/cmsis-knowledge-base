---
id: "ts-packchk-m363"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M363: No API defined for Component 'Cclass=…, Cgroup=…, Csub=…, Cversion=…, Capiversion=…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M363"
symptoms: ["M363", "No API defined for Component 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Csub=%CSUB%, Cversion=%CVER%, Capiversion=%APIVER%'"]
symptom_regex: "^No API defined for Component 'Cclass=.+?, Cgroup=.+?, Csub=.+?, Cversion=.+?, Capiversion=.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The package is missing the API information for the specified component. Refer to [/package/apis](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_apis_pg.html#element_apis)."
summary: "packchk prints this warning when a component in the PDSC declares an API version (Capiversion) for which the package has no matching <apis> entry under /package/apis."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (trigger lines not available in this session)"]
---

## Symptom

`M363`
`No API defined for Component 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Csub=%CSUB%, Cversion=%CVER%, Capiversion=%APIVER%'`

## Cause

packchk prints this warning when a component in the PDSC declares an API version (Capiversion) for which the package has no matching <apis> entry under /package/apis. The message variables Cclass, Cgroup, Csub and Cversion identify the component, and Capiversion is the API version it refers to that the package does not define.

## Fix

Add an <apis> element under <package> with an <api> entry whose Cclass, Cgroup, Csub and Capiversion match the component's API reference, or remove the apiversion reference from the component if it is not needed. Then rerun packchk.

## Note

Answered from the message text and the README only; the source clone was not available, so the trigger condition is inferred from the message wording and the README's reference to /package/apis.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (trigger lines not available in this session)`
