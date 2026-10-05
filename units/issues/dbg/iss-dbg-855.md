---
id: "iss-dbg-855"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: App does not resume from main() with Serial Monitor open (Nu-Link2 probe)"
summary: "The behaviour came from the Nu-Link2 debug probe firmware, not from the extension."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/855"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/855"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cmsis-debugger"], "device": ["Nuvoton M55M1"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The behaviour came from the Nu-Link2 debug probe firmware, not from the extension.

## Fix

Update the Nu-Link2 firmware to the latest release from Nuvoton.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/vscode-cmsis-debugger #855](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/855), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
