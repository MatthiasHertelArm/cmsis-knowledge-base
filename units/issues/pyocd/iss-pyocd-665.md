---
id: "iss-pyocd-665"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: AssertionError: flash pages do not fit evenly into sector (STM32L0/H7 Keil pack)"
summary: "The flash algorithm in the Keil STM32 device packs declares a page size larger than its sector size, which pyocd refuses."
status: "draft"
tool: "pyocd"
symptoms: ["Flash pages (1024 bytes) do not fit evenly into sector (128 bytes)"]
symptom_regex: "Flash\\s+pages\\s+\\(\\S+\\s+bytes\\)\\s+do\\s+not\\s+fit\\s+evenly\\s+into\\s+sector\\s+\\(\\S+\\s+bytes\\)"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/665"
doc_source: "https://github.com/pyocd/pyOCD/issues/665"
resolution: "unresolved"
versions: "pyOCD 0.20.1; Keil.STM32L0xx_DFP; Keil.STM32H7xx_DFP 3.1.1"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "family": ["STM32L0 Series", "STM32H7 Series"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Flash pages (1024 bytes) do not fit evenly into sector (128 bytes)`

## Cause

The flash algorithm in the Keil STM32 device packs declares a page size larger than its sector size, which pyocd refuses.

## Fix

The pack's flash algorithm has to be fixed by the vendor: the maintainer reported it to Keil, who planned a fixed pack, and planned pyocd workarounds for such pack mistakes.

## Source

Resolution: unresolved

Versions: pyOCD 0.20.1; Keil.STM32L0xx_DFP; Keil.STM32H7xx_DFP 3.1.1

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #665](https://github.com/pyocd/pyOCD/issues/665), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
