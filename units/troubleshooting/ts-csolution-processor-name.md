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
summary: "The processor part of `device:` (after the colon, as in `device: <Device>:<Pname>` or `device: :<Pname>`) names a processor that the selected device does not have; `<…>` is that name."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1513", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:774", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestSolution/test_no_device_name.csolution.yml:6", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:3085"]
---

## Symptom

`processor name '<…>' was not found`

## Cause

The processor part of `device:` (after the colon, as in `device: <Device>:<Pname>` or `device: :<Pname>`) names a processor that the selected device does not have; `<…>` is that name. Single-core devices usually have no processor name at all.

## Fix

Use a processor name of the device as listed by `csolution list devices` (`Vendor::Device:Pname`), or drop the `:<Pname>` part for a single-core device.

## Trigger in the source

```cpp
if (!deviceItem.pname.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:1513`
- `tools/projmgr/src/ProjMgrWorker.cpp:774`
- `tools/projmgr/test/data/TestSolution/test_no_device_name.csolution.yml:6`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:3085`
