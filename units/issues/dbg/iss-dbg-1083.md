---
id: "iss-dbg-1083"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Load and Run leaves PIC32CM device halted after flashing due to DFP reset sequence"
summary: "The reporter believes the reset after flashing, as defined in the device pack's PDSC (line 300 of Microchip::PIC32CM-PL_DFP@1.5.437), forces the CPU into a halt so the program does not start."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1083"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1083"
resolution: "unresolved"
versions: "Affected: PIC32CM-PL_DFP 1.5.437. Expected fix: pyOCD 1.10.0 together with a DFP update."
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-debugger"], "device": ["PIC32CM6408PL10048"], "pack": ["Microchip::PIC32CM-PL_DFP"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The reporter believes the reset after flashing, as defined in the device pack's PDSC (line 300 of Microchip::PIC32CM-PL_DFP@1.5.437), forces the CPU into a halt so the program does not start. The debug description specification needs an update for this case, and pyOCD needs support for it.

## Fix

No fix yet. The pack's debug sequence needs updating once the debug description spec change and matching pyOCD support are available (pyOCD 1.10.0 expected). Full verification may only come after release.

## Source

Resolution: unresolved

Versions: Affected: PIC32CM-PL_DFP 1.5.437. Expected fix: pyOCD 1.10.0 together with a DFP update.

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/vscode-cmsis-debugger #1083](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1083), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
