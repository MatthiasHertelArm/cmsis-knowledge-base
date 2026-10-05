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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4346"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4346", "Open-CMSIS-Pack/devtools@30f5e817:libs/rteutils/src/RteUtils.cpp:616"]
---

## Symptom

`no device was found with filter '<…>'`

## Cause

`csolution list devices -f <words>` found devices, but none whose line (`Vendor::Device[:Pname] (Vendor::Pack@version)`) contains all the filter words; `<…>` is the filter. Matching is case-insensitive substring matching and every word must match.

## Fix

Loosen the filter (e.g. `-f STM32U5`), or run without `-f`. If the device belongs to a pack that is not installed, install it with `cpackget add <Vendor>::<Pack>`.

## Trigger in the source

```cpp
if (matchedDevices.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4346`
- `libs/rteutils/src/RteUtils.cpp:616`
