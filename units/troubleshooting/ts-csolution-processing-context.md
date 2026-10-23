---
id: "ts-csolution-processing-context"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: processing context '…' failed"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["processing context '<…>' failed"]
symptom_regex: "^processing context '.+?' failed$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgr.cpp:743"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "One or more errors occurred while csolution processed the named context (packs, device or board, components, linker, output types, compiler or other settings)."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:742", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4107", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:4351", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:4787"]
---

## Symptom

`processing context '<…>' failed`

## Cause

One or more errors occurred while csolution processed the named context (packs, device or board, components, linker, output types, compiler or other settings). This line only sums them up; the specific errors are printed before it.

## Fix

Fix the errors reported before this line for the same context, e.g. a missing pack, a component not found or a redefinition, then run again.

## Trigger in the source

```cpp
if (!m_worker.ProcessContext(contextItem, true, true, false)) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:742`
- `tools/projmgr/src/ProjMgrWorker.cpp:4107`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:4351`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:4787`
