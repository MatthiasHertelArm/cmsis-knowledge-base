---
id: "ts-csolution-no-installed-npu-was-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no installed NPU was found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no installed NPU was found"]
symptom_regex: "^no installed NPU was found$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:4386"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "`csolution list npus` found no NPU: none of the devices in the loaded packs (or, with a csolution.yml, the device of the selected contexts) declares an NPU feature (`<feature type=\"NPU\">`) in its DFP."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4355", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4385", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:6485"]
---

## Symptom

`no installed NPU was found`

## Cause

`csolution list npus` found no NPU: none of the devices in the loaded packs (or, with a csolution.yml, the device of the selected contexts) declares an NPU feature (`<feature type="NPU">`) in its DFP.

## Fix

Install the DFP of a device with an NPU (for example an Ethos-U based device) or select a context whose device has one. Run `csolution list devices` to check which devices are loaded.

## Trigger in the source

```cpp
if (npuInfos.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4355`
- `tools/projmgr/src/ProjMgrWorker.cpp:4385`
- `tools/projmgr/src/ProjMgrWorker.cpp:6485`
