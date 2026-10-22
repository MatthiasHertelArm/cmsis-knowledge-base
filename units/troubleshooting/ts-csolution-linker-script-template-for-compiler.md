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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:2462"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "csolution looks for a default linker script template when the context has no linker script set and it is not a dry run."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2449-2451", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2454-2460", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2461-2464"]
---

## Symptom

`linker script template for compiler '<…>' was not found`

## Cause

csolution looks for a default linker script template when the context has no linker script set and it is not a dry run. It walks the compiler root directory recursively and matches a file whose double-stem equals '<toolchain name>_linker_script' (case-insensitive). The message is printed when no such file exists under the compiler root, so the toolchain named in the context (the '<...>' part of the message) has no bundled linker script template. In that case csolution does not set a linker script and returns without copying anything.

## Fix

Set the linker script explicitly in the csolution project (linker script entry of the build-type or project YAML) so csolution does not need a default template. Alternatively, check that the selected toolchain is installed in the expected compiler root, since a missing template in that root is what triggers the warning.

## Trigger in the source

```cpp
if (linkerScript.empty()) {
```

## Note

The message is a warning and processing continues without a linker script; the user-facing cause is my reading of the directory scan. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:2449-2451`
- `tools/projmgr/src/ProjMgrWorker.cpp:2454-2460`
- `tools/projmgr/src/ProjMgrWorker.cpp:2461-2464`
