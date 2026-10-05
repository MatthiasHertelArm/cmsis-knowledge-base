---
id: "iss-dbg-882"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: RTT broken on single-core devices when control block is found by ELF symbol"
summary: "pyOCD handled the pname of a single-core target wrongly, so the lookup of the RTT control block by its ELF symbol failed."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/882"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/882"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

pyOCD handled the pname of a single-core target wrongly, so the lookup of the RTT control block by its ELF symbol failed.

## Fix

Update to pyOCD 0.43.1 / CMSIS Debugger 1.4.1 or later, which contain pyOCD PR #1923.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #882](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/882), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
