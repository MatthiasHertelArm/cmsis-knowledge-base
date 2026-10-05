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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlEmitter.cpp:61"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlEmitter.cpp:55-63", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrGeneratorUnitTests.cpp:106-125"]
---

## Symptom

`destination directory cannot be created`

## Cause

csolution cannot create the folder for a YAML file it writes (cbuild-idx.yml, cbuild.yml, cbuild-pack.yml, cbuild-run.yml, cbuild-gen.yml and similar), e.g. because a plain file exists where a folder of the path is needed or the location is not writable. The message is prefixed with the file path.

## Fix

Remove or rename the file that blocks the path (e.g. a file named `tmp` or `out` in the solution folder), make the location writable, or choose another output folder with `--output`/`-o` or output-dirs:.

## Trigger in the source

```cpp
if (!RteFsUtils::MakeSureFilePath(filename)) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlEmitter.cpp:55-63`
- `tools/projmgr/test/src/ProjMgrGeneratorUnitTests.cpp:106-125`
