---
id: "iss-dbg-1083"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Load and Run leaves PIC32CM6408PL10048 halted after flashing"
summary: "The reporter suspects that the reset after flashing in the PIC32CM-PL pack PDSC (around line 300) forces a CPU halt, so the program does not start after Load and Run."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1083"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1083"
resolution: "unresolved"
versions: "Reported against Microchip::PIC32CM-PL_DFP 1.5.437; pyOCD 1.10.0 is expected to carry the needed provisions."
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
checked: "unsupported"
applies_to: {"tool": ["cmsis-debugger", "pyocd"], "device": ["PIC32CM6408PL10048"], "pack": ["Microchip::PIC32CM-PL_DFP"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The reporter suspects that the reset after flashing in the PIC32CM-PL pack PDSC (around line 300) forces a CPU halt, so the program does not start after Load and Run. This is unconfirmed; the debug description spec requires an update to address it.

## Fix

No fix is confirmed. The thread expects a debug description spec change and pyOCD provisions in 1.10.0, followed by a matching DFP update, to resolve the problem; full verification may only happen after release.

## Source

Resolution: unresolved

Versions: Reported against Microchip::PIC32CM-PL_DFP 1.5.437; pyOCD 1.10.0 is expected to carry the needed provisions.

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/vscode-cmsis-debugger #1083](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1083), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
