---
id: "ts-csolution-file-not-allowed-to-be-updated"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: file not allowed to be updated"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["file not allowed to be updated"]
symptom_regex: "^file not allowed to be updated$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrYamlEmitter.cpp:57"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "WriteFile generated the YAML content for a file that already exists and differs from it, so CompareFile returned false."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlEmitter.cpp:55-58", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlEmitter.cpp:39", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlEmitter.cpp:90-99"]
---

## Symptom

`file not allowed to be updated`

## Cause

WriteFile generated the YAML content for a file that already exists and differs from it, so CompareFile returned false. The caller passed allowUpdate as false, which forbids overwriting an existing file, so the write is refused. The message names the file (%NAME% is the filename argument) and the context of the operation.

## Fix

Check whether the listed file is a generated file that csolution should be allowed to rewrite. If it is a generated file you no longer need, remove it and run the command again so it is created fresh. If you edited it by hand, move your changes into the source input or revert the file, then run the command again. The lines shown do not identify which caller passes allowUpdate as false, so the exact option that enables the update is not established here.

## Trigger in the source

```cpp
if (!allowUpdate) {
```

## Note

The README does not document this message. The lines given do not show the callers that pass allowUpdate, so the option that sets it and the exact reason a caller forbids the update remain unverified. The cause is a reading of the trigger condition.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlEmitter.cpp:55-58`
- `tools/projmgr/src/ProjMgrYamlEmitter.cpp:39`
- `tools/projmgr/src/ProjMgrYamlEmitter.cpp:90-99`
