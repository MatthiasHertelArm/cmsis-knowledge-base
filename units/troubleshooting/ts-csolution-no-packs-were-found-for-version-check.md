---
id: "ts-csolution-no-packs-were-found-for-version-check"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no packs were found for version check"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no packs were found for version check"]
symptom_regex: "^no packs were found for version check$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:6202"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "`csolution check pack-updates` loaded no pack for the selected contexts, so there is nothing to compare with the pack index."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:6137", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:6202"]
---

## Symptom

`no packs were found for version check`

## Cause

`csolution check pack-updates` loaded no pack for the selected contexts, so there is nothing to compare with the pack index. That happens when the pack root has no installed packs and the solution names no pack with a local `path:`.

## Fix

Install the packs the solution needs (`cpackget add <Vendor>::<Pack>` or `csolution list packs -m my.csolution.yml` to see the missing ones) and check CMSIS_PACK_ROOT, then run the check again.

## Trigger in the source

```cpp
if (checkPackResults.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:6137`
- `tools/projmgr/src/ProjMgrWorker.cpp:6202`
