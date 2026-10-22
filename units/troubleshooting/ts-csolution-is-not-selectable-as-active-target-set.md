---
id: "ts-csolution-is-not-selectable-as-active-target-set"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: '…' is not selectable as active target-set"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["'<…>' is not selectable as active target-set"]
symptom_regex: "^'.+?' is not selectable as active target\\-set$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:6321"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The value of `--active`/`-a` (`<target-type>[@<target-set>]`) does not match the csolution.yml: no entry under target-types: has that `type:` name, or that type has no target-set: entry whose `set:` equals the part after `@`."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:6288-6324", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:7659-7669"]
---

## Symptom

`'<…>' is not selectable as active target-set`

## Cause

The value of `--active`/`-a` (`<target-type>[@<target-set>]`) does not match the csolution.yml: no entry under target-types: has that `type:` name, or that type has no target-set: entry whose `set:` equals the part after `@`. The `<…>` is the value as given.

## Fix

List the valid values with `csolution list target-sets <name>.csolution.yml` and pass one of them, e.g. `-a CM0` or `-a CM0@Production`; or add the set to the target type (`target-set: - set: Production`). Names are case-sensitive.

## Trigger in the source

```cpp
if (m_activeTargetType.empty() || (!targetSetFound && !targetSet.empty())) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:6288-6324`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:7659-7669`
