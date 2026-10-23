---
id: "ts-csolution-is-declared-multiple-times-2"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: conflict: file '…' is declared multiple times"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["conflict: file '<…>' is declared multiple times"]
symptom_regex: "^conflict: file '.+?' is declared multiple times$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:3854"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "Within one group of a cproject.yml, clayer.yml or *.cgen.yml, the same `file:` path is listed twice for the same context (after for-context:/not-for-context:/for-compiler: filtering)."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3850-3870", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3710-3797", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:223-233"]
---

## Symptom

`conflict: file '<…>' is declared multiple times`

## Cause

Within one group of a cproject.yml, clayer.yml or *.cgen.yml, the same `file:` path is listed twice for the same context (after for-context:/not-for-context:/for-compiler: filtering).

## Fix

Delete the duplicate `- file:` entry, or give the entries disjoint `for-context:`/`for-compiler:` filters.

## Trigger in the source

```cpp
if (dstNode.file == src.file) {
```

## Note

AddFile compares the raw path with already-rebased paths (made relative to the cbuild/cprj folder), so with the default cbuild2cmake backend real duplicates are probably not detected; no test covers this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:3850-3870`
- `tools/projmgr/src/ProjMgrWorker.cpp:3710-3797`
- `tools/projmgr/src/ProjMgrWorker.cpp:223-233`
