---
id: "ts-csolution-export-file-cannot-be-written"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: export file cannot be written"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["export file cannot be written"]
symptom_regex: "^export file cannot be written$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:811"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "With `--cbuildgen` and `--export <suffix>`/`-e`, csolution also writes `<context><suffix>.cprj` without fixed pack versions, and that file cannot be saved in the cprj output folder, e.g. the folder is not writable or a folder with that file name exists."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:794-815", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrGenerator.cpp:89-95"]
---

## Symptom

`export file cannot be written`

## Cause

With `--cbuildgen` and `--export <suffix>`/`-e`, csolution also writes `<context><suffix>.cprj` without fixed pack versions, and that file cannot be saved in the cprj output folder, e.g. the folder is not writable or a folder with that file name exists. The message is prefixed with the file path.

## Fix

Make the output folder writable or remove what blocks the path, or choose another output folder with `--output`/`-o`.

## Trigger in the source

```cpp
if (m_generator.GenerateCprj(*contextItem, exportfilename, true)) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:794-815`
- `tools/projmgr/src/ProjMgrGenerator.cpp:89-95`
