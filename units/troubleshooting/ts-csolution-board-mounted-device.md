---
id: "ts-csolution-board-mounted-device"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: board mounted device … not found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["board mounted device <…> not found"]
symptom_regex: "^board mounted device .+? not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:1446"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The board selected for the project lists a mounted device (name and vendor taken from the board's pack)."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1444-1446", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1474"]
---

## Symptom

`board mounted device <…> not found`

## Cause

The board selected for the project lists a mounted device (name and vendor taken from the board's pack). When csolution looks that device up in the filtered device model built for the project, the lookup returns nothing, so the device the board mounts is not among the devices csolution has loaded. The placeholder is the full device name of that mounted device. The source does not show how the filtered model is populated, so the likely reason, that the pack providing that device is not installed or not part of the project's packs, is an inference.

## Fix

Check that the pack that defines the board's mounted device is installed. If it is missing, install it with cpackget add Vendor::PackName, using the vendor and pack that define the device. Then make sure the project's pack selection includes it. If the board is meant to use a different device, select it explicitly in the csolution YAML instead of relying on the board's mounted device.

## Trigger in the source

```cpp
if (!device) {
```

## Note

The message is printed only when exactly one mounted device exists and it is missing from context.rteFilteredModel. The cause of the missing entry (missing pack versus filtering) is not shown in these lines. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:1444-1446`
- `tools/projmgr/src/ProjMgrWorker.cpp:1474`
