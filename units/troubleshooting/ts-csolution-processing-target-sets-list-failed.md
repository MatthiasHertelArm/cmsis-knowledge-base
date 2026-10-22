---
id: "ts-csolution-processing-target-sets-list-failed"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: processing target-sets list failed"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["processing target-sets list failed"]
symptom_regex: "^processing target\\-sets list failed$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:926"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "Raised by RunListTargetSets when the csolution list target-sets command fails in ListTargetSets."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:925-928", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:919-924"]
---

## Symptom

`processing target-sets list failed`

## Cause

Raised by RunListTargetSets when the csolution list target-sets command fails in ListTargetSets. The message itself is emitted only after PopulateContexts succeeded, so the failure comes from the target-set listing step, not from parsing the input files. The source lines shown do not reveal which inner condition makes ListTargetSets return false.

## Fix

The source lines given do not show a specific user-side remedy. Check the csolution output printed just before this message for the underlying error, and check that the --filter value, if used, matches a target-set name. Re-run the command after correcting the input the earlier errors point to.

## Trigger in the source

```cpp
if (!m_worker.ListTargetSets(targetSets, m_filter)) {
```

## Note

The README does not document this message. The trigger is clear, but the failing condition inside ProjMgrWorker::ListTargetSets was not among the lines provided, so the cause is inferred from the call site. The same pattern of message is used for the contexts list (line 910) and the examples and templates lists (via RunListCommand).

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:925-928`
- `tools/projmgr/src/ProjMgr.cpp:919-924`
