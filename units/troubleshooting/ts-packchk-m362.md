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
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "Some of the component dependencies could not be resolved."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:181", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSemantic.cpp:877-973", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSemantic.cpp:154-190", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackOptions.cpp:422-426", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:198-229", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:201"]
---

## Symptom

`M362`
`Not all Component Dependencies for 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Csub=%CSUB%, Cversion=%CVER%, Capiversion=%APIVER%' can be resolved.%MSG%`

## Cause

Some of the component dependencies could not be resolved. The message might contain additional information. Verify and correct component definition and dependency information. Refer to [/package/components/.../component](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_component) attribute _condition_.

## Fix

Read the M502/M504 lines that follow; they name the dependency that fails. Provide the required component or API in this pack, pass the providing pack's PDSC with -i (e.g. ARM.CMSIS.pdsc for CMSIS:CORE), or correct Cclass/Cgroup/Csub/Capiversion in the condition. -x M362 also suppresses M502 and M504.

## Note

Bug at 30f5e81: bOk in TestComponentDependencies is set before the component loop and never reset (ValidateSemantic.cpp:890, 950), so after the first failing component every later component is also reported with M362.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:181`
- `tools/packchk/src/ValidateSemantic.cpp:877-973`
- `tools/packchk/src/ValidateSemantic.cpp:154-190`
- `tools/packchk/src/PackOptions.cpp:422-426`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:198-229`
- `tools/packchk/README.md:201`
