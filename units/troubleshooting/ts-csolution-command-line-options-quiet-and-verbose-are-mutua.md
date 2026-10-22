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
summary: "The csolution command line was given both --quiet and --verbose."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:331-334", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:326-328"]
---

## Symptom

`command line options '--quiet' and '--verbose' are mutually exclusive`

## Cause

The csolution command line was given both --quiet and --verbose. Both flags set static logger flags (ProjMgrLogger::m_quiet and ProjMgrLogger::m_verbose) during option parsing, and after parsing finishes the code rejects the combination because the two logging levels cannot apply at once. The check runs after the help option is handled and before the load policy is set.

## Fix

Run the command with only one of the two options: keep --quiet for minimal output or --verbose for detailed output, and remove the other from the command line or from any wrapper script or build step that adds it.

## Trigger in the source

```cpp
if (ProjMgrLogger::m_quiet && ProjMgrLogger::m_verbose) {
```

## Note

The lines shown do not include where m_quiet and m_verbose are set, so the claim that each flag comes from its command line option rests on the message text and the variable names. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:331-334`
- `tools/projmgr/src/ProjMgr.cpp:326-328`
