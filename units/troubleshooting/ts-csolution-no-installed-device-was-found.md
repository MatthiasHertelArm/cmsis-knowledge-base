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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4338"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4310", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4337"]
---

## Symptom

`no installed device was found`

## Cause

`csolution list devices` found no device in the packs it loaded: the CMSIS pack root has no device family pack (DFP), or the csolution.yml given loads only `packs:` without devices.

## Fix

Install the DFP, e.g. `cpackget add Keil::STM32U5xx_DFP`, and check CMSIS_PACK_ROOT. With a csolution.yml, add the DFP under `packs:`.

## Trigger in the source

```cpp
if (devicesSet.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4310`
- `tools/projmgr/src/ProjMgrWorker.cpp:4337`
