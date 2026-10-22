---
id: "ts-csolution-multiple-cdefault-files-were-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: multiple cdefault files were found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["multiple cdefault files were found"]
symptom_regex: "^multiple cdefault files were found$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:1164"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "GetCdefaultFile searches the project root directory and, if set, the compiler root for files matching cdefault.yml or cdefault.yaml."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:1156-1166", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:1162-1164"]
---

## Symptom

`multiple cdefault files were found`

## Cause

GetCdefaultFile searches the project root directory and, if set, the compiler root for files matching cdefault.yml or cdefault.yaml. The message is printed when RteFsUtils::FindFileRegEx returns false but has already filled cdefaultFile with a path, which indicates that more than one matching cdefault file was found. The printed path is the value stored in cdefaultFile, so it names one of the matching files.

## Fix

Keep exactly one cdefault.yml (or cdefault.yaml) in the search locations. Check the project root directory and the compiler root (the toolchain directory reported by the tool) for extra copies, and remove or rename the duplicates. Then run the csolution command again.

## Trigger in the source

```cpp
if (!cdefaultFile.empty()) {
```

## Note

The behaviour of FindFileRegEx when it returns false is not in the lines given, so the reading that a duplicate match is the cause is inferred from the message text and the call. The third argument is a file path, so the message reports a path, not the name of a directory. The search covers the compiler root as well as the project directory, so a stray cdefault file in the toolchain tree can also trigger it.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:1156-1166`
- `tools/projmgr/src/ProjMgr.cpp:1162-1164`
