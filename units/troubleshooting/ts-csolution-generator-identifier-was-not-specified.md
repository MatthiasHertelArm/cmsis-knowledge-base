---
id: "ts-csolution-generator-identifier-was-not-specified"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: generator identifier was not specified"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["generator identifier was not specified"]
symptom_regex: "^generator identifier was not specified$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:1045"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution run reached the code generator path (RunCodeGenerator) without a generator identifier, so m_codeGenerator is empty."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:1042-1047"]
---

## Symptom

`generator identifier was not specified`

## Cause

The csolution run reached the code generator path (RunCodeGenerator) without a generator identifier, so m_codeGenerator is empty. The tool checks this before it parses any input, so the csolution.yml content is not the cause; the command line that selected the generator mode did not supply an identifier for the generator to run.

## Fix

Re-run the command and pass the generator identifier that the code generator mode expects, for example the identifier of a generator defined in your project's generator configuration. Check the csolution command help for the exact option that sets the generator identifier, since the source lines shown do not name it.

## Trigger in the source

```cpp
if (m_codeGenerator.empty()) {
```

## Note

The source lines show only the check and the error call; the option that fills m_codeGenerator is not in the given lines, so the exact option name is not stated here. The message text is missing the trailing period used by other messages, which is cosmetic only.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:1042-1047`
