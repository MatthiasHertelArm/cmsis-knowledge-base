---
id: "ts-csolution-command-line-options-quiet-and-verbose-are-mutua"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: command line options '--quiet' and '--verbose' are mutually exclusive"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["command line options '--quiet' and '--verbose' are mutually exclusive"]
symptom_regex: "^command line options '\\-\\-quiet' and '\\-\\-verbose' are mutually exclusive$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:332"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "Both `--quiet`/`-q` and `--verbose`/`-v` were given on the csolution command line (for example passed through by cbuild); they contradict each other."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:330-334", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:7894-7907"]
---

## Symptom

`command line options '--quiet' and '--verbose' are mutually exclusive`

## Cause

Both `--quiet`/`-q` and `--verbose`/`-v` were given on the csolution command line (for example passed through by cbuild); they contradict each other.

## Fix

Remove one of the two options.

## Trigger in the source

```cpp
if (ProjMgrLogger::m_quiet && ProjMgrLogger::m_verbose) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:330-334`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:7894-7907`
