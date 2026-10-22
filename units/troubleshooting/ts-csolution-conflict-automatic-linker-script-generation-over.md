---
id: "ts-csolution-conflict-automatic-linker-script-generation-over"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: conflict: automatic linker script generation overrules specified script '…'"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["conflict: automatic linker script generation overrules specified script '<…>'"]
symptom_regex: "^conflict: automatic linker script generation overrules specified script '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:2359"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The linker section of the csolution project sets both an explicit linker script and automatic linker script generation (linker: autoGen)."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2356-2361", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2357-2359"]
---

## Symptom

`conflict: automatic linker script generation overrules specified script '<…>'`

## Cause

The linker section of the csolution project sets both an explicit linker script and automatic linker script generation (linker: autoGen). When the tool processes an ELF output that is not image-only and not a West or CMake build, it sees a non-empty linker script together with autoGen enabled, prints this warning and discards the script path, so the generated script is used instead. The text in angle brackets is the script path from the project's linker settings.

## Fix

Decide which linker script should be used. To keep the generated script, remove the script entry from the linker section of the csolution project so the warning no longer applies. To use your own script, turn off automatic generation (set autoGen to false, or remove it) and keep the script entry.

## Trigger in the source

```cpp
if (!context.linker.script.empty()) {
```

## Note

The README does not document this message. The warning is emitted with the context name, so it appears per build context. The exact YAML key names were not visible in the lines given, so the fix refers to the setting by its meaning.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:2356-2361`
- `tools/projmgr/src/ProjMgrWorker.cpp:2357-2359`
