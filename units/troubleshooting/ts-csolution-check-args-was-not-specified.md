---
id: "ts-csolution-check-args-was-not-specified"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: check <args> was not specified"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["check <args> was not specified"]
symptom_regex: "^check <args> was not specified$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:451"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "`csolution check` was run without a subcommand."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:448-453", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:257-266"]
---

## Symptom

`check <args> was not specified`

## Cause

`csolution check` was run without a subcommand. `<args>` is printed literally.

## Fix

Add the subcommand: `csolution check pack-updates <name>.csolution.yml`.

## Trigger in the source

```cpp
if (m_args.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:448-453`
- `tools/projmgr/src/ProjMgr.cpp:257-266`
