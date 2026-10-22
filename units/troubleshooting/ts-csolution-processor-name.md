---
id: "ts-csolution-processor-name"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: processor name '…' was not found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["processor name '<…>' was not found"]
symptom_regex: "^processor name '.+?' was not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:1517"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution run resolved the device to a single matched device, but the processor name given in the device item (the pname from the project's device/processor selection) does not match any processor declared for that device in the installed pack."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1514-1518", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1519-1526"]
---

## Symptom

`processor name '<…>' was not found`

## Cause

The csolution run resolved the device to a single matched device, but the processor name given in the device item (the pname from the project's device/processor selection) does not match any processor declared for that device in the installed pack. The message quotes that requested processor name. The lookup is done by matchedDevice->GetProcessor(deviceItem.pname) and the error is raised only when a non-empty name was requested and no processor was found.

## Fix

Check the processor name you set for the device in the csolution YAML (the processor/name entry under the device) against the processors the device defines in its pack (the PDSC device entry). Correct the spelling or choose one of the processor names the device actually declares, then run csolution again. If the processor name is meant to be omitted, remove it so the tool lists the available processors instead.

## Trigger in the source

```cpp
if (!deviceItem.pname.empty()) {
```

## Note

The sibling branch for an empty pname lists the valid processors via 'one of the following processors must be specified', which is a useful hint for the user. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:1514-1518`
- `tools/projmgr/src/ProjMgrWorker.cpp:1519-1526`
