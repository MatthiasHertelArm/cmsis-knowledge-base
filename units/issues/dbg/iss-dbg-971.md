---
id: "iss-dbg-971"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd load exits 1 after a good flash because the post-load reset drops the connection"
summary: "The default post-load reset for cbuild-run targets is a hardware reset."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/971"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/971"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The default post-load reset for cbuild-run targets is a hardware reset. With the default ResetHardware sequence the debug connection can be lost right after it, the board uninit steps then fail, and load exits non-zero although programming worked; the CMSIS Load pre-launch task then shows an error pop-up.

## Fix

Use a pyOCD with PR 1971: a hardware post-load reset runs after board uninit, and for other reset types failures are reported as information with exit code 0 when flashing succeeded.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #971](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/971), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
