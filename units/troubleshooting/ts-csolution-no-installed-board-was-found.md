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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:4293"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "ListBoards loads the packs for each selected context, then collects every board in that context's filtered RTE model."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4276-4293", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4283-4284", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4292-4293"]
---

## Symptom

`no installed board was found`

## Cause

ListBoards loads the packs for each selected context, then collects every board in that context's filtered RTE model. The message is printed when that collection is empty across all selected contexts, so no board from the installed packs matched the selected contexts. The check runs after LoadPacks has succeeded, so the packs were read but none supplied a board.

## Fix

Install a pack that provides boards (for example a Device or BSP pack with board definitions) into the CMSIS pack root, then run the board listing again. Check that the contexts selected for the command are the ones whose packs supply boards. If a pack is already installed, confirm that its PDSC lists boards and that the project's pack selection does not exclude it.

## Trigger in the source

```cpp
if (boardsSet.empty()) {
```

## Note

The message says 'installed' but the check is on the filtered model of the selected contexts, not on the pack root, so a board can be missing because of context selection or filtering rather than a missing installation. The README does not document this message. The fix is my reading of the code path, not a documented procedure.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4276-4293`
- `tools/projmgr/src/ProjMgrWorker.cpp:4283-4284`
- `tools/projmgr/src/ProjMgrWorker.cpp:4292-4293`
