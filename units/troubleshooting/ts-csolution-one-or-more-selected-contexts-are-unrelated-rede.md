---
id: "ts-csolution-one-or-more-selected-contexts-are-unrelated-rede"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: one or more selected contexts are unrelated, redefine the '--context arg [...]' option"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["one or more selected contexts are unrelated, redefine the '--context arg [...]' option"]
symptom_regex: "^one or more selected contexts are unrelated, redefine the '\\-\\-context arg \\[\\.\\.\\.\\]' option$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:5870"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "When a generator is executed for the selected contexts, the tool collects the project names of all sibling contexts that share the selected context's device, processor and project type (ProcessGlobalGenerators)."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5859-5873", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5818", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5840-5844"]
---

## Symptom

`one or more selected contexts are unrelated, redefine the '--context arg [...]' option`

## Cause

When a generator is executed for the selected contexts, the tool collects the project names of all sibling contexts that share the selected context's device, processor and project type (ProcessGlobalGenerators). It then checks each context named in the --context argument; if a selected context's project name is not among those siblings, it stops with this error. The selected contexts therefore belong to projects that are not part of the same generator group, for example contexts from different projects mixed in one --context list.

## Fix

Run the generator again with a --context list whose entries all belong to the same project and to the same device/processor group as the first selected context, so that every named context is a sibling of it. Check the context names given to --context against the projects in the csolution file.

## Trigger in the source

```cpp
if (find(siblingProjects.begin(), siblingProjects.end(), selectedContextItem->cproject->name) == siblingProjects.end()) {
```

## Note

The message is not documented in the README. The grouping rule is read from ProcessGlobalGenerators; the exact user-facing meaning of 'related' is my interpretation of that code. The message text says 'redefine the --context arg [...] option', so the fix follows that wording.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:5859-5873`
- `tools/projmgr/src/ProjMgrWorker.cpp:5818`
- `tools/projmgr/src/ProjMgrWorker.cpp:5840-5844`
