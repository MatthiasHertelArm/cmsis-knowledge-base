---
id: "ts-csolution-no-unresolved-dependency-was-found-with-filter"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no unresolved dependency was found with filter '…'"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no unresolved dependency was found with filter '<…>'"]
symptom_regex: "^no unresolved dependency was found with filter '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4509"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4492", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4509", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4544"]
---

## Symptom

`no unresolved dependency was found with filter '<…>'`

## Cause

`csolution list dependencies -f <words>` or `csolution list configs -f <words>` produced entries, but none contains all the filter words; `<…>` is the filter. Both commands print this same text, so for `list configs` it means that no configuration file matched the filter, not anything about dependencies.

## Fix

Loosen the filter or run the command without `-f` to see all unresolved dependencies or all configuration files of the selected contexts.

## Trigger in the source

```cpp
if (filteredConfigs.empty()) {
```

## Note

The cited line 4509 is in ListConfigs; ListDependencies raises the identical text at line 4544.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4492`
- `tools/projmgr/src/ProjMgrWorker.cpp:4509`
- `tools/projmgr/src/ProjMgrWorker.cpp:4544`
