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
summary: "Validate() calls FindSchema(), which builds a schema file name from the YAML file's base name, appends \".schema.json\", and searches for it with RteFsUtils::FindFileInEtc relative to the csolution executable's path."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlSchemaChecker.cpp:26-30", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlSchemaChecker.cpp:41-56"]
---

## Symptom

`yaml schemas were not found, file cannot be validated`

## Cause

Validate() calls FindSchema(), which builds a schema file name from the YAML file's base name, appends ".schema.json", and searches for it with RteFsUtils::FindFileInEtc relative to the csolution executable's path. When no matching schema is found, the tool logs this warning with the YAML file as its location and returns success without validating the file. The warning therefore means the schema lookup failed, not that the YAML file itself is wrong.

## Fix

Check that the csolution installation is complete and that it contains the schema JSON files in an etc directory next to its executable, with a name matching the YAML file (for example cdefault.schema.json for cdefault.yml). If the installation is intact, run csolution from its installed location rather than from a copy of the binary that lacks the etc directory. The source does not show any other way to supply the schema, so if the lookup still fails, the file cannot be validated by this tool version.

## Trigger in the source

```cpp
if(schemaFile.empty()) {
```

## Note

The message is a warning and Validate() returns true, so processing continues and the YAML file is not checked against any schema. The message carries no variable text; the file name appears only in the logger's location field. The lookup logic for names with a prefix (the ExtractFileExtension branch) is only partly clear from these lines, so the exact schema name for such files is not confirmed.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlSchemaChecker.cpp:26-30`
- `tools/projmgr/src/ProjMgrYamlSchemaChecker.cpp:41-56`
