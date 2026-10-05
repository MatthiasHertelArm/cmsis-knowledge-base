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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1446"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The board selected with `board:` lists exactly one mounted device in its pack, but that device is not found in the loaded packs, typically because the device family pack (DFP) is not listed under packs: or not installed."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1428-1450", "Open-CMSIS-Pack/devtools@30f5e817:test/packs/ARM/RteTest_DFP/0.2.0/ARM.RteTest_DFP.pdsc:555-560"]
---

## Symptom

`board mounted device <…> not found`

## Cause

The board selected with `board:` lists exactly one mounted device in its pack, but that device is not found in the loaded packs, typically because the device family pack (DFP) is not listed under packs: or not installed. The `<…>` is the mounted device as Vendor::Name. The check runs before an explicit `device:` is considered, so setting `device:` does not avoid it.

## Fix

Add the device family pack that defines this device under packs:, e.g. `- pack: Keil::STM32U5xx_DFP`, and install it with `cpackget add <Vendor::Pack>`.

## Trigger in the source

```cpp
if (!device) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:1428-1450`
- `test/packs/ARM/RteTest_DFP/0.2.0/ARM.RteTest_DFP.pdsc:555-560`
