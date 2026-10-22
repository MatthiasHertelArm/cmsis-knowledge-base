---
id: "ts-csolution-no-installed-component-was-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no installed component was found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no installed component was found"]
symptom_regex: "^no installed component was found$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:4466"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "`csolution list components` without a solution context found no software component in the installed packs, which usually means the CMSIS pack root is empty or holds no pack with components."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4463", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4466"]
---

## Symptom

`no installed component was found`

## Cause

`csolution list components` without a solution context found no software component in the installed packs, which usually means the CMSIS pack root is empty or holds no pack with components.

## Fix

Install packs with cpackget (for example `cpackget add ARM::CMSIS`) and check that CMSIS_PACK_ROOT points to that pack root. To list components for a device, pass the csolution.yml.

## Trigger in the source

```cpp
if (!selectedContext.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4463`
- `tools/projmgr/src/ProjMgrWorker.cpp:4466`
