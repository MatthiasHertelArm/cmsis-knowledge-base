---
id: "ts-csolution-no-toolchain-cmake-files-found-for"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no toolchain cmake files found for '…' in '…' directory"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no toolchain cmake files found for '<…>' in '<…>' directory"]
symptom_regex: "^no toolchain cmake files found for '.+?' in '.+?' directory$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:5470"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "csolution found no toolchain configuration file `<name>.<major>.<minor>.<patch>.cmake` for the named compiler in the compiler root, the folder named second: the one `CMSIS_COMPILER_ROOT` points to, else the `etc` folder of the CMSIS-Toolbox installation (empty when that folder does not exist)."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5442-5473", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5430-5440", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrUtils.cpp:199-212", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1948-1951", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5395-5411", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5004-5019", "Open-CMSIS-Pack/devtools@30f5e817:libs/rteutils/src/VersionCmp.cpp:165-187", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:2158-2190", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrWorkerUnitTests.cpp:68-92"]
---

## Symptom

`no toolchain cmake files found for '<…>' in '<…>' directory`

## Cause

csolution found no toolchain configuration file `<name>.<major>.<minor>.<patch>.cmake` for the named compiler in the compiler root, the folder named second: the one `CMSIS_COMPILER_ROOT` points to, else the `etc` folder of the CMSIS-Toolbox installation (empty when that folder does not exist). Either the name has no such file there (a `compiler:` value or a registered `<name>_TOOLCHAIN_<major>_<minor>_<patch>` environment variable with a name the installation does not support), `CMSIS_COMPILER_ROOT` points to a folder without these files, or a fixed version (`compiler: <name>@<version>`) is older than every file for that compiler.

## Fix

Use a compiler name the installation has a toolchain file for (AC6, GCC, IAR or CLANG) in `compiler:` and in the `*_TOOLCHAIN_*` environment variables; if `CMSIS_COMPILER_ROOT` is set, point it to the CMSIS-Toolbox `etc` folder that holds the `*.cmake` toolchain files. For a fixed version, use one that is not older than the toolchain files there, or a minimum version (`<name>@>=<version>`).

## Trigger in the source

```cpp
if (!found) {
```

## Note

Printed once, after the contexts were processed; the context itself goes on with the version from `compiler:`. `csolution list toolchains` prints it for a registered environment variable with an unknown name (unit test with UNKNOWN_TOOLCHAIN_1_2_3).

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:5442-5473`
- `tools/projmgr/src/ProjMgrWorker.cpp:5430-5440`
- `tools/projmgr/src/ProjMgrUtils.cpp:199-212`
- `tools/projmgr/src/ProjMgrWorker.cpp:1948-1951`
- `tools/projmgr/src/ProjMgrWorker.cpp:5395-5411`
- `tools/projmgr/src/ProjMgrWorker.cpp:5004-5019`
- `libs/rteutils/src/VersionCmp.cpp:165-187`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:2158-2190`
- `tools/projmgr/test/src/ProjMgrWorkerUnitTests.cpp:68-92`
