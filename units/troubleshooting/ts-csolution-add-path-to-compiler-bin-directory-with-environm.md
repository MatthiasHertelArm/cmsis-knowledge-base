---
id: "ts-csolution-add-path-to-compiler-bin-directory-with-environm"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no compiler registered for '…'. Add path to compiler 'bin' directory with environment variable …"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["no compiler registered for '<…>'. Add path to compiler 'bin' directory with environment variable <…>_TOOLCHAIN_<major>_<minor>_<patch>"]
symptom_regex: "^no compiler registered for '.+?'\\. Add path to compiler 'bin' directory with environment variable .+?_TOOLCHAIN_<major>_<minor>_<patch>$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:1942"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "Toolchains are registered through `<name>_TOOLCHAIN_<major>_<minor>_<patch>` environment variables, but none is set for the compiler the context uses: the name in the message, from `compiler:` or `--toolchain`. csolution goes on and prints this warning once at the end."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1933-1946", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5377-5393", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:6037-6052"]
---

## Symptom

`no compiler registered for '<…>'. Add path to compiler 'bin' directory with environment variable <…>_TOOLCHAIN_<major>_<minor>_<patch>`

## Cause

Toolchains are registered through `<name>_TOOLCHAIN_<major>_<minor>_<patch>` environment variables, but none is set for the compiler the context uses: the name in the message, from `compiler:` or `--toolchain`. csolution goes on and prints this warning once at the end.

## Fix

Set `<name>_TOOLCHAIN_<major>_<minor>_<patch>` for this compiler to its `bin` directory (the message names the variable's prefix), or select a compiler that is registered.

## Trigger in the source

```cpp
if (itr == m_regToolchainsEnvVars.end()) {
```

## Note

No unit test prints this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:1933-1946`
- `tools/projmgr/src/ProjMgrWorker.cpp:5377-5393`
- `tools/projmgr/src/ProjMgrWorker.cpp:6037-6052`
