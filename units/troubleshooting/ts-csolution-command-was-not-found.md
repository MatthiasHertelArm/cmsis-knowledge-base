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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:407"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The first argument after `csolution` is not a known command (list, check, update-rte, convert, run, rpc), e.g. a typo such as `csolution conver ...`, or only a *.csolution.yml was given without a command."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:257-266", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:369-410"]
---

## Symptom

`<command> was not found`

## Cause

The first argument after `csolution` is not a known command (list, check, update-rte, convert, run, rpc), e.g. a typo such as `csolution conver ...`, or only a *.csolution.yml was given without a command. The text `<command>` is printed literally, not replaced by what was typed.

## Fix

Put a valid command before the options, e.g. `csolution convert <name>.csolution.yml`; `csolution --help` lists the commands.

## Trigger in the source

```cpp
if (!m_rpcServer.Run()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:257-266`
- `tools/projmgr/src/ProjMgr.cpp:369-410`
