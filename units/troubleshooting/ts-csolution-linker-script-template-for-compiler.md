---
id: "ts-csolution-linker-script-template-for-compiler"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: linker script template for compiler '…' was not found"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["linker script template for compiler '<…>' was not found"]
symptom_regex: "^linker script template for compiler '.+?' was not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:2462"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The project has no linker script of its own (no `linker:` - `script:` in cproject.yml or clayer.yml and none from a component), or uses `linker:` - `auto:`, so csolution looks for the template `<compiler>_linker_script.*` of the selected compiler; `<…>` …"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2449", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2462", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2355", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrUtils.cpp:199", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/templates/gcc_linker_script.ld.src:1", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrWorkerUnitTests.cpp:1549"]
---

## Symptom

`linker script template for compiler '<…>' was not found`

## Cause

The project has no linker script of its own (no `linker:` - `script:` in cproject.yml or clayer.yml and none from a component), or uses `linker:` - `auto:`, so csolution looks for the template `<compiler>_linker_script.*` of the selected compiler; `<…>` is that compiler. It searches the compiler root (environment variable CMSIS_COMPILER_ROOT, otherwise the `etc` folder of the CMSIS-Toolbox installation) and found no template there. Templates exist for AC6, GCC, IAR, CLANG, CLANG_TI and XC. The context then has no linker script.

## Fix

Check that CMSIS_COMPILER_ROOT points to the toolbox's `etc` folder, or that the CMSIS-Toolbox installation is complete, and that `compiler:` names a supported toolchain. Alternatively give the project its own script: `linker:` - `script: path/to/file.sct` in the cproject.yml.

## Trigger in the source

```cpp
if (linkerScript.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:2449`
- `tools/projmgr/src/ProjMgrWorker.cpp:2462`
- `tools/projmgr/src/ProjMgrWorker.cpp:2355`
- `tools/projmgr/src/ProjMgrUtils.cpp:199`
- `tools/projmgr/templates/gcc_linker_script.ld.src:1`
- `tools/projmgr/test/src/ProjMgrWorkerUnitTests.cpp:1549`
