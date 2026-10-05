---
id: "iss-dbg-382"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: CMSIS-DAP v1 (HID) probes fail on macOS with \"already open\""
summary: "The libusb path timed out on HID probes on macOS, and the follow-up open raised."
status: "draft"
tool: "pyocd"
symptoms: ["0100505 C Error: already open [__main__]"]
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/382"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/382"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0100505 C Error: already open [__main__]`

## Cause

The libusb path timed out on HID probes on macOS, and the follow-up open raised.

## Fix

Use a pyOCD with the hidapi change (PR 1792), shipped from CMSIS Debugger 1.0.0.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #382](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/382), summarized in own words; confidence high, not reviewed yet.
