---
id: "ts-csolution-initializing-rte-model-failed"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: initializing RTE Model failed"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["initializing RTE Model failed"]
symptom_regex: "^initializing RTE Model failed$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:511"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "csolution could not obtain the global pack model from its kernel at start."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:509-513", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/include/RteKernel.h:119"]
---

## Symptom

`initializing RTE Model failed`

## Cause

csolution could not obtain the global pack model from its kernel at start. The model is created together with the kernel, independent of project files or options, so this indicates an internal failure rather than a project problem.

## Fix

Not fixable in the project files. Reinstall CMSIS-Toolbox and retry; if it persists, report it to Open-CMSIS-Pack/devtools with the output of `csolution -V`.

## Trigger in the source

```cpp
if (!m_model) {
```

## Note

Defensive check; no input path found that leaves the global model null.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:509-513`
- `libs/rtemodel/include/RteKernel.h:119`
