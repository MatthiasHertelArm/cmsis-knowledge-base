---
id: "ts-csolution-csolution-file-was-not-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: csolution file was not found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["csolution file was not found"]
symptom_regex: "^csolution file was not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:271"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:267-274", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:319-321"]
---

## Symptom

`csolution file was not found`

## Cause

The *.csolution.yml given on the command line (positional or `--solution`/`-s`) does not exist at that path; a relative path is resolved from the current working directory. The message is prefixed with the path as given.

## Fix

Correct the path or file name, or run csolution from the folder that contains the solution.

## Trigger in the source

```cpp
if (!RteFsUtils::Exists(m_csolutionFile)) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:267-274`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:319-321`
