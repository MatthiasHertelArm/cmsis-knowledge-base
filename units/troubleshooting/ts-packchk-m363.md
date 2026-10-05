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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The package is missing the API information for the specified component. Refer to [/package/apis](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_apis_pg.html#element_apis)."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:182", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSemantic.cpp:924-931", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:202"]
---

## Symptom

`M363`
`No API defined for Component 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Csub=%CSUB%, Cversion=%CVER%, Capiversion=%APIVER%'`

## Cause

A component has Capiversion, but no <api> with the same Cclass and Cgroup (and a compatible version) is defined in this pack or in a PDSC passed with -i.

## Fix

Add the API to <apis> (<api Cclass="..." Cgroup="..." Capiversion="...">), pass the pack that defines it with -i, or remove Capiversion if the component implements no API.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:182`
- `tools/packchk/src/ValidateSemantic.cpp:924-931`
- `tools/packchk/README.md:202`
