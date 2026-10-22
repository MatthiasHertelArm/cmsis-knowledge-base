---
id: "ts-csolution-clayer-search-path-does-not-exist"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: clayer search path does not exist"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["clayer search path does not exist"]
symptom_regex: "^clayer search path does not exist$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:862"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "CollectLayersFromSearchPath is called with a non-empty clayer search path (the search path given for generic clayer discovery) and, after canonicalising it, the directory does not exist on disk."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:857-864", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:921-922"]
---

## Symptom

`clayer search path does not exist`

## Cause

CollectLayersFromSearchPath is called with a non-empty clayer search path (the search path given for generic clayer discovery) and, after canonicalising it, the directory does not exist on disk. The message is printed with the absolute, canonical path as its last argument, which is the path that was checked, so the user's search path value is missing or misspelled, or relative to a different working directory than expected.

## Fix

Check the clayer search path value that csolution was given (the search path used for generic clayer discovery) and correct it so it names an existing directory, using a path relative to the directory where csolution runs or an absolute path. Create the directory or fix the spelling, then run csolution again.

## Trigger in the source

```cpp
if (!RteFsUtils::Exists(absSearchPath)) {
```

## Note

The message is printed with the canonical path as its third argument, so the log shows where the tool looked. The source does not show how the search path reaches this function, so the exact option name is not confirmed here.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:857-864`
- `tools/projmgr/src/ProjMgrWorker.cpp:921-922`
