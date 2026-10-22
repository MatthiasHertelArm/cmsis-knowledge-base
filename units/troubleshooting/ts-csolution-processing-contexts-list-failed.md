---
id: "ts-csolution-processing-contexts-list-failed"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: processing contexts list failed"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["processing contexts list failed"]
symptom_regex: "^processing contexts list failed$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:910"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "`csolution list contexts` could not produce a list: a `-f` filter matched no context (the line before reports `no context was found with filter`), or the solution yielded no contexts at all."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:909", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4834"]
---

## Symptom

`processing contexts list failed`

## Cause

`csolution list contexts` could not produce a list: a `-f` filter matched no context (the line before reports `no context was found with filter`), or the solution yielded no contexts at all.

## Fix

Fix the error printed before it; drop or loosen `-f`, and check that the csolution.yml has `projects:` and `target-types:`.

## Trigger in the source

```cpp
if (!m_worker.ListContexts(contexts, m_filter, m_ymlOrder)) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:909`
- `tools/projmgr/src/ProjMgrWorker.cpp:4834`
