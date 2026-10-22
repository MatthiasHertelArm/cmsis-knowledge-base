---
id: "ts-csolution-csolution-file-not-specified"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: csolution file not specified"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["csolution file not specified"]
symptom_regex: "^csolution file not specified$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:537"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "PopulateContexts only parses a csolution when m_csolutionFile is non-empty."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:487-491", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:536-538"]
---

## Symptom

`csolution file not specified`

## Cause

PopulateContexts only parses a csolution when m_csolutionFile is non-empty. When it is empty, the tool logs this error and stops. The csolution file path was not set on the command line, so the tool has no solution file to load.

## Fix

Run csolution again and pass the path to your .csolution.yml file as the input. Check that the path is spelled correctly and that the file exists. The source lines shown do not name the exact command-line option, so confirm the syntax with the csolution help output.

## Note

The message has no file name or variable part. The check is on the path the tool stores, so it fires when no csolution file was given, not when the file is missing from disk. A missing file is reported by the parser instead.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:487-491`
- `tools/projmgr/src/ProjMgr.cpp:536-538`
