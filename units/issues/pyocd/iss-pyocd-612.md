---
id: "iss-pyocd-612"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: STM32F401RE pack fails: not enough space for flash algorithm, then TypeError"
summary: "The device has 128 kB sectors, so the flash algorithm plus a sector-sized data buffer did not fit in RAM; the pack sector table parsing also mishandled (start,size) tuples."
status: "draft"
tool: "pyocd"
symptoms: ["0000464:WARNING:flash_algo:Not enough space for flash algorithm", "0000464:ERROR:__main__:uncaught exception: unsupported operand type(s) for -: 'tuple' and 'int'"]
symptom_regex: "\\S+:WARNING:flash_algo:Not\\s+enough\\s+space\\s+for\\s+flash\\s+algorithm"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/612"
doc_source: "https://github.com/pyocd/pyOCD/issues/612"
resolution: "fixed-in-release"
versions: "development builds before 0.20.0"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["STM32F401RETx"], "core": ["Cortex-M4"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0000464:WARNING:flash_algo:Not enough space for flash algorithm`
`0000464:ERROR:__main__:uncaught exception: unsupported operand type(s) for -: 'tuple' and 'int'`

## Cause

The device has 128 kB sectors, so the flash algorithm plus a sector-sized data buffer did not fit in RAM; the pack sector table parsing also mishandled (start,size) tuples.

## Fix

Use a pyOCD release in which pack flash algorithms support separate erase and program sizes (0.20.0).

## Source

Resolution: fixed-in-release

Versions: development builds before 0.20.0

From [pyocd/pyOCD #612](https://github.com/pyocd/pyOCD/issues/612), summarized in own words; confidence medium, not reviewed yet.
