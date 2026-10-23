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
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:3884"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A linker script file (extension .ld, .sct, .scf, .icf, .src or `category: linkerScript`) is listed under groups: files:, but the context's linker script is already decided: by a `linker:` node with `script:`, `regions:`, `define:` or `auto:`, or by an …"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3879-3888", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3503-3553", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4117-4118", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtefsutils/src/RteFsUtils.cpp:875-884", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:4925-4947"]
---

## Symptom

`'<…>' this linker script is ignored<…>; multiple linker scripts defined<…>`

## Cause

A linker script file (extension .ld, .sct, .scf, .icf, .src or `category: linkerScript`) is listed under groups: files:, but the context's linker script is already decided: by a `linker:` node with `script:`, `regions:`, `define:` or `auto:`, or by an earlier linker script file in the groups. The file named in `<…>` is ignored; the suffix `; multiple linker scripts defined` is added when a script was already set.

## Fix

Keep one linker script per context: remove the extra file from groups:, or name the one you want with `linker: - script: <file>` and drop the other, or limit the entries with `for-context:`/`for-compiler:`. With `regions:` or `define:` a script listed only in groups: is ignored, so put your own script under `linker: - script:`; with `auto:` remove linker scripts from groups:.

## Trigger in the source

```cpp
if (!context.linker.autoGen && context.linker.script.empty() &&
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:3879-3888`
- `tools/projmgr/src/ProjMgrWorker.cpp:3503-3553`
- `tools/projmgr/src/ProjMgrWorker.cpp:4117-4118`
- `libs/rtefsutils/src/RteFsUtils.cpp:875-884`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:4925-4947`
