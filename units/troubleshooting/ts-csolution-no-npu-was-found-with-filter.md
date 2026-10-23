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
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:4436"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "`csolution list npus -f <words>` found NPUs, but no entry matched all filter words; `<…>` is the filter."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4407", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4436"]
---

## Symptom

`no NPU was found with filter '<…>'`

## Cause

`csolution list npus -f <words>` found NPUs, but no entry matched all filter words; `<…>` is the filter. A word matches either the NPU line (type and MACs) or one of its device lines (vendor, device, processor, core); matching is case-insensitive.

## Fix

Loosen the filter, e.g. `-f U55` or a device name part, or run without `-f`.

## Trigger in the source

```cpp
if (npusVec.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4407`
- `tools/projmgr/src/ProjMgrWorker.cpp:4436`
