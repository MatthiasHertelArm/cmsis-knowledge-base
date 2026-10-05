---
id: "ts-csolution-mlops-npu-macs-value-does-not-match-dfp-device-i"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: mlops.npu.macs value does not match DFP device information"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["mlops.npu.macs value does not match DFP device information"]
symptom_regex: "^mlops\\.npu\\.macs value does not match DFP device information$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrMlops.cpp:292"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrMlops.cpp:286", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrMlops.cpp:253", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:6485", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/MLOps/npu_mismatch.csolution.yml:8", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:7950"]
---

## Symptom

`mlops.npu.macs value does not match DFP device information`

## Cause

`mlops:` - `npu:` - `macs:` in the csolution.yml (possibly combined with `npu: type:`) names a MAC count that no NPU of the selected device offers. csolution compares it with the `<feature type="NPU">` entries the DFP declares for the processors of the MLOps contexts; a type and a MAC count that each exist but not on the same NPU also trigger it. The value is still used for the Vela options.

## Fix

Set `macs:` to a value the device supports, or leave `npu:` out so that csolution takes type and MACs of the first NPU in the DFP. `csolution list npus my.csolution.yml` shows the NPUs and MAC counts per device.

## Trigger in the source

```cpp
if (find_if(npuInfoItems.begin(), npuInfoItems.end(), matchesMacs) == npuInfoItems.end()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrMlops.cpp:286`
- `tools/projmgr/src/ProjMgrMlops.cpp:253`
- `tools/projmgr/src/ProjMgrWorker.cpp:6485`
- `tools/projmgr/test/data/MLOps/npu_mismatch.csolution.yml:8`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:7950`
