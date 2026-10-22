---
id: "ts-csolution-file-cannot-be-written"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: file cannot be written"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["file cannot be written"]
symptom_regex: "^file cannot be written$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:802"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "csolution cannot save an output file whose path prefixes the message, e.g. a folder with the same name exists at that path or the location is not writable."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:794-804", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlEmitter.cpp:39-44", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlEmitter.cpp:64-67", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:1075-1093"]
---

## Symptom

`file cannot be written`

## Cause

csolution cannot save an output file whose path prefixes the message, e.g. a folder with the same name exists at that path or the location is not writable. From ProjMgr.cpp:802 it is the legacy `<context>.cprj` written with `--cbuildgen`; the same text is printed for YAML outputs such as *.cbuild.yml.

## Fix

Remove the folder or file that blocks the path, make the output location writable, or choose another output folder with `--output`/`-o`.

## Trigger in the source

```cpp
if (m_generator.GenerateCprj(*contextItem, filename)) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:794-804`
- `tools/projmgr/src/ProjMgrYamlEmitter.cpp:39-44`
- `tools/projmgr/src/ProjMgrYamlEmitter.cpp:64-67`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:1075-1093`
