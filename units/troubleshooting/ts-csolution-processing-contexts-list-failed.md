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
summary: "The csolution `list contexts` command failed inside ProjMgrWorker::ListContexts after the input files were parsed successfully."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:903-912"]
---

## Symptom

`processing contexts list failed`

## Cause

The csolution `list contexts` command failed inside ProjMgrWorker::ListContexts after the input files were parsed successfully. The worker returned false, so the generic error is printed; the specific reason is reported by the worker's own log lines, not by this message. The message carries no variable parts.

## Fix

Read the lines printed before this error for the specific cause, and fix the input they point to (csolution project YAML or PDSC). Then rerun the list contexts command. The source lines given do not show a further fix for this message.

## Trigger in the source

```cpp
if (!m_worker.ListContexts(contexts, m_filter, m_ymlOrder)) {
```

## Note

The message is a wrapper around a worker failure, so it is not specific by itself. The trigger is the worker's false return, which is shown in the lines given; the cause of that failure is not in these lines. No README entry exists for this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:903-912`
