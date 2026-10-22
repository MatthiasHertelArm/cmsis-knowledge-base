---
id: "ts-csolution-input-csolution-yml-was-not-specified"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: input csolution.yml was not specified"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["input csolution.yml was not specified"]
symptom_regex: "^input csolution\\.yml was not specified$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:1076"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution command ran its pack version check mode without a csolution.yml path."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:1074-1078", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:1097-1103"]
---

## Symptom

`input csolution.yml was not specified`

## Cause

The csolution command ran its pack version check mode without a csolution.yml path. RunCheckPackVerCmd requires m_csolutionFile to be set before it parses contexts, and it stops with this error when that input is empty. Unlike the list-toolchains path, which only parses files when a csolution file was given, this check always needs one.

## Fix

Run the same csolution command again and pass the path to your csolution.yml project file as its input argument, for example csolution <check-pack-version-subcommand> path/to/project.csolution.yml. Use the subcommand that runs the pack version check; the source lines shown do not name it.

## Trigger in the source

```cpp
if (m_csolutionFile.empty()) {
```

## Note

The README does not document this message. The fix relies on the subcommand's own argument syntax, which is outside the lines given, so the example command is generic.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:1074-1078`
- `tools/projmgr/src/ProjMgr.cpp:1097-1103`
