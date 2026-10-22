---
id: "ts-csolution-no-installed-device-was-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no installed device was found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no installed device was found"]
symptom_regex: "^no installed device was found$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:4338"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution list devices command builds its list from the device items in the filtered RTE model of each selected context, after loading the packs for that context."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4337-4340", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4311-4336", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4342-4344"]
---

## Symptom

`no installed device was found`

## Cause

The csolution list devices command builds its list from the device items in the filtered RTE model of each selected context, after loading the packs for that context. When no installed pack provides a device leaf (a device entry with no sub-items), the set stays empty and the tool prints this message. The filter argument is applied only after this check, so a filter cannot cause this message.

## Fix

Install the device pack(s) that provide the devices you want to list, then run the list command again. If you expected devices from a specific pack, check that it is installed and that the context selects it. The source does not show further steps.

## Trigger in the source

```cpp
if (devicesSet.empty()) {
```

## Note

The README does not document this message. The cause is inferred from the ListDevices function: devices are skipped when they have sub-items, and the message fires only when no leaf device remains across all selected contexts. Whether the pack list is empty or only contains devices with sub-items is not visible in these lines.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4337-4340`
- `tools/projmgr/src/ProjMgrWorker.cpp:4311-4336`
- `tools/projmgr/src/ProjMgrWorker.cpp:4342-4344`
