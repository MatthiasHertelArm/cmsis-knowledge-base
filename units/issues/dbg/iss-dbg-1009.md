---
id: "iss-dbg-1009"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd load: \"flash erase sector sequence not available\" with flashinfo plus FLM in DFP"
summary: "The generated cbuild-run file contains both a programming algorithm and a flash-info block for the same region."
status: "draft"
tool: "pyocd"
symptoms: ["0009000 W flash uninit sequence not available [flash_dsq]", "0009000 W flash init sequence not available [flash_dsq]", "0009003 C flash erase sector sequence not available (address 0x0804a000) [__main__]"]
symptom_regex: "flash\\s+uninit\\s+sequence\\s+not\\s+available"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1009"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1009"
resolution: "fixed-in-release"
versions: "pyOCD 0.44 and later until the fallback"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["STM32C562RETx"], "core": ["Cortex-M33"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0009000 W flash uninit sequence not available [flash_dsq]`
`0009000 W flash init sequence not available [flash_dsq]`
`0009003 C flash erase sector sequence not available (address 0x0804a000) [__main__]`

## Cause

The generated cbuild-run file contains both a programming algorithm and a flash-info block for the same region. From pyOCD 0.44 on the flash-info block wins and selects the debug-sequence flash backend, but the DFP defined no flash debug sequences, so programming aborts although a working FLM was present.

## Fix

Use a pyOCD that falls back to the algorithm when no flash sequences exist (CMSIS Debugger nightly from mid-June 2026, then the next release). Older workaround: delete the flash-info block from the cbuild-run file. A pack should not declare flashinfo without matching sequences.

## Source

Resolution: fixed-in-release

Versions: pyOCD 0.44 and later until the fallback

From [Open-CMSIS-Pack/vscode-cmsis-debugger #1009](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1009), summarized in own words; confidence high, not reviewed yet.
