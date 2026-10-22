---
id: "ts-csolution-does-not-accept-more-than"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: component '…' does not accept more than … instance(s)"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["component '<…>' does not accept more than <…> instance(s)"]
symptom_regex: "^component '.+?' does not accept more than .+? instance\\(s\\)$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:2042"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution project requests more instances of a component than the component's definition allows."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2041-2043", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2045-2046"]
---

## Symptom

`component '<…>' does not accept more than <…> instance(s)`

## Cause

The csolution project requests more instances of a component than the component's definition allows. The requested count comes from the component's instances value in the csolution input (item.instances), and the limit is the maximum instance count the matched component declares in the pack description (GetMaxInstances()). The first placeholder is the component name from the request, and the number is the maximum the component accepts.

## Fix

Lower the instances value for this component in the csolution project (or in the layer or component entry that sets it) to at most the maximum printed in the message. If more instances are really needed, check whether a different component variant or a pack version declares a higher maximum; the limit itself is defined by the pack, not by csolution.

## Trigger in the source

```cpp
if (item.instances > matchedComponentInstance->GetMaxInstances()) {
```

## Note

Not documented in the README. The message is printed only when item.instances exceeds GetMaxInstances(); the lines given do not show where item.instances is read from the YAML, so the exact input key is inferred rather than confirmed. Otherwise the handling is plain: an error is logged and the error flag is set, and no instances attribute is added.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:2041-2043`
- `tools/projmgr/src/ProjMgrWorker.cpp:2045-2046`
