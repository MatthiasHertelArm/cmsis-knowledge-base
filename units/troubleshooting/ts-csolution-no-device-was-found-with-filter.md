---
id: "ts-csolution-no-device-was-found-with-filter"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no device was found with filter '…'"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no device was found with filter '<…>'"]
symptom_regex: "^no device was found with filter '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:4346"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution device listing (ListDevices) was run with a filter argument, and none of the installed devices (vendor::name (pack) entries built from the loaded packs) matched the filter terms."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4342-4348", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4337-4340"]
---

## Symptom

`no device was found with filter '<…>'`

## Cause

The csolution device listing (ListDevices) was run with a filter argument, and none of the installed devices (vendor::name (pack) entries built from the loaded packs) matched the filter terms. The '<…>' in the message is the filter string the user passed on the command line.

## Fix

Check the filter spelling against the listing without a filter, for example by running the same list-devices command with no filter argument and searching the output for the device name or vendor. Install the pack that provides the device if it is missing (csolution list packs or the cpackget tool can show installed packs), then rerun with a corrected filter.

## Trigger in the source

```cpp
if (matchedDevices.empty()) {
```

## Note

Message is not listed in the README. The filter is applied with RteUtils::ApplyFilter to the list of installed devices; if no packs are installed the earlier 'no installed device was found' error is printed instead.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4342-4348`
- `tools/projmgr/src/ProjMgrWorker.cpp:4337-4340`
