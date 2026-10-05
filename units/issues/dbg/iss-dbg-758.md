---
id: "iss-dbg-758"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: CMSIS Load fails with SWD \"No ACK\" on Infineon T2G after a pyOCD update"
summary: "pyOCD now does a hardware reset after load."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/758"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/758"
resolution: "fixed-in-release"
versions: "CMSIS Debugger 1.3.0 affected; 0.45 more robust"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "family": ["T2G-B-H"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

pyOCD now does a hardware reset after load. The ResetHardware sequence of the DFP breaks the debug connection, so closing the connection reports an error although programming worked.

## Fix

Set a different post-load reset in the solution, for example under target-set/debugger: load-setup: post-reset: system. pyOCD 0.45 also copes with this better; the DFP sequence should be corrected.

## Source

Resolution: fixed-in-release

Versions: CMSIS Debugger 1.3.0 affected; 0.45 more robust

From [Open-CMSIS-Pack/vscode-cmsis-debugger #758](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/758), summarized in own words; confidence high, not reviewed yet.
