---
id: "ts-csolution-was-not-recognized"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: key '…' was not recognized"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["key '<…>' was not recognized"]
symptom_regex: "^key '.+?' was not recognized$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrYamlParser.cpp:1738"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A YAML file csolution reads (csolution.yml, cproject.yml, clayer.yml, cdefault.yml, cbuild-pack.yml or cbuild-set.yml) contains a key that is not valid at that place; `<…>` is the key and the message carries its file, line and column."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:1733", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:1663", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:71", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestSolution/PackLocking/cbuild_pack_with_disallowed_field.cbuild-pack.yml:1", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:1638"]
---

## Symptom

`key '<…>' was not recognized`

## Cause

A YAML file csolution reads (csolution.yml, cproject.yml, clayer.yml, cdefault.yml, cbuild-pack.yml or cbuild-set.yml) contains a key that is not valid at that place; `<…>` is the key and the message carries its file, line and column. It is usually a typo or a key placed under the wrong parent. With the schema check on, the schema normally reports the key first; this warning is what remains with `-n`/`--no-check-schema` or when the schemas are not installed.

## Fix

Fix the spelling or move the key to the node where the YAML schema allows it (schemas/*.schema.json), or remove it. Run without `-n` to get the schema's report on the same line.

## Trigger in the source

```cpp
if (keys.find(item.first.as<string>()) == keys.end()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:1733`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:1663`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:71`
- `tools/projmgr/test/data/TestSolution/PackLocking/cbuild_pack_with_disallowed_field.cbuild-pack.yml:1`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:1638`
