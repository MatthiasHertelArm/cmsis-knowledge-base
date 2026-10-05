---
id: "ts-csolution-malformed-access-sequence"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: malformed access sequence: '…"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["malformed access sequence: '<…>"]
symptom_regex: "^malformed access sequence: '.+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3722"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A path or value in the YAML (for example under `add-path:`, `define:`, `misc:`, `output-dirs:`, `linker:`, a debugger or image file, or a generator path) contains a `$` that opens an access sequence but has no closing `$`."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3720", "Open-CMSIS-Pack/devtools@30f5e817:libs/rteutils/src/RteUtils.cpp:600"]
---

## Symptom

`malformed access sequence: '<…>`

## Cause

A path or value in the YAML (for example under `add-path:`, `define:`, `misc:`, `output-dirs:`, `linker:`, a debugger or image file, or a generator path) contains a `$` that opens an access sequence but has no closing `$`. `<…>` is the whole value after variables were expanded.

## Fix

Close the access sequence, e.g. `$OutDir(project)$` or `$SolutionDir()$`, or remove the stray `$`.

## Trigger in the source

```cpp
if (!RteUtils::GetAccessSequence(offset, input, sequence, '$', '$')) {
```

## Note

No test produces this message; the MLOps test commented as 'malformed access sequence' (ProjMgrUnitTests.cpp:8025) uses `$BadVar$`, which is closed and leads to 'unknown access sequence' instead.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:3720`
- `libs/rteutils/src/RteUtils.cpp:600`
