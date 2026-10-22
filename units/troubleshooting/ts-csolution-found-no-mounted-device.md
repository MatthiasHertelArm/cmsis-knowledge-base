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
summary: "The csolution matched a board, but the board's pack entry lists no mounted devices, so GetMountedDevices returns an empty list."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1431", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1439-1441", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1425-1428"]
---

## Symptom

`found no mounted device`

## Cause

The csolution matched a board, but the board's pack entry lists no mounted devices, so GetMountedDevices returns an empty list. The code at line 1439 treats an empty list as an error no matter whether the user also named a device, so the message appears whenever the selected board declares no mounted device.

## Fix

Check the board entry in the installed board pack for a mounted device declaration. If it has none, select a board that declares mounted devices, or correct the board pack. Then rerun the csolution command. Do not rely on adding a device name alone to clear this error, because the zero-device check does not depend on the device setting.

## Trigger in the source

```cpp
} else if (mountedDevices.size() == 0) {
```

## Note

The enclosing block condition is not in the lines given, so the exact entry path is inferred. The trigger is the zero-size branch, and it is reached regardless of deviceItem.name, which the other branch at line 1432 checks. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:1431`
- `tools/projmgr/src/ProjMgrWorker.cpp:1439-1441`
- `tools/projmgr/src/ProjMgrWorker.cpp:1425-1428`
