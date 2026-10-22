---
id: "ts-csolution-no-target-set-was-found-with-filter"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no target-set was found with filter '…'"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no target-set was found with filter '<…>'"]
symptom_regex: "^no target\\-set was found with filter '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:4869"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "`csolution list target-sets` (or `list targets`) with `-f <words>` found no `<target-type>[@<set>]` entry from `target-types:` - `target-set:` in the csolution.yml that contains all the filter words; `<…>` is the filter."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4856", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4868", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:7471"]
---

## Symptom

`no target-set was found with filter '<…>'`

## Cause

`csolution list target-sets` (or `list targets`) with `-f <words>` found no `<target-type>[@<set>]` entry from `target-types:` - `target-set:` in the csolution.yml that contains all the filter words; `<…>` is the filter. A target type without `target-set:` entries is not listed.

## Fix

Use part of an existing target-type or set name in the filter, or run without `-f` to see the target sets the csolution.yml defines.

## Trigger in the source

```cpp
if (filteredTargetSets.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4856`
- `tools/projmgr/src/ProjMgrWorker.cpp:4868`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:7471`
