---
id: "iss-pyocd-1580"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd rtt cannot find the control block; using RTT with gdbserver needs monitor commands"
summary: "pyOCD's RTT control-block search only scans the first RAM region and a short range, so a block in a later RAM (for example 0x20002300 on LPC55S16, whose first RAM is code RAM) is not found. gdbserver has no preset, …"
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1580"
doc_source: "https://github.com/pyocd/pyOCD/issues/1580"
resolution: "workaround"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["LPC55S16"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

pyOCD's RTT control-block search only scans the first RAM region and a short range, so a block in a later RAM (for example 0x20002300 on LPC55S16, whose first RAM is code RAM) is not found. gdbserver has no preset, so RTT must be set up manually.

## Fix

Give pyocd rtt an explicit search address/size covering the RAM that holds _SEGGER_RTT. For gdbserver use: monitor rtt setup <address> <size> SEGGER RTT, monitor rtt start, monitor rtt server start <port> 0, monitor rtt channels, then connect with nc localhost <port>. Widening the default search range was planned.

## Source

Resolution: workaround

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1580](https://github.com/pyocd/pyOCD/issues/1580), summarized in own words; confidence medium, not reviewed yet.
