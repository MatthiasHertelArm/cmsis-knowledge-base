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
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgr.cpp:416"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "`csolution list` was run without saying what to list."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:414", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:420", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:26"]
---

## Symptom

`list <args> was not specified`

## Cause

`csolution list` was run without saying what to list.

## Fix

Add the subject after `list`, e.g. `csolution list packs`, `csolution list devices`, `csolution list components my.csolution.yml` or `csolution list contexts my.csolution.yml`; `csolution --help` lists the choices.

## Trigger in the source

```cpp
if (m_args.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:414`
- `tools/projmgr/src/ProjMgr.cpp:420`
- `tools/projmgr/src/ProjMgr.cpp:26`
