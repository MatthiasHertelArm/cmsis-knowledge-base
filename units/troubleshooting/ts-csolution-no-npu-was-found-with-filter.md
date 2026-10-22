---
id: "ts-csolution-no-npu-was-found-with-filter"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no NPU was found with filter '…'"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no NPU was found with filter '<…>'"]
symptom_regex: "^no NPU was found with filter '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:4436"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The NPU listing collected at least one installed NPU, but none of them matched the filter string the user passed, so the result list is empty."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4400-4434", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4435-4437"]
---

## Symptom

`no NPU was found with filter '<…>'`

## Cause

The NPU listing collected at least one installed NPU, but none of them matched the filter string the user passed, so the result list is empty. A filter word counts as matched if it appears in the NPU description line. Otherwise it must match one of that NPU's device lines, and the NPU is dropped if no device line matches. The '<…>' in the message is the filter text as given by the user.

## Fix

Check the filter words for typos or for names that do not appear in the NPU or device descriptions, then retry with a broader filter. To see every installed NPU, run the same listing command without the filter argument.

## Trigger in the source

```cpp
if (npusVec.empty()) {
```

## Note

This message is only reached when a non-empty filter was given, because without a filter every collected NPU is added. The separate message 'no installed NPU was found' at line 4386 covers the case where no NPU is installed at all. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4400-4434`
- `tools/projmgr/src/ProjMgrWorker.cpp:4435-4437`
