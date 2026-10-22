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
summary: "`csolution check` was followed by a subcommand other than `pack-updates`, the only one it knows."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:448-465"]
---

## Symptom

`check <args> was not found`

## Cause

`csolution check` was followed by a subcommand other than `pack-updates`, the only one it knows. The text `<args>` is printed literally, not replaced by what was typed.

## Fix

Use `csolution check pack-updates <name>.csolution.yml`.

## Trigger in the source

```cpp
if (it == handlers.end()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:448-465`
