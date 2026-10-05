---
id: "iss-devtools-1260"
type: "troubleshooting"
domain: "project"
title: "cbuild: CMake configuration step takes minutes with Arm Compiler 6"
summary: "Compiler detection runs armclang several times; with a floating-license (FlexNet) server each start waits for the license check, while GCC has no such delay."
status: "draft"
tool: "cbuild"
symptoms: ["-- Configuring done (188.5s)"]
symptom_regex: "\\-\\-\\s+Configuring\\s+done\\s+\\(\\S+\\.5s\\)"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1260"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1260"
resolution: "configuration"
versions: "toolbox 2.1.0, AC6 6.19"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild"], "toolchain": ["AC6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`-- Configuring done (188.5s)`

## Cause

Compiler detection runs armclang several times; with a floating-license (FlexNet) server each start waits for the license check, while GCC has no such delay.

## Fix

The latency comes from the license server, not from the toolbox. Arm Compiler in MDK v6 uses user-based licensing, which avoids it; CMake caches the result so later configures are faster.

## Source

Resolution: configuration

Versions: toolbox 2.1.0, AC6 6.19

From [Open-CMSIS-Pack/devtools #1260](https://github.com/Open-CMSIS-Pack/devtools/issues/1260), summarized in own words; confidence medium, not reviewed yet.
