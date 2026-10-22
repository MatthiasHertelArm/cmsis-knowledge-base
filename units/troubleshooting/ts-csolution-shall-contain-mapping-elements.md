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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrYamlParser.cpp:1753"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "ValidateKeys reaches this error when a YAML key that the parser knows as a mapping-type node (it is in the mappings table and not in the sequences table) has a value that is not a YAML map, for example …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:1733-1758", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:1752-1753"]
---

## Symptom

`node '<…>' shall contain mapping elements`

## Cause

ValidateKeys reaches this error when a YAML key that the parser knows as a mapping-type node (it is in the mappings table and not in the sequences table) has a value that is not a YAML map, for example a scalar or an empty value after the colon. The '<…>' in the message is that key's name, as written in the csolution YAML file at the line and column the message reports.

## Fix

Open the file named in the message at the reported line and check the value of the node named in the message. Write it as a block of indented 'key: value' entries under that node, not as a single scalar or an empty value. Compare the structure with the csolution schema for that key.

## Trigger in the source

```cpp
} else if ((mappings.find(key) != mappings.end()) && (sequences.find(key) == sequences.end())) {
```

## Note

The message text is the same string used for the sequence case at line 1745 with 'sequence' in place of 'mapping'; the two branches are symmetric. The condition is checked after IsMap() fails, so a value that is a sequence or a scalar both reach it when the key is in mappings. The README does not document this message, and the fix assumes the user's file is hand-written YAML, which the source does not confirm.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:1733-1758`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:1752-1753`
