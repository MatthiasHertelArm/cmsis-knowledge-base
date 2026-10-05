---
id: "ts-csolution-found-multiple-device-variants"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: found multiple device variants"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["found multiple device variants"]
symptom_regex: "^found multiple device variants$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1504"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1502-1512", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:3394-3409", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestSolution/TestProject4/test_board_multi_variant.cproject.yml", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestSolution/TestProject4/test_board_multi_variant_and_device.cproject.yml"]
---

## Symptom

`found multiple device variants`

## Cause

The selected device, from `device:` or from the board's mounted device, has variants in its pack, and csolution needs one variant. The error that follows lists the variant names.

## Fix

Set `device:` in the target type to one of the listed variants, e.g. `device: RteTest_ARMCM4_FP`.

## Trigger in the source

```cpp
if (matchedDevice->GetDeviceItemCount() > 0) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:1502-1512`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:3394-3409`
- `tools/projmgr/test/data/TestSolution/TestProject4/test_board_multi_variant.cproject.yml`
- `tools/projmgr/test/data/TestSolution/TestProject4/test_board_multi_variant_and_device.cproject.yml`
