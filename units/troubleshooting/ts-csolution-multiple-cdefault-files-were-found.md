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
summary: "The csolution.yml has `cdefault:`, and one of the folders csolution searches for the cdefault file (the solution folder first, then the compiler root, i.e."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:1154", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:496", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtefsutils/src/RteFsUtils.cpp:809"]
---

## Symptom

`multiple cdefault files were found`

## Cause

The csolution.yml has `cdefault:`, and one of the folders csolution searches for the cdefault file (the solution folder first, then the compiler root, i.e. CMSIS_COMPILER_ROOT or the toolbox's `etc` folder) contains both `cdefault.yml` and `cdefault.yaml`. The message's location is that folder.

## Fix

Keep only one of `cdefault.yml` and `cdefault.yaml` in that folder.

## Trigger in the source

```cpp
if (!cdefaultFile.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:1154`
- `tools/projmgr/src/ProjMgr.cpp:496`
- `libs/rtefsutils/src/RteFsUtils.cpp:809`
