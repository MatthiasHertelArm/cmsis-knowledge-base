---
id: "ts-csolution-initializing-rte-kernel-failed"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: initializing RTE Kernel failed"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["initializing RTE Kernel failed"]
symptom_regex: "^initializing RTE Kernel failed$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:506"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "ProjMgrKernel::Get() returned no kernel object while the worker was initializing the model for the first time, so InitializeModel() stops before loading any packs or the global model."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:504-508"]
---

## Symptom

`initializing RTE Kernel failed`

## Cause

ProjMgrKernel::Get() returned no kernel object while the worker was initializing the model for the first time, so InitializeModel() stops before loading any packs or the global model. The source does not show what inside the kernel creation fails, so the cause of the null return is not visible from these lines.

## Fix

The source gives no user-level remedy for this message. Check that the csolution installation is complete and that the csolution binary runs (for example with --version), then rerun the command; if it persists, report it with the full build log.

## Trigger in the source

```cpp
if (!m_kernel) {
```

## Note

This is an internal initialization failure with no README entry; the trigger is only the null check on m_kernel after ProjMgrKernel::Get(). The actual failure reason is not logged by these lines, so the fix above is a generic check rather than a documented remedy.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:504-508`
