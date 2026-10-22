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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrMlops.cpp:292"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution sets an mlops.npu.macs value (after variable expansion) and the DFP device information lists NPU entries for the selected processors, but none of those entries has a matching MACs count."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrMlops.cpp:286-294", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrMlops.cpp:287-290", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrMlops.cpp:248", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrMlops.cpp:253-275"]
---

## Symptom

`mlops.npu.macs value does not match DFP device information`

## Cause

The csolution sets an mlops.npu.macs value (after variable expansion) and the DFP device information lists NPU entries for the selected processors, but none of those entries has a matching MACs count. The comparison strips the "MACs" suffix from the DFP values and compares them numerically; when the NPU type is also set, the entry must additionally have that same type. So the user's macs value (or the macs/type pair) does not correspond to any NPU the device's pack provides.

## Fix

Check the mlops.npu.macs value in the csolution YAML against the NPU configurations the selected device's DFP offers, and correct it to a listed MACs count. Alternatively remove mlops.npu.macs so the tool picks the matching value from the DFP when mlops.npu.type is set or from the first NPU entry when neither is set. If mlops.npu.type is also set, make sure the type and MACs describe the same NPU.

## Trigger in the source

```cpp
if (find_if(npuInfoItems.begin(), npuInfoItems.end(), matchesMacs) == npuInfoItems.end()) {
```

## Note

The message is not documented in the README. The sibling message for mlops.npu.type is printed at line 283 under the same condition style. The warning only fires when the DFP provides NPU info items for the device's pnames, so it does not appear for devices without NPU data.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrMlops.cpp:286-294`
- `tools/projmgr/src/ProjMgrMlops.cpp:287-290`
- `tools/projmgr/src/ProjMgrMlops.cpp:248`
- `tools/projmgr/src/ProjMgrMlops.cpp:253-275`
