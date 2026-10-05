---
id: "ts-csolution-contains-more-than-one"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: '…' contains more than one '… file, PLM may fail"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["'<…>' contains more than one '<…> file, PLM may fail"]
symptom_regex: "^'.+?' contains more than one '.+? file, PLM may fail$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrCbuild.cpp:252"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The RTE folder of a component configuration file (for example RTE/Device/<device>/startup_<device>.c) holds more than one backup with the same prefix, such as two `<file>.base@<version>` or two `<file>.update@<version>` files."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrCbuild.cpp:235-261", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrCbuild.cpp:191-196", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteProject.cpp:646-668", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteProject.cpp:714-725", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteProject.cpp:1087-1092", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2425"]
---

## Symptom

`'<…>' contains more than one '<…> file, PLM may fail`

## Cause

The RTE folder of a component configuration file (for example RTE/Device/<device>/startup_<device>.c) holds more than one backup with the same prefix, such as two `<file>.base@<version>` or two `<file>.update@<version>` files. The first `<…>` is that folder, the second the prefix (`<file>.base` or `<file>.update`); csolution writes the first match into the cbuild.yml, so the PLM status reported for the file may be wrong.

## Fix

Keep only the backup whose version is the file's current base version (normally the highest) and delete the stale `.base@`/`.update@` copies, or run `csolution update-rte <name>.csolution.yml`, which deletes redundant backups when it updates the RTE files. Such leftovers usually come from copying RTE folders or from merges in version control.

## Trigger in the source

```cpp
if (backupFiles.size() > 1) {
```

## Note

Source comment says the condition 'should never be triggered'; update-rte keeps only file.base@<highest version> and the matching update file. No test reproduces it. The message lacks the closing quote after the prefix.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrCbuild.cpp:235-261`
- `tools/projmgr/src/ProjMgrCbuild.cpp:191-196`
- `libs/rtemodel/src/RteProject.cpp:646-668`
- `libs/rtemodel/src/RteProject.cpp:714-725`
- `libs/rtemodel/src/RteProject.cpp:1087-1092`
- `tools/projmgr/src/ProjMgrWorker.cpp:2425`
