---
id: "ts-csolution-is-not-among-board-mounted-devices"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: specified device '…' is not among board mounted devices"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["specified device '<…>' is not among board mounted devices"]
symptom_regex: "^specified device '.+?' is not among board mounted devices$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:1490"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The context sets both `board:` and `device:`, and the device (`<…>`) is not one of the devices the BSP declares as mounted on that board. csolution builds for the device given, not for the board's device."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1480", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:3430"]
---

## Symptom

`specified device '<…>' is not among board mounted devices`

## Cause

The context sets both `board:` and `device:`, and the device (`<…>`) is not one of the devices the BSP declares as mounted on that board. csolution builds for the device given, not for the board's device.

## Fix

If the board carries that device, remove `device:` and let the board determine it, or set `device:` to the mounted device (`csolution list boards` and the BSP show it). Keep the combination only if you deliberately target a different device on the board.

## Trigger in the source

```cpp
if (!match) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:1480`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:3430`
