---
id: "iss-dbg-520"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: HE core on Alif E7 does not start after flashing"
summary: "pyOCD did not apply a hardware reset after flashing; the maintainers expected the missing clean post-load state to be why the HE core did not start."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/520"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/520"
resolution: "fixed-in-release"
versions: "fixed in pyOCD 0.40 and CMSIS Debugger 1.2.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["Alif E7"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

pyOCD did not apply a hardware reset after flashing; the maintainers expected the missing clean post-load state to be why the HE core did not start.

## Fix

Use pyOCD 0.40 / CMSIS Debugger 1.2.0 or later (reset catch on all cores, no implicit resets between images, hardware reset after flashing).

## Source

Resolution: fixed-in-release

Versions: fixed in pyOCD 0.40 and CMSIS Debugger 1.2.0

From [Open-CMSIS-Pack/vscode-cmsis-debugger #520](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/520), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
