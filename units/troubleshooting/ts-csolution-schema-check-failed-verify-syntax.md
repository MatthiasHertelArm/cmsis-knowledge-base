---
id: "ts-csolution-schema-check-failed-verify-syntax"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: schema check failed, verify syntax"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["schema check failed, verify syntax"]
symptom_regex: "^schema check failed, verify syntax$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:libs/ymlschemachecker/src/YmlSchemaValidator.cpp:53"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "Before it reads a YAML file, csolution checks it against its schema (cdefault.yml, csolution.yml, cbuild-pack.yml, cproject.yml, clayer.yml, cbuild-set.yml, debug-adapters.yml, and the files it generates) and prints this message with the file, line and column of each problem."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlSchemaChecker.cpp:18-39", "Open-CMSIS-Pack/devtools@30f5e817:libs/ymlschemachecker/src/YmlSchemaValidator.cpp:47-54", "Open-CMSIS-Pack/devtools@30f5e817:libs/ymlschemachecker/src/YmlSchemaValidator.cpp:159-191", "Open-CMSIS-Pack/devtools@30f5e817:libs/ymlschemachecker/src/YmlSchemaErrorHandler.cpp:27-54", "Open-CMSIS-Pack/devtools@30f5e817:external/json-schema-validator.patch:56", "Open-CMSIS-Pack/devtools@30f5e817:external/json-schema-validator.patch:65", "Open-CMSIS-Pack/devtools@30f5e817:external/json-schema-validator.patch:116", "Open-CMSIS-Pack/devtools@30f5e817:external/json-schema-validator.patch:125", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:29-33", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlEmitter.cpp:79-82", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:57", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:1617-1636", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:5485-5498", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:7379-7395"]
---

## Symptom

`schema check failed, verify syntax`

## Cause

Before it reads a YAML file, csolution checks it against its schema (cdefault.yml, csolution.yml, cbuild-pack.yml, cproject.yml, clayer.yml, cbuild-set.yml, debug-adapters.yml, and the files it generates) and prints this message with the file, line and column of each problem. It appears when the file is not valid YAML (the position of the parse error), or when a node breaks the schema: a key that is not allowed at that place, a value that does not have the allowed form, or a node that fits none or not all of the alternatives the schema combines.

## Fix

Open the file at the line and column printed in front of the message and correct it there: the YAML syntax (indentation, quoting, a key repeated in one map), the spelling and level of the key, or the form of the value. `-n` (`--no-check-schema`) skips the check; it does not make the input valid.

## Trigger in the source

```cpp
catch (YAML::Exception& e) {
```

## Note

csolution logs each schema error through a variable (ProjMgrYamlSchemaChecker.cpp:36), so the text is not in tools/projmgr: it comes from the schema checker library (a YAML parse error) and from devtools' patch of json-schema-validator, which replaces the validator's messages for a pattern mismatch, an additional property and failed anyOf/oneOf/allOf combinations with this one. Other schema violations may still print the validator's own text.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlSchemaChecker.cpp:18-39`
- `libs/ymlschemachecker/src/YmlSchemaValidator.cpp:47-54`
- `libs/ymlschemachecker/src/YmlSchemaValidator.cpp:159-191`
- `libs/ymlschemachecker/src/YmlSchemaErrorHandler.cpp:27-54`
- `external/json-schema-validator.patch:56`
- `external/json-schema-validator.patch:65`
- `external/json-schema-validator.patch:116`
- `external/json-schema-validator.patch:125`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:29-33`
- `tools/projmgr/src/ProjMgrYamlEmitter.cpp:79-82`
- `tools/projmgr/src/ProjMgr.cpp:57`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:1617-1636`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:5485-5498`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:7379-7395`
