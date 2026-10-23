---
id: "ts-csolution-no-board-was-found-with-filter"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no board was found with filter '…'"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no board was found with filter '<…>'"]
symptom_regex: "^no board was found with filter '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:4301"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "`csolution list boards -f <words>` found boards, but none whose line (`Vendor::Board[:Revision] (Vendor::Pack@version)`) contains all the filter words; `<…>` is the filter."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4301", "Open-CMSIS-Pack/devtools@30f5e817:libs/rteutils/src/RteUtils.cpp:616", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:285"]
---

## Symptom

`no board was found with filter '<…>'`

## Cause

`csolution list boards -f <words>` found boards, but none whose line (`Vendor::Board[:Revision] (Vendor::Pack@version)`) contains all the filter words; `<…>` is the filter. Matching is case-insensitive substring matching, and every word must match.

## Fix

Use fewer or shorter filter words, e.g. `-f STM32` instead of a full board name, or run without `-f` to see the full list. Without a csolution.yml the list covers all installed packs; with one, only the packs the solution loads.

## Trigger in the source

```cpp
if (matchedBoards.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4301`
- `libs/rteutils/src/RteUtils.cpp:616`
- `tools/projmgr/src/ProjMgr.cpp:285`
