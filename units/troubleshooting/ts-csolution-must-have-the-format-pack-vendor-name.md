---
id: "ts-csolution-must-have-the-format-pack-vendor-name"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: access sequence '$Pack(…)' must have the format '$Pack(vendor::name)$'"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["access sequence '$Pack(<…>)' must have the format '$Pack(vendor::name)$'"]
symptom_regex: "^access sequence '\\$Pack\\(.+?\\)' must have the format '\\$Pack\\(vendor::name\\)\\$'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:3688"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The $Pack(...)$ access sequence used in a csolution file does not contain a valid vendor::name pair."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3684-3690", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3686-3688"]
---

## Symptom

`access sequence '$Pack(<…>)' must have the format '$Pack(vendor::name)$'`

## Cause

The $Pack(...)$ access sequence used in a csolution file does not contain a valid vendor::name pair. ExpandPackDir parses the text between the parentheses with ConvertToPackInfo, and the vendor or the name comes out empty, so the sequence cannot identify a pack. The <…> in the message is the text the user wrote between $Pack( and ).

## Fix

Rewrite the access sequence so the argument has the form vendor::name, for example $Pack(ARM::CMSIS)$ instead of a bare name without the vendor part. Then run the build again.

## Trigger in the source

```cpp
if (packInfo.vendor.empty() || packInfo.name.empty()) {
```

## Note

The warning is raised before the pack is looked up, so it is about the syntax of the argument only. When the syntax is valid but no loaded pack matches, the tool prints a different message ('access sequence pack was not loaded').

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:3684-3690`
- `tools/projmgr/src/ProjMgrWorker.cpp:3686-3688`
