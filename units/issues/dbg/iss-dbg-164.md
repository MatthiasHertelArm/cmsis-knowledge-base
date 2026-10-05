---
id: "iss-dbg-164"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Attach again to the same core fails after detaching"
summary: "pyOCD gdbserver exits after the client disconnects unless --persist is given."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/164"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/164"
resolution: "configuration"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

pyOCD gdbserver exits after the client disconnects unless --persist is given.

## Fix

Add --persist to the pyOCD gdbserver arguments; the maintainers planned to add it to the launch and tasks templates.

## Source

Resolution: configuration

From [Open-CMSIS-Pack/vscode-cmsis-debugger #164](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/164), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
