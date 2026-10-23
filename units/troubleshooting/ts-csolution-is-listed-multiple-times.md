---
id: "ts-csolution-is-listed-multiple-times"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: conflict: component '…' is listed multiple times"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["conflict: component '<…>' is listed multiple times"]
symptom_regex: "^conflict: component '.+?' is listed multiple times$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:3909"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The same `component:` string appears more than once under components: of the cproject.yml for the same context (entries are compared as written, after for-context:/not-for-context: filtering)."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3900-3914", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3611-3619", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:7871-7885", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestSolution/DuplicateComponents/Cproject/duplicateComponents_cproject.cproject.yml"]
---

## Symptom

`conflict: component '<…>' is listed multiple times`

## Cause

The same `component:` string appears more than once under components: of the cproject.yml for the same context (entries are compared as written, after for-context:/not-for-context: filtering). The same duplicate coming from a clayer.yml only gives the warning 'ignoring conflict'.

## Fix

Delete the duplicate entry, or give the entries disjoint `for-context:` filters if they belong to different build or target types.

## Trigger in the source

```cpp
if (ignoreDuplicates) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:3900-3914`
- `tools/projmgr/src/ProjMgrWorker.cpp:3611-3619`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:7871-7885`
- `tools/projmgr/test/data/TestSolution/DuplicateComponents/Cproject/duplicateComponents_cproject.cproject.yml`
