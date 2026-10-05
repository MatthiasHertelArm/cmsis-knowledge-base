---
id: "iss-dbg-435"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Load fails with an empty critical error at 10 MHz debug clock on Alif E7 with ULINKplus"
summary: "The Alif E7 needs extra time for memory requests, so SWD/JTAG answers WAIT, and pyOCD gave up after too few retries; a lower clock only lengthened the communication so that fewer retries were needed."
status: "draft"
tool: "pyocd"
symptoms: ["0013264 C  [__main__]"]
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/435"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/435"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["AE722F80F55D5LS"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0013264 C  [__main__]`

## Cause

The Alif E7 needs extra time for memory requests, so SWD/JTAG answers WAIT, and pyOCD gave up after too few retries; a lower clock only lengthened the communication so that fewer retries were needed. Programming through the HP core still needed more than 100 retries.

## Fix

Use a pyOCD build with more WAIT retries (PR 1806: 100, later raised to 150) and the clearer SWD/JTAG error messages of PR 1804; no release is named. Workaround: reduce the debug clock to 5 MHz.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/vscode-cmsis-debugger #435](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/435), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
