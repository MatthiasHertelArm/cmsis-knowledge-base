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
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgr.cpp:1045"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "`csolution run` was called without `-g`/`--generator <id>`."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:1042-1047"]
---

## Symptom

`generator identifier was not specified`

## Cause

`csolution run` was called without `-g`/`--generator <id>`.

## Fix

Add the generator id, e.g. `csolution run <name>.csolution.yml -g <generator-id> -c <context>`; `csolution list generators <name>.csolution.yml` shows the ids.

## Trigger in the source

```cpp
if (m_codeGenerator.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:1042-1047`
