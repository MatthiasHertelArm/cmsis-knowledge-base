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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:1504"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The message is printed when the device the project resolved to is a parent device that has device variants under it (RteDeviceItem::VARIANT items), so the selection is not a single concrete device."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1503-1511", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1455-1478", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1495-1500", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1506-1509"]
---

## Symptom

`found multiple device variants`

## Cause

The message is printed when the device the project resolved to is a parent device that has device variants under it (RteDeviceItem::VARIANT items), so the selection is not a single concrete device. The device comes either from the device name given in the csolution file (matched against full device names in the installed packs, lines 1455-1478) or, when none is given, from the device mounted on the selected board (lines 1495-1500). Because the matched device still has variant items, the tool stops. The wording says 'multiple' but the code does not count matches. It reports that a variant must be chosen.

## Fix

Set the device in the csolution project to one of the variant full names that the tool lists right after this message (the lines starting with 'one of the following device variants must be specified:'). Use the exact full device name, for example Vendor::Device:Variant, rather than the base device name. If the device came from a board, set the device explicitly to the variant that matches your hardware, because the board's mounted device has no variant chosen.

## Trigger in the source

```cpp
if (matchedDevice->GetDeviceItemCount() > 0) {
```

## Note

The message text ('found multiple device variants') does not match the check, which only tests whether the device has variant items. The list of variants is printed by a second error on line 1509. If neither deviceItem.name nor a board mounted device is set, matchedDevice stays null and line 1503 dereferences it without a check, which may crash; this path is not confirmed from the lines given.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:1503-1511`
- `tools/projmgr/src/ProjMgrWorker.cpp:1455-1478`
- `tools/projmgr/src/ProjMgrWorker.cpp:1495-1500`
- `tools/projmgr/src/ProjMgrWorker.cpp:1506-1509`
