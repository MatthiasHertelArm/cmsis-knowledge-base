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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:927"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "In the csolution.yml, a projects: entry with `cmake:` lists two `images:` with the same `type:` (elf, hex, bin or lib)."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:918-931", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/schemas/common.schema.json:2710-2733"]
---

## Symptom

`duplicate CMake image type '<…>'`

## Cause

In the csolution.yml, a projects: entry with `cmake:` lists two `images:` with the same `type:` (elf, hex, bin or lib). Each output type may appear once per CMake project; the message points to the second `type:`.

## Fix

Keep one image per type, e.g. `images: - image: build/app.elf  type: elf` and `- image: build/app.hex  type: hex`.

## Trigger in the source

```cpp
if (!imageTypes.insert(image.type).second) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:918-931`
- `tools/projmgr/schemas/common.schema.json:2710-2733`
