---
id: "ts-csolution-missing-rte-target"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: missing RTE target"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["missing RTE target"]
symptom_regex: "^missing RTE target$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:1978"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "ProcessComponents() needs the RTE active target of the build context to resolve the components a project requires."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1977-1980", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1983"]
---

## Symptom

`missing RTE target`

## Cause

ProcessComponents() needs the RTE active target of the build context to resolve the components a project requires. When rteActiveTarget is null, it logs 'missing RTE target' and returns failure before any component is matched. The given lines do not show where rteActiveTarget is assigned, so the reason it stays unset is not established here. It most likely means the target for this context could not be set up, for example because the device, target type or required packs were not resolved.

## Fix

The source lines do not show a direct user-side fix. Check the log above this message for earlier errors about the device, board, target type or packs of this project, and resolve those first. Then confirm that the packs the project uses are installed and that the csolution project refers to a valid device or target, and run the build again.

## Trigger in the source

```cpp
if (!context.rteActiveTarget) {
```

## Note

The message has no code and the README does not document it. The assignment of rteActiveTarget lies outside the given lines, so the upstream cause is inferred and not confirmed. The message is logged without the context name, so it does not say which project or target failed.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:1977-1980`
- `tools/projmgr/src/ProjMgrWorker.cpp:1983`
