---
id: "iss-dbg-91"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: \"Zephyr kernel detected\" warning when debugging bare metal"
summary: "A newer pyOCD main change raised the warning without checking an RTOS."
status: "draft"
tool: "pyocd"
symptoms: ["0002477 W Zephyr kernel detected. Build your Zephyr application with `CONFIG_DEBUG_THREAD_INFO=y` to enable thread awareness. [zephyr]"]
symptom_regex: "Zephyr\\s+kernel\\s+detected\\.\\s+Build\\s+your\\s+Zephyr\\s+application\\s+with\\s+`.*?`\\s+to\\s+enable\\s+thread\\s+awareness\\."
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/91"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/91"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0002477 W Zephyr kernel detected. Build your Zephyr application with `CONFIG_DEBUG_THREAD_INFO=y` to enable thread awareness. [zephyr]`

## Cause

A newer pyOCD main change raised the warning without checking an RTOS.

## Fix

Use CMSIS Debugger 0.2+ pyOCD.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #91](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/91), summarized in own words; confidence high, not reviewed yet.
