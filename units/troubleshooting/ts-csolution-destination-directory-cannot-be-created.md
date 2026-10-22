---
id: "ts-csolution-destination-directory-cannot-be-created"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: destination directory cannot be created"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["destination directory cannot be created"]
symptom_regex: "^destination directory cannot be created$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrYamlEmitter.cpp:61"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "csolution is about to write a generated YAML file (for example a generated .cbuild or .cprj style output) to the given path and the file content differs from what is on disk, so updating is allowed."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlEmitter.cpp:60-63", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlEmitter.cpp:55-58"]
---

## Symptom

`destination directory cannot be created`

## Cause

csolution is about to write a generated YAML file (for example a generated .cbuild or .cprj style output) to the given path and the file content differs from what is on disk, so updating is allowed. Before writing, it calls RteFsUtils::MakeSureFilePath on the target path to create its parent directories, and that call failed. The path in the message is the generated file whose parent directory could not be created, typically because a path component exists as a regular file, or the location is not writable.

## Fix

Check the output location shown in the message: make sure no file exists where one of its parent directories should be, and that the parent directory is writable by the user running csolution. Remove or rename the conflicting file or fix the permissions, then rerun the build. The source gives no further workaround.

## Trigger in the source

```cpp
if (!RteFsUtils::MakeSureFilePath(filename)) {
```

## Note

Not documented in the README. The cause for the failure of MakeSureFilePath is inferred from its name and call site; the body of RteFsUtils::MakeSureFilePath was not among the lines provided.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlEmitter.cpp:60-63`
- `tools/projmgr/src/ProjMgrYamlEmitter.cpp:55-58`
