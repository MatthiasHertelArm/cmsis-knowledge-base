---
id: "ts-csolution-compiler-undefined-use-toolchain-option-or-add-c"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: compiler undefined, use '--toolchain' option or add 'compiler: <value>' to yml input…, selectable …"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["compiler undefined, use '--toolchain' option or add 'compiler: <value>' to yml input<…>, selectable values can be found in cbuild-idx.yml<…>"]
symptom_regex: "^compiler undefined, use '\\-\\-toolchain' option or add 'compiler: <value>' to yml input.*$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:6061"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "No compiler is set for the context: neither the cproject.yml, the csolution.yml, the target-type or build-type, a clayer.yml nor the `--toolchain` option gives `compiler:`, and cdefault.yml has none either, so csolution cannot choose a toolchain and the context fails."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1908-1931", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3080-3102", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:6037-6064", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:6066-6091", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrCbuildIdx.cpp:84-91", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:386-389", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:6669-6684"]
---

## Symptom

`compiler undefined, use '--toolchain' option or add 'compiler: <value>' to yml input<…>, selectable values can be found in cbuild-idx.yml<…>`

## Cause

No compiler is set for the context: neither the cproject.yml, the csolution.yml, the target-type or build-type, a clayer.yml nor the `--toolchain` option gives `compiler:`, and cdefault.yml has none either, so csolution cannot choose a toolchain and the context fails. The message is printed once, after all contexts were processed. It ends with `, selectable values can be found in cbuild-idx.yml` when `select-compiler:` in the csolution.yml or cdefault.yml lists a compiler whose version range a registered toolchain meets; those compilers are then written under `select-compiler:` in the cbuild-idx.yml, and `csolution convert` exits with its code for an undefined compiler.

## Fix

Add `compiler:` with AC6, GCC, IAR or CLANG, optionally with a version (`compiler: GCC`, `compiler: AC6@>=6.18.0`), to the csolution.yml (or to the cproject.yml, a target-type or build-type, or cdefault.yml), or pass `--toolchain <compiler>`. When the message names cbuild-idx.yml, take one of the values listed under `select-compiler:` there.

## Trigger in the source

```cpp
if (m_undefCompiler) {
```

## Note

Printed after the contexts were processed, so `processing context '…' failed` for an affected context can come before it. With `csolution setup` and a `select-compiler:` list in the csolution.yml, the first selectable compiler that is registered is used instead and the message does not appear.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:1908-1931`
- `tools/projmgr/src/ProjMgrWorker.cpp:3080-3102`
- `tools/projmgr/src/ProjMgrWorker.cpp:6037-6064`
- `tools/projmgr/src/ProjMgrWorker.cpp:6066-6091`
- `tools/projmgr/src/ProjMgrCbuildIdx.cpp:84-91`
- `tools/projmgr/src/ProjMgr.cpp:386-389`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:6669-6684`
