---
id: "ts-csolution-cproject-file-was-not-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: cproject file was not found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["cproject file was not found"]
symptom_regex: "^cproject file was not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:529"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution parser lists a cproject entry under `projects` in the csolution file."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:525-531", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:527"]
---

## Symptom

`cproject file was not found`

## Cause

The csolution parser lists a cproject entry under `projects` in the csolution file. For each entry, ProjMgr resolves `m_rootDir + "/" + cproject` with `fs::canonical` and ignores the error code. When the path does not exist, canonical returns an empty path, the generic string is empty, and the tool prints this error with the entry as the file argument. The reported path is the entry as written in the csolution file, not the resolved one.

## Fix

Open the csolution file and check the `projects` entry named in the message. Paths are resolved relative to the directory that contains the csolution file. Correct the path or file name so it points to an existing cproject.yml, for example `- project: ./app/app.cproject.yml` style entries as your layout requires, then run the command again.

## Trigger in the source

```cpp
if (cprojectFile.empty()) {
```

## Note

The README does not document this message. The code prints the message with the raw cproject entry, so the reported text may be a relative path that differs from the resolved location. The error code from fs::canonical is discarded, so the underlying OS reason is not shown; a missing file is the case the code is written for.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:525-531`
- `tools/projmgr/src/ProjMgr.cpp:527`
