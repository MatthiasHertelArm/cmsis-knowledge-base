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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:3854"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "During group processing, AddFile compares each file already collected into the destination list against the file of the new source node, and fails when the same path string is found."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3852-3856", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3819-3848", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3828-3832"]
---

## Symptom

`conflict: file '<…>' is declared multiple times`

## Cause

During group processing, AddFile compares each file already collected into the destination list against the file of the new source node, and fails when the same path string is found. This happens when the same file entry (after the file's path is stored as written in the csolution or cproject input) appears more than once within one group or across the files of the same group scope, for example the same source listed twice in a group's files or in both a group and a layer that contribute to the same group. The file name printed is the one already present in the list.

## Fix

Open the csolution or project file that lists the file and remove the duplicate entry, keeping it in only one group, or put it under a single group with a for-compiler or context filter so only one copy applies. Then run the build again.

## Trigger in the source

```cpp
if (dstNode.file == src.file) {
```

## Note

The comparison is on the raw file string, so the same file written with different relative paths would not be flagged; the message is raised only for identical strings. The README does not document this message. The message reads 'file' but the check is in AddFile, which also handles file lists for groups.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:3852-3856`
- `tools/projmgr/src/ProjMgrWorker.cpp:3819-3848`
- `tools/projmgr/src/ProjMgrWorker.cpp:3828-3832`
