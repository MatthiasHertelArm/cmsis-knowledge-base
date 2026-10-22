---
id: "ts-csolution-list-args-was-not-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: list <args> was not found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["list <args> was not found"]
symptom_regex: "^list <args> was not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:441"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution `list` command takes one subcommand word, which the tool stores in m_args."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:439-441", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:420-438"]
---

## Symptom

`list <args> was not found`

## Cause

The csolution `list` command takes one subcommand word, which the tool stores in m_args. The value the user gave is not one of the keys in the handler map built in ProcessListCommand, so the lookup fails and the tool prints this error. The message text is a literal string in the source, so the `<args>` in it does not show the value the user typed.

## Fix

Run `csolution list` with one of the supported subcommands: packs, boards, devices, npus, components, configs, dependencies, examples, templates, contexts, targets, target-sets, debuggers, generators, layers, toolchains or environment. For example: `csolution list packs`. Check the spelling of the word you passed; the match is exact and case-sensitive.

## Trigger in the source

```cpp
if (it == handlers.end()) {
```

## Note

The message does not repeat the unknown value, so the user has to compare their command with the list above. The sibling message at ProjMgr.cpp:415-418 covers the case where no subcommand is given. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:439-441`
- `tools/projmgr/src/ProjMgr.cpp:420-438`
