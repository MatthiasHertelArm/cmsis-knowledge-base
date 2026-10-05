---
id: "iss-dbg-701"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Connect mode pre-reset fails with ST-Link probes"
summary: "In pre-reset mode pyOCD ran its post-reset recovery on a device that was not yet connected, which the ST-Link rejects."
status: "draft"
tool: "pyocd"
symptoms: ["0000735 C STLink error (66): Unknown command [__main__]"]
symptom_regex: "STLink\\s+error\\s+\\(\\S+\\):\\s+Unknown\\s+command"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/701"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/701"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["STM32H743ZITx"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0000735 C STLink error (66): Unknown command [__main__]`

## Cause

In pre-reset mode pyOCD ran its post-reset recovery on a device that was not yet connected, which the ST-Link rejects.

## Fix

Use a pyOCD with PR 2036.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #701](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/701), summarized in own words; confidence high, not reviewed yet.
