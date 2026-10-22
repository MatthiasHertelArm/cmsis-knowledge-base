---
id: "ts-csolution-was-not-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: board '…' was not found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["board '<…>' was not found"]
symptom_regex: "^board '.+?' was not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:1372"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The board named in the project's board field (the context.board string, which GetBoardItem splits into name, vendor and revision) matches no board in the filtered model's board list."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1357-1374", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1362-1372"]
---

## Symptom

`board '<…>' was not found`

## Cause

The board named in the project's board field (the context.board string, which GetBoardItem splits into name, vendor and revision) matches no board in the filtered model's board list. The tool keeps only boards whose name equals the parsed name exactly and, when a vendor was given, whose vendor string also equals it. If nothing passes both checks, it prints this error and fails the context. The board list comes from the packs the tool has loaded, so a board from a pack that is not available to the project also produces this message.

## Fix

Check the board name and vendor in the csolution board entry against the board's name and vendor as listed in the board pack's PDSC. Remove or correct the vendor part if it does not match exactly. Make sure the pack that provides the board is installed and reachable for the project, for example by listing it under its dependencies in the .csolution.yml or .cproject.yml file. Then run the build again.

## Trigger in the source

```cpp
if (partialMatchedBoards.empty()) {
```

## Note

Message text is also printed at ProjMgrWorker.cpp:1396 when no board matches a given revision; that call omits the context name, and its cause is a revision mismatch, not a missing board. The filtered model's pack selection is not in the lines provided, so the pack-availability part of the cause is inferred from the code that builds the model.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:1357-1374`
- `tools/projmgr/src/ProjMgrWorker.cpp:1362-1372`
