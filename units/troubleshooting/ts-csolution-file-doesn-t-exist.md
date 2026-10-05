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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlSchemaChecker.cpp:22"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlSchemaChecker.cpp:18-24", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:69-74", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrRpcServer.cpp:322-350", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrSchemaCheckerUnitTests.cpp:62-64"]
---

## Symptom

`file doesn't exist: '<…>'`

## Cause

The YAML schema check was asked to validate a file that does not exist at the given path (`<…>`). On the command line csolution checks its input files before, so this mostly appears when a client such as an IDE extension, using `csolution rpc`, loads a *.csolution.yml path that does not exist.

## Fix

Check the solution path the command or the client passes to csolution and point it to an existing `<name>.csolution.yml`.

## Trigger in the source

```cpp
if (!RteFsUtils::Exists(file)) {
```

## Note

All command-line callers check existence before parsing; RPC LoadSolution does not, which is the only plain path to this message found.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlSchemaChecker.cpp:18-24`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:69-74`
- `tools/projmgr/src/ProjMgrRpcServer.cpp:322-350`
- `tools/projmgr/test/src/ProjMgrSchemaCheckerUnitTests.cpp:62-64`
