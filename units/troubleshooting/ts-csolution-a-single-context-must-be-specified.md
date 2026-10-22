---
id: "ts-csolution-a-single-context-must-be-specified"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: a single context must be specified"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["a single context must be specified"]
symptom_regex: "^a single context must be specified$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:5103"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution generator command (ExecuteGenerator) runs on exactly one selected context, but the number of selected contexts is not one."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5102-5103", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5106-5107"]
---

## Symptom

`a single context must be specified`

## Cause

The csolution generator command (ExecuteGenerator) runs on exactly one selected context, but the number of selected contexts is not one. The selection comes from the command line; when no context or more than one context is given, the size check at line 5102 fails and the tool stops before processing any context.

## Fix

Run the generator command with exactly one context, naming the project as a single context such as <project>+<target-type> (for example, a context in the form project.Debug+Target), and do not pass several contexts or omit the context argument.

## Trigger in the source

```cpp
if (m_selectedContexts.size() != 1) {
```

## Note

The exact accepted context syntax is inferred from the context-name usage in m_contexts; the source lines given do not show the command-line parsing that fills m_selectedContexts. The message is printed with no error code.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:5102-5103`
- `tools/projmgr/src/ProjMgrWorker.cpp:5106-5107`
