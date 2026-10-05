---
id: "iss-dbg-1026"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyOCD run prints RTT SWD/JTAG WAIT ACK errors although the test passes (Alif E8)"
summary: "pyOCD reads the RTT buffers continuously."
status: "draft"
tool: "pyocd"
symptoms: ["0001754 E Error reading RTT up channel 1: SWD/JTAG communication failure (WAIT ACK) [rtt_server]", "0001754 E Error reading from RTT channel worker 1: SWD/JTAG communication failure (WAIT ACK) [rtt_server]"]
symptom_regex: "Error\\s+reading\\s+RTT\\s+up\\s+channel\\s+\\S+:\\s+SWD/JTAG\\s+communication\\s+failure\\s+\\(WAIT\\s+ACK\\)"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1026"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1026"
resolution: "not-a-bug"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "family": ["Alif Ensemble E8"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0001754 E Error reading RTT up channel 1: SWD/JTAG communication failure (WAIT ACK) [rtt_server]`
`0001754 E Error reading from RTT channel worker 1: SWD/JTAG communication failure (WAIT ACK) [rtt_server]`

## Cause

pyOCD reads the RTT buffers continuously. On Alif E8 SWD/JTAG WAIT errors tend to occur sporadically just after the target is reset and starts running, also influenced by the processor stubs programmed with the Alif SE tools; a failed iteration is dropped and RTT processing continues.

## Fix

A single error after reset or a few sporadic ones are usually not critical and only lower the RTT bandwidth (SystemView data can overflow); persistent errors mean RTT no longer works and point to the target or the debug link. The maintainers planned to check whether pyocd run can report it as a warning.

## Source

Resolution: not-a-bug

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/vscode-cmsis-debugger #1026](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1026), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
