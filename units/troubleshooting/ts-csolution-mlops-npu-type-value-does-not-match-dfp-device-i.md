---
id: "ts-csolution-mlops-npu-type-value-does-not-match-dfp-device-i"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: mlops.npu.type value does not match DFP device information"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["mlops.npu.type value does not match DFP device information"]
symptom_regex: "^mlops\\.npu\\.type value does not match DFP device information$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrMlops.cpp:283"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "`mlops:` - `npu:` - `type:` in the csolution.yml names an NPU type (e.g."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrMlops.cpp:277", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:6485", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:7958"]
---

## Symptom

`mlops.npu.type value does not match DFP device information`

## Cause

`mlops:` - `npu:` - `type:` in the csolution.yml names an NPU type (e.g. Ethos-U85) that the DFP does not declare as an NPU feature for the processors of the MLOps contexts. The comparison is exact text. The value is still used for the Vela options.

## Fix

Write the NPU type exactly as the DFP declares it, or remove `type:` so that csolution takes it from the DFP. `csolution list npus my.csolution.yml` shows the types per device.

## Trigger in the source

```cpp
if (find_if(npuInfoItems.begin(), npuInfoItems.end(), matchesType) == npuInfoItems.end()) {
```

## Note

The tests check that this warning is absent in the mismatch and no-NPU cases; none provokes it.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrMlops.cpp:277`
- `tools/projmgr/src/ProjMgrWorker.cpp:6485`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:7958`
