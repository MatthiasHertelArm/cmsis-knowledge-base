---
id: "ts-csolution-processing-context"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: processing context '…' failed"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["processing context '<…>' failed"]
symptom_regex: "^processing context '.+?' failed$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:743"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution tool prints this as a summary when ProcessContext returns false for one build context (the '<…>' part is the context name, such as project+target)."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:739-743", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:744-745"]
---

## Symptom

`processing context '<…>' failed`

## Cause

The csolution tool prints this as a summary when ProcessContext returns false for one build context (the '<…>' part is the context name, such as project+target). ProcessContext is the step that resolves that context's inputs, and the specific failure is logged by it or by the functions it calls before this line runs. This message only reports that the context as a whole failed, so it does not name the underlying problem.

## Fix

Read the error or warning lines printed just before this message for the same context name and fix those first, for example a missing or invalid component, pack, file or csolution.yml entry. Then rerun the csolution command. If no earlier error for that context appears in the log, rerun with verbose output to surface the reason.

## Trigger in the source

```cpp
if (!m_worker.ProcessContext(contextItem, true, true, false)) {
```

## Note

The triggering error is generic, and the real cause is printed by ProcessContext or its callees, which are not in the lines given. The Code field is empty. The message is printed with contextName as the second argument, so the context is also identified in the log entry itself.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:739-743`
- `tools/projmgr/src/ProjMgr.cpp:744-745`
