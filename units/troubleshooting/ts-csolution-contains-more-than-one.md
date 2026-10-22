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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrCbuild.cpp:252"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "When csolution writes the cbuild file, SetPLMStatus looks for PLM backup files next to each configuration file (for example Name.h, Name.h.base@<stamp> and Name.h.update@<stamp>)."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrCbuild.cpp:240-247", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrCbuild.cpp:249-256", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrCbuild.cpp:260-261"]
---

## Symptom

`'<…>' contains more than one '<…> file, PLM may fail`

## Cause

When csolution writes the cbuild file, SetPLMStatus looks for PLM backup files next to each configuration file (for example Name.h, Name.h.base@<stamp> and Name.h.update@<stamp>). The GetBackupFile lambda lists every entry in the file's directory matching the pattern '<name>.base@*' or '<name>.update@*'. If that listing returns more than one file, the warning prints the directory and the filter (the text after the placeholder reads '<filter> file'). The code takes the first match as the backup and continues, so PLM state can be wrong for that file.

## Fix

Open the directory named in the message and list the files whose names start with the configuration file name followed by .base@ or .update@. Keep one .base@ and one .update@ file for that configuration file, delete the surplus copies, then run the csolution build again. The source does not describe how the extra backups get created, so if they reappear, investigate what writes them.

## Trigger in the source

```cpp
if (backupFiles.size() > 1) {
```

## Note

The source comment says this safeguard should never be triggered, so the message may be hard to reach in practice. The printed text has an unbalanced quote: the filter is followed by ' file' with no closing quote. The message names the directory, not the configuration file, and the printed filter includes the .base or .update suffix. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrCbuild.cpp:240-247`
- `tools/projmgr/src/ProjMgrCbuild.cpp:249-256`
- `tools/projmgr/src/ProjMgrCbuild.cpp:260-261`
