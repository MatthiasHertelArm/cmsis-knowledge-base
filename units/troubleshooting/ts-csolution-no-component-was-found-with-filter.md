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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4481"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4481", "Open-CMSIS-Pack/devtools@30f5e817:libs/rteutils/src/RteUtils.cpp:616"]
---

## Symptom

`no component was found with filter '<…>'`

## Cause

`csolution list components -f <words>` found components, but none whose component ID contains all the filter words; `<…>` is the filter. Matching is case-insensitive substring matching and every word must match.

## Fix

Loosen the filter, e.g. `-f CORE` or `-f Device`, or run without `-f` to see all component IDs.

## Trigger in the source

```cpp
if (filteredIds.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4481`
- `libs/rteutils/src/RteUtils.cpp:616`
