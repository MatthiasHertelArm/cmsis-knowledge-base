---
id: "ts-csolution-shall-contain-mapping-elements"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: node '…' shall contain mapping elements"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["node '<…>' shall contain mapping elements"]
symptom_regex: "^node '.+?' shall contain mapping elements$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:1753"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A node that must hold key/value pairs is written as a scalar or empty in a csolution, cproject, clayer, cbuild-pack or cbuild-set YAML file; `<…>` is the node, with file, line and column."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:1753", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:1640"]
---

## Symptom

`node '<…>' shall contain mapping elements`

## Cause

A node that must hold key/value pairs is written as a scalar or empty in a csolution, cproject, clayer, cbuild-pack or cbuild-set YAML file; `<…>` is the node, with file, line and column. The nodes checked are `processor:`, `output-dirs:`, `generators:`, `rte:` and `west:`. A key left without a value (`processor:` with nothing indented under it) also counts.

## Fix

Write the node as a mapping with indented keys, e.g. `processor:` followed by `  trustzone: secure`, or remove the empty node.

## Trigger in the source

```cpp
} else if ((mappings.find(key) != mappings.end()) && (sequences.find(key) == sequences.end())) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:1753`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:1640`
