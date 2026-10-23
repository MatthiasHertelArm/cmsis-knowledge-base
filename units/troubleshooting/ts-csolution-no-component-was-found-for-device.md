---
id: "ts-csolution-no-component-was-found-for-device"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no component was found for device '…'"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no component was found for device '<…>'"]
symptom_regex: "^no component was found for device '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:4463"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "`csolution list components` with a csolution.yml found no software component in the loaded packs that applies to the context's device; `<…>` is the device."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4463", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4449"]
---

## Symptom

`no component was found for device '<…>'`

## Cause

`csolution list components` with a csolution.yml found no software component in the loaded packs that applies to the context's device; `<…>` is the device. Typically the solution's `packs:` list contains only packs whose components do not match that device, or the device pack has no components.

## Fix

Add the packs that provide components for the device under `packs:` in the csolution.yml (for example the DFP and `- pack: ARM::CMSIS`), install them with cpackget, and run the command again.

## Trigger in the source

```cpp
if (!selectedContext.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4463`
- `tools/projmgr/src/ProjMgrWorker.cpp:4449`
