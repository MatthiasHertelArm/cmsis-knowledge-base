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
versions: "pyOCD 0.44 and 0.45"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The default post-load reset for cbuild-run targets is a hardware reset. With a default or faulty ResetHardware sequence the debug connection is lost right after, the board uninit steps fail, and load returns non-zero although programming worked; the CMSIS Load pre-launch task then shows an error pop-up.

## Fix

Use a pyOCD with PR 1971 (hardware reset done after uninit; other reset types only report problems as information and exit 0). Or choose the reset type via load-setup post-reset in the solution.

## Source

Resolution: fixed-in-release

Versions: pyOCD 0.44 and 0.45

From [Open-CMSIS-Pack/vscode-cmsis-debugger #971](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/971), summarized in own words; confidence high, not reviewed yet.
