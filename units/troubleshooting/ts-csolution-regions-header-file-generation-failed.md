---
id: "ts-csolution-regions-header-file-generation-failed"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: regions header file generation failed"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["regions header file generation failed"]
symptom_regex: "^regions header file generation failed$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:2336"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "csolution tried to generate the memory regions header `regions_<board or device>.h` in the project's RTE device folder, either for a default linker script template or because `linker:` - `regions:` names a file that does not exist, and could not."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2332", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2302", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteTarget.cpp:1931", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteTarget.cpp:1799", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrWorkerUnitTests.cpp:1566"]
---

## Symptom

`regions header file generation failed`

## Cause

csolution tried to generate the memory regions header `regions_<board or device>.h` in the project's RTE device folder, either for a default linker script template or because `linker:` - `regions:` names a file that does not exist, and could not. The header is built from the device memories of the DFP (and BSP); it fails when the target has no resolved device or the file cannot be written.

## Fix

Make sure the device or board resolves (its DFP is installed and listed under `packs:`) and that the RTE folder is writable. Alternatively provide the regions file yourself and name it in `linker:` - `regions:`.

## Trigger in the source

```cpp
if (!context.rteActiveTarget->GenerateRegionsHeader(rteFolder + "/")) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:2332`
- `tools/projmgr/src/ProjMgrWorker.cpp:2302`
- `libs/rtemodel/src/RteTarget.cpp:1931`
- `libs/rtemodel/src/RteTarget.cpp:1799`
- `tools/projmgr/test/src/ProjMgrWorkerUnitTests.cpp:1566`
