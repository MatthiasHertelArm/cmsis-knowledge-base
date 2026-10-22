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
summary: "ProjMgrWorker::InitializeModel obtained the kernel from ProjMgrKernel::Get() successfully, but the kernel's GetGlobalModel() returned a null pointer."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:496-513"]
---

## Symptom

`initializing RTE Model failed`

## Cause

ProjMgrWorker::InitializeModel obtained the kernel from ProjMgrKernel::Get() successfully, but the kernel's GetGlobalModel() returned a null pointer. The csolution tool therefore cannot create the RTE model that holds the packs and project data it needs to continue. The source lines do not show what makes the global model creation fail, so the trigger is internal to the tool rather than a particular user input.

## Fix

The source gives no user-level workaround. Check that the csolution tool installation is complete and not corrupted, and that the CMSIS pack root (CMSIS_PACK_ROOT or the default location) is accessible, then rerun the command. If the message persists, report it to the CMSIS devtools project with the csolution version and the command line.

## Trigger in the source

```cpp
if (!m_model) {
```

## Note

The README does not document this message. The trigger is a null-pointer check on m_model right after the kernel is created, so the failure is internal and the README-style advice on the pack root is my guess at likely causes, not something the source shows. Kernel creation failure is reported separately with 'initializing RTE Kernel failed' at line 506.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:496-513`
