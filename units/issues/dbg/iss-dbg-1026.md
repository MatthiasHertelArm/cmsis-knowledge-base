---
id: "iss-dbg-1026"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyOCD run prints RTT SWD/JTAG WAIT ACK errors although the test passes (Alif E8)"
summary: "The RTT worker polls target memory continuously."
status: "draft"
tool: "pyocd"
symptoms: ["0001754 E Error reading RTT up channel 1: SWD/JTAG communication failure (WAIT ACK) [rtt_server]", "0001754 E Error reading from RTT channel worker 1: SWD/JTAG communication failure (WAIT ACK) [rtt_server]"]
symptom_regex: "Error\\s+reading\\s+RTT\\s+up\\s+channel\\s+\\S+:\\s+SWD/JTAG\\s+communication\\s+failure\\s+\\(WAIT\\s+ACK\\)"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1026"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1026"
resolution: "not-a-bug"
versions: "pyOCD 0.44.1"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "family": ["Alif Ensemble E8"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0001754 E Error reading RTT up channel 1: SWD/JTAG communication failure (WAIT ACK) [rtt_server]`
`0001754 E Error reading from RTT channel worker 1: SWD/JTAG communication failure (WAIT ACK) [rtt_server]`

## Cause

The RTT worker polls target memory continuously. On Alif E8 parts a communication error can occur sporadically right after the target is reset and starts running; the failed iteration is abandoned and polling continues. The messages are real link errors, so they stay at error level.

## Fix

A single error after reset or a few sporadic ones are harmless apart from lower RTT bandwidth (SystemView data could overflow). If they keep appearing and RTT stops working, look at the debug link and the target side (for example the processor stubs programmed through the Alif SE tools). In CI, do not treat a lone error line as a test failure unless RTT output is missing.

## Source

Resolution: not-a-bug

Versions: pyOCD 0.44.1

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/vscode-cmsis-debugger #1026](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1026), summarized in own words; confidence medium, not reviewed yet.
