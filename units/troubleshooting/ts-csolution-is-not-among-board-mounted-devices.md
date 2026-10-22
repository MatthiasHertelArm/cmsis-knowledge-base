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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:1490"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The project names a device (deviceItem.name) that exists in the installed packs, and it also selects a board whose mounted-device list is non-empty."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1481-1492", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1454-1477", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1495-1500"]
---

## Symptom

`specified device '<…>' is not among board mounted devices`

## Cause

The project names a device (deviceItem.name) that exists in the installed packs, and it also selects a board whose mounted-device list is non-empty. The device name is not among that board's mounted devices, so the check at line 1489 fails and the tool prints the warning. The placeholder in the message is the full device name, optionally prefixed with the vendor. The build continues because this is only a warning.

## Fix

Either set the device in the project to one of the devices the board mounts, or remove the device setting so csolution uses the board's mounted device (lines 1495-1500 apply the board device when no device is named). To find the valid names, check the board's mounted devices in its pack description.

## Trigger in the source

```cpp
if (!match) {
```

## Note

The message is a warning, not an error, so processing continues with the specified device. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:1481-1492`
- `tools/projmgr/src/ProjMgrWorker.cpp:1454-1477`
- `tools/projmgr/src/ProjMgrWorker.cpp:1495-1500`
