---
id: "ts-csolution-generator-executable-file"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: generator executable file '…' does not exist"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["generator executable file '<…>' does not exist"]
symptom_regex: "^generator executable file '.+?' does not exist$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:5151"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The pack generator's command resolved to a file that does not exist."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5150-5153", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteGenerator.cpp:103-168", "Open-CMSIS-Pack/devtools@30f5e817:libs/crossplatform/test/src/UnitTests.cpp:118", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:3741-3758"]
---

## Symptom

`generator executable file '<…>' does not exist`

## Cause

The pack generator's command resolved to a file that does not exist. Relative commands are taken from the pack folder; a command with a `key` attribute takes its folder from that Windows registry value or, on Linux/macOS, the environment variable of that name. The `<…>` is the resolved path.

## Fix

Check that the pack is installed completely (reinstall it if the file is missing) and that a tool referenced through a key is installed and its registry value/environment variable points to it.

## Trigger in the source

```cpp
if(!RteFsUtils::Exists(generatorExe)) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:5150-5153`
- `libs/rtemodel/src/RteGenerator.cpp:103-168`
- `libs/crossplatform/test/src/UnitTests.cpp:118`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:3741-3758`
