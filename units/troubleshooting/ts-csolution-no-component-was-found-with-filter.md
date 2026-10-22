---
id: "ts-csolution-no-component-was-found-with-filter"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no component was found with filter '…'"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no component was found with filter '<…>'"]
symptom_regex: "^no component was found with filter '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:4481"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution `list components` operation was given a filter argument, and none of the component IDs of the installed components of the selected contexts match it."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4477-4483", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4460-4474"]
---

## Symptom

`no component was found with filter '<…>'`

## Cause

The csolution `list components` operation was given a filter argument, and none of the component IDs of the installed components of the selected contexts match it. The component IDs are collected from the active target's filtered components after the packs are loaded and the target attributes are set, and the filter is applied to that list with the split filter terms; an empty result yields this error. The '<…>' in the message is the filter string the user passed.

## Fix

Check the filter spelling and the terms it uses against the component list the tool prints without a filter, then run the command again with the corrected filter. Also confirm that the required packs are installed and that the context (device/target) selected is the one that provides the components you expect.

## Trigger in the source

```cpp
if (filteredIds.empty()) {
```

## Note

The README does not document this message. The cause is inferred from the ListComponents code path: the message fires only when a filter is given and no component ID matches, so an empty component set without a filter gives a different message ('no component was found for device' or 'no installed component was found') instead.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4477-4483`
- `tools/projmgr/src/ProjMgrWorker.cpp:4460-4474`
