---
id: "ts-packchk-m219"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M219: Unable to find specified schema file '…'"
status: "draft"
tool: "packchk"
severity: "error"
code: "M219"
symptoms: ["M219", "Unable to find specified schema file '%PATH%'"]
symptom_regex: "^Unable to find specified schema file '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "The schema file given with --xsd does not exist (a relative path is resolved against the current working directory)."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:105", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackOptions.cpp:272-287", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CreateModel.cpp:151-162", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:697-727", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:730-762", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:54-57"]
---

## Symptom

`M219`
`Unable to find specified schema file '%PATH%'`

## Cause

The schema file given with --xsd does not exist (a relative path is resolved against the current working directory). The same message appears when the stored schema path no longer exists when the check starts.

## Fix

Point --xsd at an existing PACK.xsd, preferably with an absolute path; or omit --xsd so packchk uses the PACK.xsd of its installation (./, ../etc/ or ../../etc/ next to the executable); or use --disable-validation to skip the schema check.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:105`
- `tools/packchk/src/PackOptions.cpp:272-287`
- `tools/packchk/src/CreateModel.cpp:151-162`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:697-727`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:730-762`
- `tools/packchk/README.md:54-57`
