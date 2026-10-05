---
id: "ts-csolution-invalid-arguments-a-option-cannot-be-used-in-com"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: invalid arguments: '-a' option cannot be used in combination with '-S'"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["invalid arguments: '-a' option cannot be used in combination with '-S'"]
symptom_regex: "^invalid arguments: '\\-a' option cannot be used in combination with '\\-S'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5231"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5224", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5230", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:175", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:168", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:7672"]
---

## Symptom

`invalid arguments: '-a' option cannot be used in combination with '-S'`

## Cause

The command line contains both `-a`/`--active` (select a target-type and target-set) and `-S`/`--context-set` (take the context selection from the <solution>.cbuild-set.yml). Both select the contexts to process, so csolution rejects the combination.

## Fix

Use only one of them: `-a <target-type>[@<target-set>]` to select by target, or `-S` to reuse the selection stored in the cbuild-set.yml.

## Trigger in the source

```cpp
if (checkCbuildSet && !m_activeTargetType.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:5224`
- `tools/projmgr/src/ProjMgrWorker.cpp:5230`
- `tools/projmgr/src/ProjMgr.cpp:175`
- `tools/projmgr/src/ProjMgr.cpp:168`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:7672`
