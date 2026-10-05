---
id: "ts-csolution-no-context-was-found-with-filter"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no context was found with filter '…'"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no context was found with filter '<…>'"]
symptom_regex: "^no context was found with filter '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4843"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4834", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:903"]
---

## Symptom

`no context was found with filter '<…>'`

## Cause

`csolution list contexts -f <words>` found no context name (`<project>.<build-type>+<target-type>`) that contains all the filter words; `<…>` is the filter. Matching is case-insensitive substring matching.

## Fix

Use a part of a project, build-type or target-type name that exists, e.g. `-f Debug`, or run `csolution list contexts my.csolution.yml` without `-f`.

## Trigger in the source

```cpp
if (filteredContexts.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4834`
- `tools/projmgr/src/ProjMgr.cpp:903`
