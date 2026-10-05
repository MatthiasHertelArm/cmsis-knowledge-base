---
id: "iss-dbg-1054"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyOCD 0.45.0 skips flash algorithm when its RAM address is not a declared memory region"
summary: "pyOCD 0.45.0 rejects a flash algorithm whose RAMstart lies outside every explicit RAM region of the pack description."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1054"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1054"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["Nuvoton M55M1"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

pyOCD 0.45.0 rejects a flash algorithm whose RAMstart lies outside every explicit RAM region of the pack description. The algorithm is dropped and the flash region ends up without a flash instance, although the address is valid RAM on the device.

## Fix

Use a pyOCD with pyOCD PR 2012, tested in a CMSIS Debugger nightly build, where programming the M55M1 worked again.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #1054](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1054), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
