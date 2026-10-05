---
id: "iss-dbg-1009"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd load: \"flash erase sector sequence not available\" with flashinfo plus FLM in DFP"
summary: "The generated cbuild-run file contains both a programming algorithm and a flash-info block for the same region. pyOCD 0.44 and later prefers the flash-info block and selects the debug-sequence flash backend, but stm32c5xx_dfp 2.0.0 defines no flash debug sequences, …"
status: "draft"
tool: "pyocd"
symptoms: ["0009000 W flash uninit sequence not available [flash_dsq]", "0009000 W flash init sequence not available [flash_dsq]", "0009003 C flash erase sector sequence not available (address 0x0804a000) [__main__]"]
symptom_regex: "flash\\s+uninit\\s+sequence\\s+not\\s+available"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1009"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1009"
resolution: "fixed-in-release"
versions: "pyOCD 0.44 and later until the fallback; stm32c5xx_dfp 2.0.0; CMSIS-Toolbox 2.13.0; fallback in the CMSIS Debugger nightly of 2026-06-16"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["STM32C562RETx"], "core": ["Cortex-M33"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0009000 W flash uninit sequence not available [flash_dsq]`
`0009000 W flash init sequence not available [flash_dsq]`
`0009003 C flash erase sector sequence not available (address 0x0804a000) [__main__]`

## Cause

The generated cbuild-run file contains both a programming algorithm and a flash-info block for the same region. pyOCD 0.44 and later prefers the flash-info block and selects the debug-sequence flash backend, but stm32c5xx_dfp 2.0.0 defines no flash debug sequences, so programming aborts although a working FLM is present.

## Fix

Use a pyOCD that falls back to the algorithm when no flash sequences exist: it is in the CMSIS Debugger nightly of 2026-06-16, and the maintainers said the next pyOCD release works with the existing DFP. Older workaround: delete the flash-info block from the cbuild-run file. Whether a pack may declare flashinfo without flash sequences was disputed; the specification is to be clarified.

## Source

Resolution: fixed-in-release

Versions: pyOCD 0.44 and later until the fallback; stm32c5xx_dfp 2.0.0; CMSIS-Toolbox 2.13.0; fallback in the CMSIS Debugger nightly of 2026-06-16

From [Open-CMSIS-Pack/vscode-cmsis-debugger #1009](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1009), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
