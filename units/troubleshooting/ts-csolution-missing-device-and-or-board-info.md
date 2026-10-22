---
id: "ts-csolution-missing-device-and-or-board-info"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: missing device and/or board info"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["missing device and/or board info"]
symptom_regex: "^missing device and/or board info$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:1351"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "ProcessDevice runs for a build context whose csolution input names neither a board nor a device."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1347-1353", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1349-1351"]
---

## Symptom

`missing device and/or board info`

## Cause

ProcessDevice runs for a build context whose csolution input names neither a board nor a device. GetDeviceItem fills deviceItem from context.device, and the check fails when context.board is empty and deviceItem.name is empty. The project or target therefore has no device and no board to resolve against, so the tool stops with this error for that context. The context name is passed as the second argument, so the log line identifies which context is affected.

## Fix

Give the project or target a device or a board in its csolution YAML, for example a device: entry naming the part number, or a board: entry naming a board that the installed packs provide. Make sure the device or board name is spelled as the pack declares it, since an unresolved device name leaves deviceItem.name empty as well. Then rerun csolution.

## Trigger in the source

```cpp
if (context.board.empty() && deviceItem.name.empty()) {
```

## Note

The README does not document this message. The cause is inferred from the trigger condition only; the exact YAML key that feeds context.device and context.board is not shown in the lines given, so the fix names the keys by their usual meaning and should be checked against the schema.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:1347-1353`
- `tools/projmgr/src/ProjMgrWorker.cpp:1349-1351`
