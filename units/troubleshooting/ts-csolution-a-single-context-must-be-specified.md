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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5103"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "`csolution run -g <generator>` for a generator defined in a pack (not a globally registered one) ran with more than one selected context, e.g. no `-c` option in a solution with several build or target types."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5101-5105", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:1042-1066", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:3545-3565"]
---

## Symptom

`a single context must be specified`

## Cause

`csolution run -g <generator>` for a generator defined in a pack (not a globally registered one) ran with more than one selected context, e.g. no `-c` option in a solution with several build or target types. The pack generator runs for exactly one context.

## Fix

Select one context with `-c`, e.g. `csolution run <name>.csolution.yml -g <generator-id> -c <project>.Debug+<target>`; `csolution list contexts <name>.csolution.yml` shows the names.

## Trigger in the source

```cpp
if (m_selectedContexts.size() != 1) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:5101-5105`
- `tools/projmgr/src/ProjMgr.cpp:1042-1066`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:3545-3565`
