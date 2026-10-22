---
id: "ts-csolution-list-args-was-not-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: list <args> was not found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["list <args> was not found"]
symptom_regex: "^list <args> was not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:441"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "`csolution list` was given a subject it does not know; the word after `list` must be one of packs, boards, devices, npus, components, configs, dependencies, examples, templates, contexts, targets, target-sets, debuggers, generators, layers, toolchains or environment."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:420", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:440", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:257"]
---

## Symptom

`list <args> was not found`

## Cause

`csolution list` was given a subject it does not know; the word after `list` must be one of packs, boards, devices, npus, components, configs, dependencies, examples, templates, contexts, targets, target-sets, debuggers, generators, layers, toolchains or environment. A solution file whose name does not end in `.csolution.yml` is also taken as that subject.

## Fix

Correct the subject, e.g. `csolution list devices my.csolution.yml`, and pass the solution as `<name>.csolution.yml` or with `-s`.

## Trigger in the source

```cpp
if (it == handlers.end()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:420`
- `tools/projmgr/src/ProjMgr.cpp:440`
- `tools/projmgr/src/ProjMgr.cpp:257`
