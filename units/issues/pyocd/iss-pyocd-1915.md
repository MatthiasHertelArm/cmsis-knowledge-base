---
id: "iss-pyocd-1915"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: RTT config node in pyocd.yaml opens no port with pyocd gdbserver"
summary: "The rtt: configuration node is only honoured by pyocd run, not by pyocd gdbserver, so no RTT server port is ever opened."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1915"
doc_source: "https://github.com/pyocd/pyOCD/issues/1915"
resolution: "workaround"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The rtt: configuration node is only honoured by pyocd run, not by pyocd gdbserver, so no RTT server port is ever opened. Running RTT independently of a GDB client was also not supported by the remote probe server.

## Fix

With gdbserver, set RTT up through the GDB monitor commands after connecting: monitor rtt setup <control-block address> <search size> SEGGER RTT, then monitor rtt start, monitor rtt channels and monitor rtt server start <port> <channel>. Config-file support for gdbserver was announced for a later release.

## Source

Resolution: workaround

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1915](https://github.com/pyocd/pyOCD/issues/1915), summarized in own words; confidence medium, not reviewed yet.
