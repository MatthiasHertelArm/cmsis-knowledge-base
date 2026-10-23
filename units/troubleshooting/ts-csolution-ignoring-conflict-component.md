---
id: "ts-csolution-ignoring-conflict-component"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: ignoring conflict: component '…' is listed multiple times"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["ignoring conflict: component '<…>' is listed multiple times"]
symptom_regex: "^ignoring conflict: component '.+?' is listed multiple times$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:3906"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A component that is already listed for the context (in the cproject.yml or an earlier processed clayer.yml) is listed again in a clayer.yml. csolution keeps the first entry and drops the layer's duplicate, including any settings on it (define:, …"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3900-3914", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3621-3633", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:7887-7891", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestSolution/DuplicateComponents/Clayer/duplicateComponents.clayer.yml"]
---

## Symptom

`ignoring conflict: component '<…>' is listed multiple times`

## Cause

A component that is already listed for the context (in the cproject.yml or an earlier processed clayer.yml) is listed again in a clayer.yml. csolution keeps the first entry and drops the layer's duplicate, including any settings on it (define:, misc:, instances: and so on).

## Fix

Remove the duplicate from either the project or the layer, keeping the entry whose settings should apply.

## Trigger in the source

```cpp
if (ignoreDuplicates) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:3900-3914`
- `tools/projmgr/src/ProjMgrWorker.cpp:3621-3633`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:7887-7891`
- `tools/projmgr/test/data/TestSolution/DuplicateComponents/Clayer/duplicateComponents.clayer.yml`
