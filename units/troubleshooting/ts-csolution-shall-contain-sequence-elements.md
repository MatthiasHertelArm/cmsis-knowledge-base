---
id: "ts-csolution-shall-contain-sequence-elements"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: node '…' shall contain sequence elements"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["node '<…>' shall contain sequence elements"]
symptom_regex: "^node '.+?' shall contain sequence elements$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrYamlParser.cpp:1745"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A node that must be a list is written as a scalar, a mapping or left empty in a csolution, cproject, clayer, cbuild-pack or cbuild-set YAML file; `<…>` is the node, with file, line and column."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:1745", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:1621", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestSolution/PackLocking/cbuild_pack_with_disallowed_field.cbuild-pack.yml:1", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:1643"]
---

## Symptom

`node '<…>' shall contain sequence elements`

## Cause

A node that must be a list is written as a scalar, a mapping or left empty in a csolution, cproject, clayer, cbuild-pack or cbuild-set YAML file; `<…>` is the node, with file, line and column. The nodes checked are `projects:`, `target-types:`, `build-types:`, `misc:`, `packs:`, `resolved-packs:`, `components:`, `connections:`, `layers:`, `groups:`, `files:`, `setups:`, `linker:`, `executes:` and `input:`. Example: `misc: 1`.

## Fix

Write the node as a list whose entries start with `- `, e.g. `packs:` followed by `  - pack: ARM::CMSIS`, or remove the empty node.

## Trigger in the source

```cpp
} else if ((sequences.find(key) != sequences.end()) && (mappings.find(key) == mappings.end())) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:1745`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:1621`
- `tools/projmgr/test/data/TestSolution/PackLocking/cbuild_pack_with_disallowed_field.cbuild-pack.yml:1`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:1643`
