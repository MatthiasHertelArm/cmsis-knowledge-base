---
id: "iss-dbg-370"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Unclear errors \"No ACK received\" and empty \"Error:\" when probe or target is missing"
summary: "pyOCD printed bare SWD/JTAG status for typical wiring or clock problems."
status: "draft"
tool: "pyocd"
symptoms: ["0001410 C No ACK received [__main__]", "0019032 C Error:  [__main__]"]
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/370"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/370"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0001410 C No ACK received [__main__]`
`0019032 C Error:  [__main__]`

## Cause

pyOCD printed bare SWD/JTAG status for typical wiring or clock problems.

## Fix

Use a pyOCD with PR 1804 and the follow-up commit that adds the hint to the unexpected-ACK case: messages read like 'SWD/JTAG communication failure (No ACK received); check USB cable, reduce debugger clock'. Check the USB cable and lower the debug clock. A probe connected while pyOCD waits for it is now picked up.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #370](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/370), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
