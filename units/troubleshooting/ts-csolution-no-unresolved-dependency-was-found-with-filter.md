---
id: "ts-csolution-no-unresolved-dependency-was-found-with-filter"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no unresolved dependency was found with filter '…'"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no unresolved dependency was found with filter '<…>'"]
symptom_regex: "^no unresolved dependency was found with filter '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:4509"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The message is printed when a filter was given and RteUtils::ApplyFilter removes every entry from the list."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4505-4511", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4540-4546"]
---

## Symptom

`no unresolved dependency was found with filter '<…>'`

## Cause

The message is printed when a filter was given and RteUtils::ApplyFilter removes every entry from the list. In ListConfigs the list holds the file instances of the active target (configuration files), so the filter pattern matches none of them. The same text is printed in ListDependencies when no unresolved dependency matches, so the wording may come from that function rather than describe what ListConfigs filtered.

## Fix

Run the command without the filter to see the full list, then retry with a filter pattern that matches an entry shown in that list. Check the pattern for typos and for characters the filter syntax treats specially. The source does not show the exact filter syntax, so confirm it in the csolution help.

## Trigger in the source

```cpp
if (filteredConfigs.empty()) {
```

## Note

The text says 'unresolved dependency' but the printing function ListConfigs filters configuration files, not dependencies; the message looks copied from ListDependencies (line 4544), so the wording may mislead users. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4505-4511`
- `tools/projmgr/src/ProjMgrWorker.cpp:4540-4546`
