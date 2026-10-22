---
id: "ts-packchk-m362"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M362: Not all Component Dependencies for 'Cclass=…, Cgroup=…, Csub=…, Cversion=…, Capiversion=…' can be …"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M362"
symptoms: ["M362", "Not all Component Dependencies for 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Csub=%CSUB%, Cversion=%CVER%, Capiversion=%APIVER%' can be resolved.%MSG%"]
symptom_regex: "^Not all Component Dependencies for 'Cclass=.+?, Cgroup=.+?, Csub=.+?, Cversion=.+?, Capiversion=.+?' can be resolved\\..+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Some of the component dependencies could not be resolved. The message might contain additional information. Verify and correct component definition and dependency information. Refer to [/package/components/.../component](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_component) attribute _condition_."
summary: "packchk prints M362 when, for the component named in the message (Cclass, Cgroup, Csub, Cversion, Capiversion), at least one of its dependencies in the PDSC cannot be matched to a component or bundle available in the pack set being checked."
cause_origin: "source-analysis"
confidence: "medium"
---

## Symptom

`M362`
`Not all Component Dependencies for 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Csub=%CSUB%, Cversion=%CVER%, Capiversion=%APIVER%' can be resolved.%MSG%`

## Cause

packchk prints M362 when, for the component named in the message (Cclass, Cgroup, Csub, Cversion, Capiversion), at least one of its dependencies in the PDSC cannot be matched to a component or bundle available in the pack set being checked. The %MSG% suffix may carry the specific dependency that failed. The source was not available, so this reading comes from the message text and the README only.

## Fix

Open the PDSC entry for the named component and check its dependencies against the components that exist in the pack. Correct the Cclass, Cgroup, Csub or Cversion values in the dependency, or add the missing component or condition definition, then rerun packchk. Read the additional detail after the message text to find the dependency that failed.

## Note

Source lines were not available; the cause and fix rely on the message text and README. The README links to the component condition attribute, which is about component conditions and may not describe the dependency resolution directly.
