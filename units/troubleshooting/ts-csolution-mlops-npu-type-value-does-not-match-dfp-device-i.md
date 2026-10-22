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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrMlops.cpp:283"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution sets an NPU type under mlops.npu.type that matches no NPU entry of the Device Family Pack (DFP) for the target device."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrMlops.cpp:239", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrMlops.cpp:245-251", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrMlops.cpp:278-284"]
---

## Symptom

`mlops.npu.type value does not match DFP device information`

## Cause

The csolution sets an NPU type under mlops.npu.type that matches no NPU entry of the Device Family Pack (DFP) for the target device. The tool collects the NPU info items of the DFP for the selected processors (pnames), keeps the ones whose pname matches, and warns when none of them has the type the user gave. The type is taken from the solution after $...$ variable expansion, so a value that expands to something unexpected also triggers it.

## Fix

Set mlops.npu.type to one of the NPU types the DFP advertises for the device, or omit mlops.npu.type and let the tool choose the default from the DFP, or set mlops.npu.macs and let the tool find the matching type. Check the spelling against the DFP device description and confirm the device and processor are correct and the DFP is installed.

## Trigger in the source

```cpp
if (find_if(npuInfoItems.begin(), npuInfoItems.end(), matchesType) == npuInfoItems.end()) {
```

## Note

The README does not document this message. The fix list is derived from the source: when type is empty the tool picks a default, and when only macs is given it looks up the type from macs. The code does not state the exact accepted type names.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrMlops.cpp:239`
- `tools/projmgr/src/ProjMgrMlops.cpp:245-251`
- `tools/projmgr/src/ProjMgrMlops.cpp:278-284`
