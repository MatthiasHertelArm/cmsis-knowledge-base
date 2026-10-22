---
id: "ts-csolution-check-args-was-not-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: check <args> was not found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["check <args> was not found"]
symptom_regex: "^check <args> was not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:460"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution command was invoked as `csolution check <args>` with an argument that is not in the check handler map."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:448-465", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:455-460"]
---

## Symptom

`check <args> was not found`

## Cause

The csolution command was invoked as `csolution check <args>` with an argument that is not in the check handler map. The only accepted value in the map here is `pack-updates`; the `<args>` in the message is the user's argument text that failed the lookup.

## Fix

Run `csolution check pack-updates` (the only subcommand argument this handler accepts) or check the spelling of the argument you passed after `check`.

## Trigger in the source

```cpp
if (it == handlers.end()) {
```

## Note

The message is printed with the literal text `<args>` in the source, so the user sees the placeholder rather than their value; the variable part is not substituted in this message. The sibling message for an empty argument is `check <args> was not specified` at line 451.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:448-465`
- `tools/projmgr/src/ProjMgr.cpp:455-460`
