---
id: "ts-csolution-no-component-was-found-for-device"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no component was found for device '…'"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no component was found for device '<…>'"]
symptom_regex: "^no component was found for device '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:4463"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution list components command loaded the packs for the selected context and resolved its target, but the active target reports no installed components after filtering."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4452-4463", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4460-4463"]
---

## Symptom

`no component was found for device '<…>'`

## Cause

The csolution list components command loaded the packs for the selected context and resolved its target, but the active target reports no installed components after filtering. The device named in the message is the context's device value as resolved for that context, so the message names the device whose component set came back empty. The source only shows that the device had no components; it does not show the specific reason the filter removed them.

## Fix

Check that the device name in the csolution project (or the --context selection) matches a device that exists in the installed packs, and that the packs providing it are installed (for example with cpackget or csolution's pack update). Then rerun the list command.

## Trigger in the source

```cpp
if (!selectedContext.empty()) {
```

## Note

The message is printed only when the context name is non-empty; an empty context gets the 'no installed component was found' message instead. README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4452-4463`
- `tools/projmgr/src/ProjMgrWorker.cpp:4460-4463`
