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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:5231"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution command line combined the target-set option '-a' with '-S' (the cbuild-set selection path)."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5230-5233", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5234-5238"]
---

## Symptom

`invalid arguments: '-a' option cannot be used in combination with '-S'`

## Cause

The csolution command line combined the target-set option '-a' with '-S' (the cbuild-set selection path). ParseContextSelection checks the cbuild-set flag first and rejects the call whenever a target type was given with '-a' (m_activeTargetType is non-empty), so the two options cannot be used together.

## Fix

Run csolution with either '-a' (to select a target type and its contexts) or '-S' (to process the contexts stored in the cbuild-set file), but not both in the same invocation. If you want the cbuild-set contexts, drop '-a'; if you want the target-set contexts, drop '-S'.

## Trigger in the source

```cpp
if (checkCbuildSet && !m_activeTargetType.empty()) {
```

## Note

The message text is not in the README. The check is the first branch, so '-a' with '-S' fails before any context is parsed. The fix relies on the else-if ordering shown in the lines given; the meaning of each flag is inferred from the branch bodies.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:5230-5233`
- `tools/projmgr/src/ProjMgrWorker.cpp:5234-5238`
