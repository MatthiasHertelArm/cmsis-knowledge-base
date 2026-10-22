---
id: "ts-csolution-executing-generator"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: executing generator '…' for context '…' failed"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["executing generator '<…>' for context '<…>' failed"]
symptom_regex: "^executing generator '.+?' for context '.+?' failed$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:5177"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "`csolution run -g <id>` started the command of a generator defined in a pack (from its `<exe>` element) for the context, and the command ended with a non-zero exit code."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5163-5180", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrLogger.cpp:72-80"]
---

## Symptom

`executing generator '<…>' for context '<…>' failed`

## Cause

`csolution run -g <id>` started the command of a generator defined in a pack (from its `<exe>` element) for the context, and the command ended with a non-zero exit code. The generator's own output is printed only with `--verbose`, as 'generator ... reported:'. The `<…>` are the generator id and the context.

## Fix

Run the same command again with `--verbose` to see what the generator reported, and fix that problem (for example a missing tool installation or invalid input); then run the generator again.

## Trigger in the source

```cpp
if (result.second) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:5163-5180`
- `tools/projmgr/src/ProjMgrLogger.cpp:72-80`
