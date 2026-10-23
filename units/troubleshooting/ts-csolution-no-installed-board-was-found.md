---
id: "ts-csolution-no-installed-board-was-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no installed board was found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no installed board was found"]
symptom_regex: "^no installed board was found$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:4293"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "`csolution list boards` found no board in the packs it loaded: the CMSIS pack root has no pack that describes boards, or the csolution.yml given restricts loading to `packs:` that contain no boards."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4277", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4292", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:561"]
---

## Symptom

`no installed board was found`

## Cause

`csolution list boards` found no board in the packs it loaded: the CMSIS pack root has no pack that describes boards, or the csolution.yml given restricts loading to `packs:` that contain no boards.

## Fix

Install a board support pack, e.g. `cpackget add <Vendor>::<Board>_BSP`, and check that CMSIS_PACK_ROOT points to the pack root in use. With a csolution.yml, add the BSP under `packs:`.

## Trigger in the source

```cpp
if (boardsSet.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4277`
- `tools/projmgr/src/ProjMgrWorker.cpp:4292`
- `tools/projmgr/src/ProjMgrWorker.cpp:561`
