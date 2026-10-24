---
id: "ts-csolution-no-compiler-registered-add-path-to-compiler-bin-"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no compiler registered. Add path to compiler 'bin' directory with environment variable …"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["no compiler registered. Add path to compiler 'bin' directory with environment variable <name>_TOOLCHAIN_<major>_<minor>_<patch>. <name> is one of AC6, GCC, IAR, CLANG"]
symptom_regex: "^no compiler registered\\. Add path to compiler 'bin' directory with environment variable <name>_TOOLCHAIN_<major>_<minor>_<patch>\\. <name> is one of AC6, GCC, IAR, CLANG$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:5391"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "No environment variable of the form `<name>_TOOLCHAIN_<major>_<minor>_<patch>=<path>` is set, so csolution knows no installed compiler."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5377-5393", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1935-1946", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:353-360", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:6037-6052", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:2071-2076", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:2079-2090"]
---

## Symptom

`no compiler registered. Add path to compiler 'bin' directory with environment variable <name>_TOOLCHAIN_<major>_<minor>_<patch>. <name> is one of AC6, GCC, IAR, CLANG`

## Cause

No environment variable of the form `<name>_TOOLCHAIN_<major>_<minor>_<patch>=<path>` is set, so csolution knows no installed compiler. It reads these variables from its environment to find the compiler of a context and to list or select toolchains; the message is a warning, printed once at the end.

## Fix

Set one variable per installed compiler to its `bin` directory in the environment csolution runs in, with the compiler's name (AC6, GCC, IAR or CLANG) and version, e.g. `AC6_TOOLCHAIN_6_18_0=<path to the compiler>/bin`; then run csolution again.

## Trigger in the source

```cpp
if (m_regToolchainsEnvVars.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:5377-5393`
- `tools/projmgr/src/ProjMgrWorker.cpp:1935-1946`
- `tools/projmgr/src/ProjMgr.cpp:353-360`
- `tools/projmgr/src/ProjMgrWorker.cpp:6037-6052`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:2071-2076`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:2079-2090`
