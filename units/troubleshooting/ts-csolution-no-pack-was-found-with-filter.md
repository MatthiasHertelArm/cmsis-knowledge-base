---
id: "ts-csolution-no-pack-was-found-with-filter"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no pack was found with filter '…'"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no pack was found with filter '<…>'"]
symptom_regex: "^no pack was found with filter '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4267"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4267", "Open-CMSIS-Pack/devtools@30f5e817:libs/rteutils/src/RteUtils.cpp:616"]
---

## Symptom

`no pack was found with filter '<…>'`

## Cause

`csolution list packs -f <words>` found packs, but none whose line (`Vendor::Pack@version` and, when shown, its path) contains all the filter words; `<…>` is the filter. Matching is case-insensitive substring matching.

## Fix

Loosen the filter (e.g. `-f CMSIS`) or run without `-f`. A pack that is not installed does not appear; install it with `cpackget add <Vendor>::<Pack>`.

## Trigger in the source

```cpp
if (filteredPacks.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4267`
- `libs/rteutils/src/RteUtils.cpp:616`
