---
id: "iss-dbg-882"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: RTT broken on single-core devices when control block is found by ELF symbol"
summary: "pyOCD handled the pname of a single-core target wrongly, so the symbol lookup of the RTT control block in the ELF failed."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/882"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/882"
resolution: "fixed-in-release"
versions: "fixed in pyOCD 0.43.1"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

pyOCD handled the pname of a single-core target wrongly, so the symbol lookup of the RTT control block in the ELF failed.

## Fix

Update to pyOCD 0.43.1 / CMSIS Debugger 1.4.1 or later; as an alternative give the control block address explicitly.

## Source

Resolution: fixed-in-release

Versions: fixed in pyOCD 0.43.1

From [Open-CMSIS-Pack/vscode-cmsis-debugger #882](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/882), summarized in own words; confidence high, not reviewed yet.
