---
id: "ts-csolution-too-many-command-line-arguments"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: too many command line arguments"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["too many command line arguments"]
symptom_regex: "^too many command line arguments$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:322"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The command-line parser reported arguments that it could not assign to an option or to the positional arguments."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:320", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:214", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:257"]
---

## Symptom

`too many command line arguments`

## Cause

The command-line parser reported arguments that it could not assign to an option or to the positional arguments.

## Fix

Remove stray words from the command line and quote values that contain spaces; `csolution <command> -h` lists the valid options.

## Trigger in the source

```cpp
if (!parseResult.unmatched().empty()) {
```

## Note

All positional words go into one catch-all list, of which csolution uses the solution file, the command and its first argument and silently ignores the rest, so this check is hard to reach; no test covers it. The cxxopts submodule was not checked out to confirm when unmatched() is non-empty.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:320`
- `tools/projmgr/src/ProjMgr.cpp:214`
- `tools/projmgr/src/ProjMgr.cpp:257`
