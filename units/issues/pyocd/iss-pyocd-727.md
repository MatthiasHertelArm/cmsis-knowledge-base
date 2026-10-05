---
id: "iss-pyocd-727"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: STM32F7/H7/G0 packs not installable: pack download fails, 'No cores discovered'"
summary: "The STM32F7/H7/G0 pdsc downloads failed during the index update (the maintainer later says this is fixed; a separate problem is that cmsis-pack-manager parallelises the index download so much that Keil and NXP servers block it, cmsis-pack-manager#190)."
status: "draft"
tool: "pyocd"
symptoms: ["ERRO download of \"https://www.keil.com/pack/Keil.STM32H7xx_DFP.pdsc\" failed: unexpected end of file"]
symptom_regex: "download\\s+of\\s+\".*?\"\\s+failed:\\s+unexpected\\s+end\\s+of\\s+file"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/727"
doc_source: "https://github.com/pyocd/pyOCD/issues/727"
resolution: "workaround"
versions: "Keil.STM32F7xx_DFP 2.12.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "family": ["STM32F7 Series", "STM32H7 Series", "STM32G0 Series"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ERRO download of "https://www.keil.com/pack/Keil.STM32H7xx_DFP.pdsc" failed: unexpected end of file`

## Cause

The STM32F7/H7/G0 pdsc downloads failed during the index update (the maintainer later says this is fixed; a separate problem is that cmsis-pack-manager parallelises the index download so much that Keil and NXP servers block it, cmsis-pack-manager#190). For 'No cores were discovered', STM32F7/H7 need DBGMCU writes to enable clocks, which packs do through debug sequences that pyOCD did not yet support.

## Fix

Download the DFP from the Keil pack list and pass it with --pack. The reporter also needed to update the ST-Link firmware and erase the flash before pyOCD connected reliably. Until debug sequences are supported, configure DBGMCU.CR in a pyOCD user script.

## Source

Resolution: workaround

Versions: Keil.STM32F7xx_DFP 2.12.0

From [pyocd/pyOCD #727](https://github.com/pyocd/pyOCD/issues/727), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
