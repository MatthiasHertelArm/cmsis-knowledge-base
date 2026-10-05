---
id: "iss-dbg-91"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: \"Zephyr kernel detected\" warning when debugging bare metal"
summary: "A change on pyOCD's main branch, newer than the last pip release, made the shipped pyOCD warn about a Zephyr kernel for bare-metal applications; with another RTOS such as RTX5 the warning did not appear."
status: "draft"
tool: "pyocd"
symptoms: ["0002477 W Zephyr kernel detected. Build your Zephyr application with `CONFIG_DEBUG_THREAD_INFO=y` to enable thread awareness. [zephyr]"]
symptom_regex: "Zephyr\\s+kernel\\s+detected\\.\\s+Build\\s+your\\s+Zephyr\\s+application\\s+with\\s+`.*?`\\s+to\\s+enable\\s+thread\\s+awareness\\."
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/91"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/91"
resolution: "fixed-in-release"
versions: "pyOCD v0.0.0-standalone-cbuild3"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0002477 W Zephyr kernel detected. Build your Zephyr application with `CONFIG_DEBUG_THREAD_INFO=y` to enable thread awareness. [zephyr]`

## Cause

A change on pyOCD's main branch, newer than the last pip release, made the shipped pyOCD warn about a Zephyr kernel for bare-metal applications; with another RTOS such as RTX5 the warning did not appear.

## Fix

Use a pyOCD from the standalone build v0.0.0-standalone-cbuild3 or later, which addresses it.

## Source

Resolution: fixed-in-release

Versions: pyOCD v0.0.0-standalone-cbuild3

From [Open-CMSIS-Pack/vscode-cmsis-debugger #91](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/91), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
