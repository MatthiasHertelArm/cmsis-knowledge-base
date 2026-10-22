---
id: "ts-csolution-duplicate-cmake-image-type"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: duplicate CMake image type '…'"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["duplicate CMake image type '<…>'"]
symptom_regex: "^duplicate CMake image type '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrYamlParser.cpp:927"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A csolution project's CMake descriptor lists more than one entry under 'images' with the same 'type' value."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:920-933", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:926-930"]
---

## Symptom

`duplicate CMake image type '<…>'`

## Cause

A csolution project's CMake descriptor lists more than one entry under 'images' with the same 'type' value. The parser keeps a set of the type strings it has seen in that images list and rejects the second occurrence; the '<…>' in the message is the repeated type string taken from the 'type' key of the image entry.

## Fix

Open the csolution YAML file named in the log and find the 'cmake' project entry with an 'images' list. Give each image a distinct 'type' value, or remove the duplicate image entry, then run csolution again.

## Trigger in the source

```cpp
if (!imageTypes.insert(image.type).second) {
```

## Note

The error is reported at the line of the 'type' key of the duplicate image entry, and the function returns false, which aborts parsing of the csolution file. The message is not documented in the README.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:920-933`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:926-930`
