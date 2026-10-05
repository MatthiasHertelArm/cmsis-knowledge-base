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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:1204"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "`created-for:` in the csolution.yml does not have the form `CMSIS-Toolbox@<major>.<minor>.<patch>`; `<…>` is the value."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:1172", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:1204", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/schemas/common.schema.json:1920", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:6521"]
---

## Symptom

`solution created for unknown tool: <…>`

## Cause

`created-for:` in the csolution.yml does not have the form `CMSIS-Toolbox@<major>.<minor>.<patch>`; `<…>` is the value. Another tool name, or a version with a pre-release or build suffix such as `CMSIS-Toolbox@2.6.0-rc1`, is not recognised, and the minimum-version check is skipped.

## Fix

Write `created-for: CMSIS-Toolbox@2.6.0` with the plain three-part version of the toolbox the solution needs, or remove the node.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:1172`
- `tools/projmgr/src/ProjMgr.cpp:1204`
- `tools/projmgr/schemas/common.schema.json:1920`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:6521`
