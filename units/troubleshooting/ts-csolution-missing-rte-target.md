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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1978"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "csolution reached component or configuration-file processing for a context that has no RTE target; the target is created when packs are loaded for the context."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1974", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:737", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:597"]
---

## Symptom

`missing RTE target`

## Cause

csolution reached component or configuration-file processing for a context that has no RTE target; the target is created when packs are loaded for the context. It is an internal guard that normal project input does not reach, and no test exercises it.

## Fix

Fix the errors reported before this message (pack loading, device or board selection). If it is the only error, report it to the CMSIS-Toolbox maintainers with the solution that produces it.

## Trigger in the source

```cpp
if (!context.rteActiveTarget) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:1974`
- `tools/projmgr/src/ProjMgrWorker.cpp:737`
- `tools/projmgr/src/ProjMgrWorker.cpp:597`
