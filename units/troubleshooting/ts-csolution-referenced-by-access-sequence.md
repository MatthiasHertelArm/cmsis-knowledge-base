---
id: "ts-csolution-referenced-by-access-sequence"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: context '…' referenced by access sequence '…' is not compatible"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["context '<…>' referenced by access sequence '<…>' is not compatible"]
symptom_regex: "^context '.+?' referenced by access sequence '.+?' is not compatible$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:3746"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A solution-level node of the csolution.yml (for example `executes:` input/output) uses an access sequence such as `$elf(unknown.Debug+Target)$` whose context argument matches no context of the solution: no context name contains the given text."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3735-3751", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:6369-6392", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestSolution/Executes/error.csolution.yml"]
---

## Symptom

`context '<…>' referenced by access sequence '<…>' is not compatible`

## Cause

A solution-level node of the csolution.yml (for example `executes:` input/output) uses an access sequence such as `$elf(unknown.Debug+Target)$` whose context argument matches no context of the solution: no context name contains the given text. Despite the wording, it means the context was not found. The `<…>` are the context text and the sequence name.

## Fix

Correct the context name in the access sequence to an existing `<project>.<build-type>+<target-type>` (see `csolution list contexts <name>.csolution.yml`).

## Trigger in the source

```cpp
if (compatibleContexts.empty()) {
```

## Note

'is not compatible' is misleading: the check is a substring match over all context names.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:3735-3751`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:6369-6392`
- `tools/projmgr/test/data/TestSolution/Executes/error.csolution.yml`
