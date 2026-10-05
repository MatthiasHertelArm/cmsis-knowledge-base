---
id: "ts-csolution-is-deprecated-at-this-level-and-accepted-in-csol"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: …'device: Dname'…'board:' node… is deprecated at this level and accepted in *.csolution.yml only"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["<…>'device: Dname'<…>'board:' node<…> is deprecated at this level and accepted in *.csolution.yml only"]
symptom_regex: "^.+?'device: Dname'.+?'board:' node.+? is deprecated at this level and accepted in \\*\\.csolution\\.yml only$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:1127"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:1110-1131", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:3056-3069"]
---

## Symptom

`<…>'device: Dname'<…>'board:' node<…> is deprecated at this level and accepted in *.csolution.yml only`

## Cause

A cproject.yml or clayer.yml sets `device:` with a device name or sets `board:`. Board and device belong to the target-types: of the csolution.yml; in a project or layer only the processor form `device: :<pname>` is accepted without warning.

## Fix

Move `board:`/`device:` to the target type in the csolution.yml (`target-types: - type: MyTarget  board: Vendor::BoardName`) and keep at most `device: :cm33_core0` in the cproject.yml. A layer that targets a board or device uses `for-board:`/`for-device:` instead.

## Trigger in the source

```cpp
if ((key == YAML_DEVICE) && regex_match(value, regex("^:[ -9;-~]+$"))) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:1110-1131`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:3056-3069`
