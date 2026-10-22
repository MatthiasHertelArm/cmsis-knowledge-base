---
id: "ts-csolution-no-context-was-found-with-filter"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no context was found with filter '…'"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no context was found with filter '<…>'"]
symptom_regex: "^no context was found with filter '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:4843"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "ListContexts applies the user's filter string, split on commas into a set, to the project's ordered context names (m_ymlOrderedContexts) and finds none that match."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4834-4845", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4843"]
---

## Symptom

`no context was found with filter '<…>'`

## Cause

ListContexts applies the user's filter string, split on commas into a set, to the project's ordered context names (m_ymlOrderedContexts) and finds none that match. The printed text is the filter as given. The filter is matched against context names, so a misspelled name, a wrong build-type or target part, or a context that is not defined in the project's csolution or cproject files will leave the result empty. The lines shown do not reveal which command option supplies the filter.

## Fix

Re-run the same command without the filter to see the context names the project actually defines, then pass one of those names exactly as printed. Check the spelling and the separators in the filter against that list.

## Trigger in the source

```cpp
if (filteredContexts.empty()) {
```

## Note

The source lines show the filter application and the error, but not the calling command or the exact context name format. The sibling message 'no target-set was found with filter' at ProjMgrWorker.cpp:4869 follows the same pattern. Code field was empty in the input.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4834-4845`
- `tools/projmgr/src/ProjMgrWorker.cpp:4843`
