---
id: "ts-csolution-cproject-file-was-not-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: cproject file was not found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["cproject file was not found"]
symptom_regex: "^cproject file was not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:529"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A `project:` entry under projects: in the csolution.yml names a cproject.yml that does not exist at that path, relative to the folder of the csolution.yml."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:524-535", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:3031-3049", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:5346-5356"]
---

## Symptom

`cproject file was not found`

## Cause

A `project:` entry under projects: in the csolution.yml names a cproject.yml that does not exist at that path, relative to the folder of the csolution.yml. The message is prefixed with the path as written.

## Fix

Correct the path and file name (case matters on Linux), e.g. `- project: app/app.cproject.yml`, or create the missing project file.

## Trigger in the source

```cpp
if (cprojectFile.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:524-535`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:3031-3049`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:5346-5356`
