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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:322"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "After cxxopts parses the csolution command line, ParseCommandLine finds arguments left in parseResult.unmatched() that match no declared option."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:262-264", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:266-267", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:320-324"]
---

## Symptom

`too many command line arguments`

## Cause

After cxxopts parses the csolution command line, ParseCommandLine finds arguments left in parseResult.unmatched() that match no declared option. The visible code only consumes the first positional argument into m_args (lines 262-264), so the extra arguments are typically surplus positional values or unknown options (for example a second path or a misspelled flag) that csolution does not accept.

## Fix

Run the command with only the arguments csolution defines: the command name, at most one positional argument if the command takes one, and options given by their declared names such as --solution. Remove the extra argument or fix the misspelled option, then run it again. Use the command's help output to check which options are valid.

## Trigger in the source

```cpp
if (!parseResult.unmatched().empty()) {
```

## Note

The lines given do not show the loop head or the parser setup, so the exact set of arguments that end up unmatched is inferred from the code that consumes positionals. The message has no code and is not documented in the README.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:262-264`
- `tools/projmgr/src/ProjMgr.cpp:266-267`
- `tools/projmgr/src/ProjMgr.cpp:320-324`
