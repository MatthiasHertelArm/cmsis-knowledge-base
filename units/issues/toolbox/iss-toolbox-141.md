---
id: "iss-toolbox-141"
type: "troubleshooting"
domain: "pack"
title: "svdconv: svdconv --generate=sfr does nothing on Linux or macOS"
summary: "The SFR output needs the Windows-only SfrCC2 tool from Keil MDK; svdconv silently skipped it elsewhere."
status: "draft"
tool: "svdconv"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/141"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/141"
resolution: "fixed-in-release"
versions: "fixed in svdconv 3.3.51"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["svdconv"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The SFR output needs the Windows-only SfrCC2 tool from Keil MDK; svdconv silently skipped it elsewhere.

## Fix

Generate SFR files on Windows only. svdconv 3.3.51 now reports an error with exit code 2 on other systems; SFD generation works everywhere.

## Source

Resolution: fixed-in-release

Versions: fixed in svdconv 3.3.51

From [Open-CMSIS-Pack/cmsis-toolbox #141](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/141), summarized in own words; confidence high, checked against the thread, not reviewed yet.
