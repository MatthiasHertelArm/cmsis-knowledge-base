---
id: "ts-csolution-processing-target-sets-list-failed"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: processing target-sets list failed"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["processing target-sets list failed"]
symptom_regex: "^processing target\\-sets list failed$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgr.cpp:926"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "`csolution list target-sets` (or `list targets`) failed because the `-f` filter matched no target set; the line before reports `no target-set was found with filter`."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:925", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4856", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:7471"]
---

## Symptom

`processing target-sets list failed`

## Cause

`csolution list target-sets` (or `list targets`) failed because the `-f` filter matched no target set; the line before reports `no target-set was found with filter`.

## Fix

Loosen or drop `-f` so that it matches a `<target-type>[@<set>]` defined in the csolution.yml.

## Trigger in the source

```cpp
if (!m_worker.ListTargetSets(targetSets, m_filter)) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:925`
- `tools/projmgr/src/ProjMgrWorker.cpp:4856`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:7471`
