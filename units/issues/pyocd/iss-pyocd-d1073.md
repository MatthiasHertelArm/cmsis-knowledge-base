---
id: "iss-pyocd-d1073"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd flash reports 0 bytes programmed although erase works"
summary: "Most likely the ELF has no loadable sections in the flash range, for example because it was linked to run from RAM."
status: "draft"
tool: "pyocd"
symptoms: ["0001982:INFO:loader:Erased 0 bytes (0 sectors), programmed 0 bytes (0 pages), skipped 0 bytes (0 pages) at 0.00 kB/s"]
symptom_regex: "\\S+:INFO:loader:Erased\\s+\\S+\\s+bytes\\s+\\(\\S+\\s+sectors\\),\\s+programmed\\s+\\S+\\s+bytes\\s+\\(\\S+\\s+pages\\),\\s+skipped\\s+\\S+\\s+bytes\\s+\\(\\S+\\s+pages\\)\\s+at\\s+\\S+\\s+kB/s"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/discussions/1073"
doc_source: "https://github.com/pyocd/pyOCD/discussions/1073"
resolution: "user-error"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["HT32F52253"], "core": ["Cortex-M0+"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0001982:INFO:loader:Erased 0 bytes (0 sectors), programmed 0 bytes (0 pages), skipped 0 bytes (0 pages) at 0.00 kB/s`

## Cause

Most likely the ELF has no loadable sections in the flash range, for example because it was linked to run from RAM. The maintainer's reading; the thread does not show a confirmation.

## Fix

List the sections with arm-none-eabi-objdump -h <file>.elf and check their load addresses against the flash region; relink for flash, or convert to a binary with arm-none-eabi-objcopy -O binary and load that at the flash base address.

## Source

Resolution: user-error

From [pyocd/pyOCD discussion 1073](https://github.com/pyocd/pyOCD/discussions/1073), summarized in own words; confidence low, not reviewed yet.
