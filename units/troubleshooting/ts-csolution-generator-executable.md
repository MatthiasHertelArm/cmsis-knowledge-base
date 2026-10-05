---
id: "ts-csolution-generator-executable"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: generator executable '…' was not found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["generator executable '<…>' was not found"]
symptom_regex: "^generator executable '.+?' was not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5147"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5144-5149", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteGenerator.cpp:103-145", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteItem.cpp:599-604"]
---

## Symptom

`generator executable '<…>' was not found`

## Cause

The pack generator selected with `-g` has no command for this host: its `<exe>` element lists no `<command>` for the host OS (host attribute win, linux or mac), or the command is a web URL. The `<…>` is the generator id.

## Fix

Run the generator on a host its pack supports, or update the pack; the pack's documentation tells how to start the tool otherwise.

## Trigger in the source

```cpp
if (generatorExe.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:5144-5149`
- `libs/rtemodel/src/RteGenerator.cpp:103-145`
- `libs/rtemodel/src/RteItem.cpp:599-604`
