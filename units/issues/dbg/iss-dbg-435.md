---
id: "iss-dbg-435"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Load fails with an empty critical error at 10 MHz debug clock on Alif E7 with ULINKplus"
summary: "The device answers memory requests slowly and SWD/JTAG returns WAIT; pyOCD gave up after too few retries."
status: "draft"
tool: "pyocd"
symptoms: ["0013264 C  [__main__]"]
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/435"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/435"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["AE722F80F55D5LS"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0013264 C  [__main__]`

## Cause

The device answers memory requests slowly and SWD/JTAG returns WAIT; pyOCD gave up after too few retries. Lower clocks merely hid it.

## Fix

Use a pyOCD with more WAIT retries (100, later 150) and better SWD/JTAG error texts; as a workaround reduce the debug clock to 5 MHz.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #435](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/435), summarized in own words; confidence high, not reviewed yet.
