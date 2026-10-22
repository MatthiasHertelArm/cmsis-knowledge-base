---
id: "ts-csolution-file-doesn-t-exist"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: file doesn't exist: '…'"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["file doesn't exist: '<…>'"]
symptom_regex: "^file doesn't exist: '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrYamlSchemaChecker.cpp:22"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "csolution calls ProjMgrYamlSchemaChecker::Validate with the path of a YAML input file before it runs schema validation."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlSchemaChecker.cpp:21-22", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlSchemaChecker.cpp:23"]
---

## Symptom

`file doesn't exist: '<…>'`

## Cause

csolution calls ProjMgrYamlSchemaChecker::Validate with the path of a YAML input file before it runs schema validation. The check at line 21 uses RteFsUtils::Exists on that path, and when no file exists there the tool logs this error with the path as given, in the placeholder, and returns false. The path is whatever was passed to the tool, so the missing file is the one named in the message.

## Fix

Check the file name and path in the message for typos or a wrong extension, and confirm that the file exists at that location. If the path is relative, run csolution from the directory that contains it, or pass the absolute path. Then run the command again.

## Trigger in the source

```cpp
if (!RteFsUtils::Exists(file)) {
```

## Note

The source lines do not show which callers pass which file, so the exact file that is missing is known only from the placeholder in the message. The message is not documented in the README.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlSchemaChecker.cpp:21-22`
- `tools/projmgr/src/ProjMgrYamlSchemaChecker.cpp:23`
