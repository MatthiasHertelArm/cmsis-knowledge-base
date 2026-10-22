---
id: "ts-csolution-project-descriptors-project-west-and-cmake-are-m"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: project descriptors 'project', 'west', and 'cmake' are mutually exclusive"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["project descriptors 'project', 'west', and 'cmake' are mutually exclusive"]
symptom_regex: "^project descriptors 'project', 'west', and 'cmake' are mutually exclusive$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrYamlParser.cpp:885"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution YAML has a single entry under 'projects' that sets more than one of the descriptor keys 'project', 'west' and 'cmake' at once."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:880-888", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:885-887"]
---

## Symptom

`project descriptors 'project', 'west', and 'cmake' are mutually exclusive`

## Cause

The csolution YAML has a single entry under 'projects' that sets more than one of the descriptor keys 'project', 'west' and 'cmake' at once. The parser counts how many of these keys are defined on that entry and rejects the entry when the count is greater than one, because each projects entry may describe only one kind of project.

## Fix

Split the entry so that each item under 'projects' uses only one of the keys. For example, keep 'project: <path>.cproject.yml' in one list item and move the 'west:' or 'cmake:' block into a separate list item, instead of putting them side by side in the same item.

## Trigger in the source

```cpp
if (descriptorCount > 1) {
```

## Note

The message text names the three keys directly; the check is a plain count of defined keys on each projects entry, so the cause and fix follow from the source. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:880-888`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:885-887`
