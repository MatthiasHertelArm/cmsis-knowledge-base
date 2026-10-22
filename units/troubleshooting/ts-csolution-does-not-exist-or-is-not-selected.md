---
id: "ts-csolution-does-not-exist-or-is-not-selected"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: context '…' referenced by access sequence '…' does not exist or is not selected"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["context '<…>' referenced by access sequence '<…>' does not exist or is not selected"]
symptom_regex: "^context '.+?' referenced by access sequence '.+?' does not exist or is not selected$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:3777"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "An access sequence such as $Dname(contextName)$ in a csolution file names a context (project or build context) that FindReferencedContext cannot resolve among the selected contexts."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3753-3756", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3775-3779"]
---

## Symptom

`context '<…>' referenced by access sequence '<…>' does not exist or is not selected`

## Cause

An access sequence such as $Dname(contextName)$ in a csolution file names a context (project or build context) that FindReferencedContext cannot resolve among the selected contexts. The context name in the message is the referenced name as written in the sequence, and the sequence name is the access sequence that refers to it. Either the name is misspelled or partial, or the referenced context is not part of the solution's selected contexts (for example, it is not listed in the solution or is filtered out by the selected build types or target types).

## Fix

Check the context name inside the access sequence against the project and build type names in the csolution file, and correct any typo or partial name. Make sure the referenced context is listed in the solution and is selected by the build type, target type or other selection in use, so that it is part of the selected contexts. Then run the csolution command again.

## Trigger in the source

```cpp
if (genDep && refContext.name != context.name) {
```

## Note

The message is printed only when FindReferencedContext returns an empty name. The exact matching rules of FindReferencedContext are not in the lines given, so the cause of 'not selected' is inferred from the name lookup against m_selectedContexts. At solution level a separate message ('is not compatible') is printed earlier when no context name contains the referenced name at all, at line 3746.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:3753-3756`
- `tools/projmgr/src/ProjMgrWorker.cpp:3775-3779`
