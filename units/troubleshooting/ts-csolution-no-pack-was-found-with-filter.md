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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:4267"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution pack listing (the list-packs command with a filter argument) builds one entry per installed pack, formatted as the pack ID plus its .pdsc path, or as the locked/available-update text when locked packs are shown."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4263-4269", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4244-4262"]
---

## Symptom

`no pack was found with filter '<…>'`

## Cause

The csolution pack listing (the list-packs command with a filter argument) builds one entry per installed pack, formatted as the pack ID plus its .pdsc path, or as the locked/available-update text when locked packs are shown. The user's filter string is split into terms and applied to these entries; when no entry matches any term, the message is printed with the filter text in place of '<…>' and the command fails. So the filter did not match any installed pack ID or pack path, or no packs were loaded at all.

## Fix

Run the same command without a filter to list the installed packs and their IDs, then retry with a filter term that matches a part of an ID or path shown there. If the expected pack is missing from that list, install it (for example with cpackget) or check the pack root and the pack selection used for loading.

## Trigger in the source

```cpp
if (filteredPacks.empty()) {
```

## Note

The README does not document this message. The exact matching rule is in RteUtils::ApplyFilter, which is not in the lines given, so the cause describes the matched text only as far as the lines show. The sibling message for boards uses the same pattern at ProjMgrWorker.cpp:4300-4301.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4263-4269`
- `tools/projmgr/src/ProjMgrWorker.cpp:4244-4262`
