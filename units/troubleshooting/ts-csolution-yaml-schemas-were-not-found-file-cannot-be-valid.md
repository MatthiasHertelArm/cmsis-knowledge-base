---
id: "ts-csolution-yaml-schemas-were-not-found-file-cannot-be-valid"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: yaml schemas were not found, file cannot be validated"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["yaml schemas were not found, file cannot be validated"]
symptom_regex: "^yaml schemas were not found, file cannot be validated$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrYamlSchemaChecker.cpp:28"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "csolution looks for `<type>.schema.json` (e.g."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlSchemaChecker.cpp:26", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlSchemaChecker.cpp:41", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtefsutils/src/RteFsUtils.cpp:869", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrSchemaCheckerUnitTests.cpp:66"]
---

## Symptom

`yaml schemas were not found, file cannot be validated`

## Cause

csolution looks for `<type>.schema.json` (e.g. `cproject.schema.json`) next to its executable, in `../etc/` or in `../../etc/`, and did not find the schema for the file named with the message. The file is processed without schema validation. This points to an incomplete CMSIS-Toolbox installation or a csolution binary moved away from its `etc` folder.

## Fix

Use csolution from a complete CMSIS-Toolbox installation whose `etc` folder contains the *.schema.json files, or reinstall the toolbox. `-n` suppresses the schema check and this warning.

## Trigger in the source

```cpp
if(schemaFile.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlSchemaChecker.cpp:26`
- `tools/projmgr/src/ProjMgrYamlSchemaChecker.cpp:41`
- `libs/rtefsutils/src/RteFsUtils.cpp:869`
- `tools/projmgr/test/src/ProjMgrSchemaCheckerUnitTests.cpp:66`
