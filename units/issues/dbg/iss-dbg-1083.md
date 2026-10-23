---
id: "iss-dbg-1083"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: PIC32CM device halts after Load and Run because the pack's post-flash reset halts the CPU"
summary: "The reporter reads the PDSC reset after flashing (line 300 of Microchip::PIC32CM-PL_DFP@1.5.437) as forcing a CPU halt, so the device stops after Load and Run; this is not confirmed."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1083"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1083"
resolution: "unresolved"
versions: "Affects Microchip::PIC32CM-PL_DFP 1.5.437; pyOCD 1.10.0 support expected."
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
checked: "unsupported"
applies_to: {"tool": ["pyocd"], "device": ["PIC32CM6408PL10048"], "pack": ["Microchip::PIC32CM-PL_DFP"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The reporter reads the PDSC reset after flashing (line 300 of Microchip::PIC32CM-PL_DFP@1.5.437) as forcing a CPU halt, so the device stops after Load and Run; this is not confirmed. The debug description spec does not yet cover this case, and a spec proposal (Open-CMSIS-Pack-Spec issue 417) is awaiting review.

## Fix

No fix is confirmed. Resolution depends on the debug description spec change (Open-CMSIS-Pack-Spec PR 419) and on pyOCD provisions expected with 1.10.0, followed by a DFP update; full verification may only happen after release.

## Source

Resolution: unresolved

Versions: Affects Microchip::PIC32CM-PL_DFP 1.5.437; pyOCD 1.10.0 support expected.

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/vscode-cmsis-debugger #1083](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1083), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
