---
id: "iss-pyocd-612"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: STM32F401RE pack fails: not enough space for flash algorithm, then TypeError"
summary: "The STM32F401RE has 128 kB sectors, so the flash algorithm and its data buffer do not fit in the available RAM; the pack sector parsing also mishandled the (start, size) tuples, causing the TypeError."
status: "draft"
tool: "pyocd"
symptoms: ["0000464:WARNING:flash_algo:Not enough space for flash algorithm", "0000464:ERROR:__main__:uncaught exception: unsupported operand type(s) for -: 'tuple' and 'int'"]
symptom_regex: "\\S+:WARNING:flash_algo:Not\\s+enough\\s+space\\s+for\\s+flash\\s+algorithm"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/612"
doc_source: "https://github.com/pyocd/pyOCD/issues/612"
resolution: "unresolved"
versions: "Keil.STM32F4xx_DFP 2.13.0"
confidence: "low"
cause_origin: "issue-digest"
checked: "unsupported"
applies_to: {"tool": ["pyocd"], "device": ["STM32F401RETx"], "core": ["Cortex-M4"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0000464:WARNING:flash_algo:Not enough space for flash algorithm`
`0000464:ERROR:__main__:uncaught exception: unsupported operand type(s) for -: 'tuple' and 'int'`

## Cause

The STM32F401RE has 128 kB sectors, so the flash algorithm and its data buffer do not fit in the available RAM; the pack sector parsing also mishandled the (start, size) tuples, causing the TypeError.

## Fix

No fix in the thread. Unpacking the tuple in cmsis_pack.py removes the TypeError, but the region then has no flash algorithm; the maintainer planned to support separate erase and program sizes for pack flash algorithms.

## Source

Resolution: unresolved

Versions: Keil.STM32F4xx_DFP 2.13.0

From [pyocd/pyOCD #612](https://github.com/pyocd/pyOCD/issues/612), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
