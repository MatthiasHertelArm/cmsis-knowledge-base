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
summary: "The csolution YAML parser found a key that the tool knows must hold a YAML sequence (a list), but the value in the user's file is a scalar or a mapping instead."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:1740-1747", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:1744-1745"]
---

## Symptom

`node '<…>' shall contain sequence elements`

## Cause

The csolution YAML parser found a key that the tool knows must hold a YAML sequence (a list), but the value in the user's file is a scalar or a mapping instead. ValidateKeys checks each key of a node: when the value is not a sequence and the key is listed in the sequences table (and not in the mappings table), it reports this error with the key name in place of the placeholder. The placeholder is the offending key in the csolution YAML file, at the line and column where that key appears.

## Fix

Open the csolution YAML file at the reported line and rewrite the value of that key as a list, with each entry prefixed by a dash, for example:
  <key>:
    - item1
    - item2
A single value written inline (key: value) or a nested mapping under that key must be turned into a list. The expected keys for each section are defined by the tool's sequences table, so check the schema for the key you are editing.

## Trigger in the source

```cpp
} else if ((sequences.find(key) != sequences.end()) && (mappings.find(key) == mappings.end())) {
```

## Note

The message is printed by ValidateKeys, which is also used for mapping checks; the sibling message 'shall contain mapping elements' is the reverse case. The README does not document this message, so the cause is read from the source logic only. The fix text is a general instruction; the list of keys that must be sequences is in a table not included in the lines given.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:1740-1747`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:1744-1745`
