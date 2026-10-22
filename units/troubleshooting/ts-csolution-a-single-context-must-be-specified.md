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
summary: "The csolution generator command ran with zero or more than one selected build context, while ExecuteGenerator needs exactly one."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5102-5103"]
---

## Symptom

`a single context must be specified`

## Cause

The csolution generator command ran with zero or more than one selected build context, while ExecuteGenerator needs exactly one. The check at ProjMgrWorker.cpp:5102 counts m_selectedContexts, which is filled from the context names given on the command line, so the user either passed no context or passed several.

## Fix

Run the generator command for exactly one context, naming it as a project.context pair (for example <project>+<target>), so that m_selectedContexts holds a single entry. Run it once per context if several need generating.

## Trigger in the source

```cpp
if (m_selectedContexts.size() != 1) {
```

## Note

The README does not document this message. The exact command-line form that fills m_selectedContexts is not in the lines shown, so the context-naming example in the fix is an inference from the count check.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:5102-5103`
