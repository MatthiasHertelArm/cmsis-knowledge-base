---
id: "ts-csolution-command-was-not-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: <command> was not found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["<command> was not found"]
symptom_regex: "^<command> was not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:407"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "ProjMgr::ProcessCommands dispatches on m_command, which is the subcommand taken from the csolution command line."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:369-374", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:398-409"]
---

## Symptom

`<command> was not found`

## Cause

ProjMgr::ProcessCommands dispatches on m_command, which is the subcommand taken from the csolution command line. It handles list, check, update-rte, convert, run and rpc. Any other value falls through to the final else branch, which prints the message. The message text is a literal string in the source, so the tool prints the placeholder '<command>' and never the name the user typed.

## Fix

Run csolution with one of the supported subcommands: list, check, update-rte, convert, run or rpc. For example, 'csolution list packs' or 'csolution convert ...'. Check the spelling of the subcommand you passed, since the message does not show which value was rejected.

## Trigger in the source

```cpp
if (!m_rpcServer.Run()) {
```

## Note

The message is printed verbatim with the literal placeholder '<command>', so the user never sees the rejected name. The lines given do not show ParseCommandLine, so an earlier check that could reject an unknown subcommand is not visible here. The fix assumes the user typed a wrong or unsupported subcommand. The message text itself may be worth fixing to include the actual command name.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:369-374`
- `tools/projmgr/src/ProjMgr.cpp:398-409`
