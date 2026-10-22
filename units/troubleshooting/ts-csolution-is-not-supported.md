---
id: "ts-csolution-is-not-supported"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: 'for-compiler: …' is not supported"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["'for-compiler: <…>' is not supported"]
symptom_regex: "^'for\\-compiler: .+?' is not supported$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:4103"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A `for-compiler:` value (on a file, group, setup or linker entry) names a compiler for which no toolchain configuration file `<name>.<version>.cmake` exists in the compiler root (CMSIS_COMPILER_ROOT, default <cmsis-toolbox>/etc)."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3944-3965", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4102-4104", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5430-5440", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrUtils.cpp:199-212", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/schemas/common.schema.json:192-197", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:5508-5531", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestSolution/typefilters.cproject.yml:19"]
---

## Symptom

`'for-compiler: <…>' is not supported`

## Cause

A `for-compiler:` value (on a file, group, setup or linker entry) names a compiler for which no toolchain configuration file `<name>.<version>.cmake` exists in the compiler root (CMSIS_COMPILER_ROOT, default <cmsis-toolbox>/etc). The name match is case-sensitive, so `Ac6` is reported while `AC6` is fine; the `<…>` is the name before `@`.

## Fix

Spell the compiler as the toolchain files do: AC6, GCC, IAR, CLANG, CLANG_TI or XC, e.g. `for-compiler: AC6@>=6.18.1`. If the spelling is right, check that CMSIS_COMPILER_ROOT points to the CMSIS-Toolbox etc folder that contains the matching *.cmake file.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:3944-3965`
- `tools/projmgr/src/ProjMgrWorker.cpp:4102-4104`
- `tools/projmgr/src/ProjMgrWorker.cpp:5430-5440`
- `tools/projmgr/src/ProjMgrUtils.cpp:199-212`
- `tools/projmgr/schemas/common.schema.json:192-197`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:5508-5531`
- `tools/projmgr/test/data/TestSolution/typefilters.cproject.yml:19`
