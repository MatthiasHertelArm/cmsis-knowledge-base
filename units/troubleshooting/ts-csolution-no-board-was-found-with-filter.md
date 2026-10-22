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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:4301"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The user asked csolution to list boards with a filter (the list-boards command takes a filter argument) and none of the installed boards matched it."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4297-4302", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4276-4289"]
---

## Symptom

`no board was found with filter '<…>'`

## Cause

The user asked csolution to list boards with a filter (the list-boards command takes a filter argument) and none of the installed boards matched it. ListBoards collects every board from the selected contexts' filtered models, formats each as Vendor::Name[:Revision] (Pack), applies the filter terms to that list, and reports this error when nothing is left. The '<…>' in the message is the filter string the user passed.

## Fix

Run the list command without a filter to see the exact board names and vendor strings that are installed, then retry with a term that matches one of them. Install the pack that provides the board if it is missing, for example with cpackget. Check that the context or target selection is the one that holds the board, since only selected contexts are searched.

## Trigger in the source

```cpp
if (matchedBoards.empty()) {
```

## Note

The README does not document this message. The cause and fix are read from ListBoards; the exact filter syntax is handled by RteUtils::ApplyFilter, which is not in the lines given. The sibling message for devices at line 4346 has the same structure.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4297-4302`
- `tools/projmgr/src/ProjMgrWorker.cpp:4276-4289`
