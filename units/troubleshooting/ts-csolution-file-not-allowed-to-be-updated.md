---
id: "ts-csolution-file-not-allowed-to-be-updated"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: file not allowed to be updated"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["file not allowed to be updated"]
symptom_regex: "^file not allowed to be updated$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlEmitter.cpp:57"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlEmitter.cpp:55-58", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrCbuildPack.cpp:139-149", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:1265-1305"]
---

## Symptom

`file not allowed to be updated`

## Cause

`--frozen-packs` was given, and the packs csolution resolves for the solution differ from those locked in `<name>.cbuild-pack.yml` (e.g. a pack was added to or removed from packs:, or a version requirement changed), so the lock file would have to change. The message is prefixed with the cbuild-pack.yml path.

## Fix

Run once without `--frozen-packs` to update the cbuild-pack.yml and commit it, or change packs: back so that it matches the locked list.

## Trigger in the source

```cpp
if (!allowUpdate) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlEmitter.cpp:55-58`
- `tools/projmgr/src/ProjMgrCbuildPack.cpp:139-149`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:1265-1305`
