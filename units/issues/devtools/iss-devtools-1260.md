---
id: "iss-devtools-1260"
type: "troubleshooting"
domain: "project"
title: "cbuild: CMake configuration step takes minutes with Arm Compiler 6"
summary: "Most likely latency of the floating license server used with Arm Compiler 6 during CMake's compiler identification; with GCC configuration takes about 3 s."
status: "draft"
tool: "cbuild"
symptoms: ["-- Configuring done (188.5s)"]
symptom_regex: "\\-\\-\\s+Configuring\\s+done\\s+\\(\\S+\\.5s\\)"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1260"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1260"
resolution: "configuration"
versions: "CMSIS-Toolbox 2.1.0, AC6 6.19.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild"], "toolchain": ["AC6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`-- Configuring done (188.5s)`

## Cause

Most likely latency of the floating license server used with Arm Compiler 6 during CMake's compiler identification; with GCC configuration takes about 3 s.

## Fix

MDK v6 uses user-based licensing, with which this latency should not appear any more. Compiler detection can be skipped, and CMake caches the configuration so later runs are faster.

## Source

Resolution: configuration

Versions: CMSIS-Toolbox 2.1.0, AC6 6.19.0

From [Open-CMSIS-Pack/devtools #1260](https://github.com/Open-CMSIS-Pack/devtools/issues/1260), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
