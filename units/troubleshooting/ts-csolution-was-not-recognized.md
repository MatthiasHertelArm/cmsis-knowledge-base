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
summary: "The csolution YAML parser checks every key in a mapping against the set of keys allowed for that node (the root or a sequence/mapping entry it validates recursively)."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:1735-1739", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:1760-1771", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:1773-1782"]
---

## Symptom

`key '<…>' was not recognized`

## Cause

The csolution YAML parser checks every key in a mapping against the set of keys allowed for that node (the root or a sequence/mapping entry it validates recursively). The key named in the message is not in the allowed set for the node where it appears, which usually means a typo, a key placed at the wrong nesting level, or a key that the installed tool version does not know. The message is a warning, so parsing continues with the unrecognized key ignored.

## Fix

Find the key named in the message in your csolution YAML (project, layer or cbuild-pack file) and check its spelling and indentation against the schema of the node it sits under. Remove the key or move it to the node where it belongs. If the key is valid for your tool version but still flagged, update csolution to a version that knows it.

## Trigger in the source

```cpp
if (keys.find(item.first.as<string>()) == keys.end()) {
```

## Note

The message text is '<key> was not recognized' with the key quoted; the id is the same family as the message. Nested nodes are validated through ValidateSequence and ValidateMapping, so the reported key can belong to any level of the file.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:1735-1739`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:1760-1771`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:1773-1782`
