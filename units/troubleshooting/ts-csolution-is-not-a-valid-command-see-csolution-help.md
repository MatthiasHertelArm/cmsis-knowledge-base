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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:109"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:95-111", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:179-203", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:326-328", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:4530-4543"]
---

## Symptom

`'<…>' is not a valid command. See 'csolution --help'.`

## Cause

`-h`/`--help` was given together with a command or subcommand that csolution does not know, e.g. `csolution list invalid -h` or `csolution test -h`. The `<…>` is the command (and subcommand) as typed.

## Fix

Run `csolution --help` and use one of the listed commands, e.g. `csolution convert -h` or `csolution list packs -h`. Valid are convert, update-rte, run, rpc, check pack-updates and list with packs, boards, devices, npus, components, configs, dependencies, examples, templates, contexts, targets, target-sets, debuggers, generators, layers, toolchains or environment.

## Trigger in the source

```cpp
if (cmdOptionsDict.find(filter) == cmdOptionsDict.end()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:95-111`
- `tools/projmgr/src/ProjMgr.cpp:179-203`
- `tools/projmgr/src/ProjMgr.cpp:326-328`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:4530-4543`
