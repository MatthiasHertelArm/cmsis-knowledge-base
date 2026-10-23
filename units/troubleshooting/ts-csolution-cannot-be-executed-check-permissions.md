---
id: "ts-csolution-cannot-be-executed-check-permissions"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: generator file '…' cannot be executed, check permissions"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["generator file '<…>' cannot be executed, check permissions"]
symptom_regex: "^generator file '.+?' cannot be executed, check permissions$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:5156"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The pack generator's executable exists but is not executable for the current user, e.g. a script in the pack without its execute bit after unpacking on Linux/macOS."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5155-5158", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrGeneratorUnitTests.cpp:127-145", "Open-CMSIS-Pack/devtools@30f5e817:test/packs/ARM/RteTestGenerator/0.1.0/ARM.RteTestGenerator.pdsc:89-107"]
---

## Symptom

`generator file '<…>' cannot be executed, check permissions`

## Cause

The pack generator's executable exists but is not executable for the current user, e.g. a script in the pack without its execute bit after unpacking on Linux/macOS. The `<…>` is the file path. The cbuild-gen.yml input file has already been written at this point.

## Fix

Make the file executable, e.g. `chmod +x "<path>"`, or reinstall the pack; then run the generator again.

## Trigger in the source

```cpp
if (!RteFsUtils::IsExecutableFile(generatorExe)) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:5155-5158`
- `tools/projmgr/test/src/ProjMgrGeneratorUnitTests.cpp:127-145`
- `test/packs/ARM/RteTestGenerator/0.1.0/ARM.RteTestGenerator.pdsc:89-107`
