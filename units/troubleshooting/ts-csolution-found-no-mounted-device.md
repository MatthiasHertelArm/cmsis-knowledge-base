---
id: "ts-csolution-found-no-mounted-device"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: found no mounted device"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["found no mounted device"]
symptom_regex: "^found no mounted device$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:1440"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The `board:` refers to a board whose pack description lists no mounted device (only compatible devices)."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1430-1442", "Open-CMSIS-Pack/devtools@30f5e817:test/packs/ARM/RteTest_DFP/0.2.0/ARM.RteTest_DFP.pdsc:542-547", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:3412-3427", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestSolution/TestProject4/test_board_no_mounted_device.cproject.yml"]
---

## Symptom

`found no mounted device`

## Cause

The `board:` refers to a board whose pack description lists no mounted device (only compatible devices). The check fails even when `device:` is also set.

## Fix

Use a board (or board support pack version) that declares its mounted device, or select the target with `device:` only and drop `board:`.

## Trigger in the source

```cpp
} else if (mountedDevices.size() == 0) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:1430-1442`
- `test/packs/ARM/RteTest_DFP/0.2.0/ARM.RteTest_DFP.pdsc:542-547`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:3412-3427`
- `tools/projmgr/test/data/TestSolution/TestProject4/test_board_no_mounted_device.cproject.yml`
