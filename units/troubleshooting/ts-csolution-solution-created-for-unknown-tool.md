---
id: "ts-csolution-solution-created-for-unknown-tool"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: solution created for unknown tool: …"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["solution created for unknown tool: <…>"]
symptom_regex: "^solution created for unknown tool: .+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:1204"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution file sets a `created-for` value (the `createdFor` argument) whose tool name is not `cmsis-toolbox` or does not match the `<name>@<major>.<minor>.<patch>` form."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:1175-1177", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:1182", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:1204"]
---

## Symptom

`solution created for unknown tool: <…>`

## Cause

The csolution file sets a `created-for` value (the `createdFor` argument) whose tool name is not `cmsis-toolbox` or does not match the `<name>@<major>.<minor>.<patch>` form. ValidateCreatedFor only checks the toolbox version for `cmsis-toolbox`; any other value falls through to this warning, which prints the raw `created-for` string after the colon.

## Fix

Set `created-for` in the csolution YAML to the form `CMSIS-Toolbox@<major>.<minor>.<patch>`, for example `created-for: CMSIS-Toolbox@2.0.0`, using the version of the toolbox that created the solution. The warning is not fatal: the function still returns true and processing continues.

## Note

The message is reached both when the regex does not match and when the tool name is something other than cmsis-toolbox; the source does not show which of these produced a given value, so the cause is inferred from the code path. The README does not document this message. The example version in the fix is illustrative, not taken from the source.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:1175-1177`
- `tools/projmgr/src/ProjMgr.cpp:1182`
- `tools/projmgr/src/ProjMgr.cpp:1204`
