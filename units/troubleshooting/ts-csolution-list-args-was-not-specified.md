---
id: "ts-csolution-list-args-was-not-specified"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: list <args> was not specified"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["list <args> was not specified"]
symptom_regex: "^list <args> was not specified$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:416"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The user ran `csolution list` without the sub-command argument that says what to list."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:413-418", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:420-438", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:441"]
---

## Symptom

`list <args> was not specified`

## Cause

The user ran `csolution list` without the sub-command argument that says what to list. ProcessListCommand() checks m_args before doing anything else and, when it is empty, prints this error and returns ERROR. The <args> placeholder stands for the missing item; valid values are the keys of the handler map in the same function (packs, boards, devices, npus, components, configs, dependencies, examples, templates, contexts, targets, target-sets, debuggers, generators, layers, toolchains, environment).

## Fix

Run the list command with one of the supported arguments, for example `csolution list packs` or `csolution list devices`. Choose the name that matches the information you need; the source lists the accepted names in the handler map of ProcessListCommand().

## Trigger in the source

```cpp
if (m_args.empty()) {
```

## Note

The sibling message for an unknown argument is 'list <args> was not found' (ProjMgr.cpp:441). The README does not document this message, so the cause and fix come from the source alone.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:413-418`
- `tools/projmgr/src/ProjMgr.cpp:420-438`
- `tools/projmgr/src/ProjMgr.cpp:441`
