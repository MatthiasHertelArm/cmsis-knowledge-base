---
id: "ts-csolution-multiple-linker-scripts-defined"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: '…' this linker script is ignored…; multiple linker scripts defined…"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["'<…>' this linker script is ignored<…>; multiple linker scripts defined<…>"]
symptom_regex: "^'.+?' this linker script is ignored.+?; multiple linker scripts defined.+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:3884"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A file with category linkerScript is added to a context, but the context already has a linker script, or it uses linker autoGen, or it defines linker regions or defines, so the tool keeps the first linker script and …"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3879-3886"]
---

## Symptom

`'<…>' this linker script is ignored<…>; multiple linker scripts defined<…>`

## Cause

A file with category linkerScript is added to a context, but the context already has a linker script, or it uses linker autoGen, or it defines linker regions or defines, so the tool keeps the first linker script and ignores this file. The message names the ignored file. The suffix '; multiple linker scripts defined' is added only when a script has already been selected, so it appears when two linker-script files are listed. Without that suffix, the file was ignored because of autoGen, regions or defines.

## Fix

Keep exactly one linker-script file in the context's file list (for example in the project or layer .csolution.yml). If you list several, remove the extra ones. If you list a linker script together with linker regions or defines, or with linker autoGen, remove one of the two approaches so that the script is used as the linker script.

## Trigger in the source

```cpp
if (!context.linker.autoGen && context.linker.script.empty() &&
```

## Note

The README does not document this message. The warning fires only in the else branch of the condition at line 3880, and the 'multiple linker scripts defined' suffix depends on context.linker.script being non-empty at that point, so the suffix can be absent even when the ignore reason is autoGen, regions or defines.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:3879-3886`
