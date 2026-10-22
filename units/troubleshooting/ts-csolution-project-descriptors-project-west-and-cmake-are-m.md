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
summary: "One entry under `projects:` in the csolution.yml has more than one of `project:`, `west:` and `cmake:`; the message points to that entry."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:879", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/schemas/common.schema.json:753"]
---

## Symptom

`project descriptors 'project', 'west', and 'cmake' are mutually exclusive`

## Cause

One entry under `projects:` in the csolution.yml has more than one of `project:`, `west:` and `cmake:`; the message points to that entry. Each entry describes exactly one project. The schema check reports the same problem, so this message appears mainly with `-n`.

## Fix

Split the entry into separate list items, one with `- project: ...`, another with `- west: ...` or `- cmake: ...`.

## Trigger in the source

```cpp
if (descriptorCount > 1) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:879`
- `tools/projmgr/schemas/common.schema.json:753`
