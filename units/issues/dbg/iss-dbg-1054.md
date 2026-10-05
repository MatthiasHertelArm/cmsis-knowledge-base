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
versions: "0.44.1 and earlier fine, 0.45.0 affected"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["Nuvoton M55M1"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

pyOCD 0.45.0 rejects a flash algorithm whose RAMstart lies outside every explicit RAM region of the pack description. The algorithm is dropped and the flash region ends up without a flash instance, although the address is valid RAM on the device.

## Fix

Use a pyOCD build with the relaxed check (pyOCD PR 2012, shipped in the CMSIS Debugger nightly and later releases). Alternatively the DFP can declare a memory element that covers the algorithm RAM.

## Source

Resolution: fixed-in-release

Versions: 0.44.1 and earlier fine, 0.45.0 affected

From [Open-CMSIS-Pack/vscode-cmsis-debugger #1054](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1054), summarized in own words; confidence high, not reviewed yet.
