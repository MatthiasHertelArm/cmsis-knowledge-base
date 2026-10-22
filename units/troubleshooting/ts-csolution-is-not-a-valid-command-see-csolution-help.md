---
id: "ts-csolution-is-not-a-valid-command-see-csolution-help"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: '…' is not a valid command. See 'csolution --help'."
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["'<…>' is not a valid command. See 'csolution --help'."]
symptom_regex: "^'.+?' is not a valid command\\. See 'csolution \\-\\-help'\\.$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:109"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "PrintUsage builds the command name from the arguments (cmd plus optional subCmd, e.g."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:107-111", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:65"]
---

## Symptom

`'<…>' is not a valid command. See 'csolution --help'.`

## Cause

PrintUsage builds the command name from the arguments (cmd plus optional subCmd, e.g. 'convert' or 'list packs') and looks it up in the dictionary of known commands; when the name is not found, it prints this error. The '<…>' in the message is the command text the user typed, so a misspelled or unsupported command or subcommand given to 'csolution -h' or a similar help request causes it.

## Fix

Check the spelling of the command and subcommand and run 'csolution --help' to list the valid commands, then use 'csolution <command> -h' for the options of a command. For example, correct the typed name to one shown in the list.

## Trigger in the source

```cpp
if (cmdOptionsDict.find(filter) == cmdOptionsDict.end()) {
```

## Note

The trigger is in PrintUsage, so the message appears when a help request names an unknown command; the source does not show which invocation path calls PrintUsage with a bad name, so the exact user action is inferred. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:107-111`
- `tools/projmgr/src/ProjMgr.cpp:65`
