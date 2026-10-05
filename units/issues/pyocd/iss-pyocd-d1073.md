---
id: "iss-pyocd-d1073"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd flash reports 0 bytes programmed although erase works"
summary: "The maintainer suspected that the ELF has no programmable sections, for example because it is linked to run from RAM instead of flash; the thread does not confirm it."
status: "draft"
tool: "pyocd"
symptoms: ["0001982:INFO:loader:Erased 0 bytes (0 sectors), programmed 0 bytes (0 pages), skipped 0 bytes (0 pages) at 0.00 kB/s"]
symptom_regex: "\\S+:INFO:loader:Erased\\s+\\S+\\s+bytes\\s+\\(\\S+\\s+sectors\\),\\s+programmed\\s+\\S+\\s+bytes\\s+\\(\\S+\\s+pages\\),\\s+skipped\\s+\\S+\\s+bytes\\s+\\(\\S+\\s+pages\\)\\s+at\\s+\\S+\\s+kB/s"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/discussions/1073"
doc_source: "https://github.com/pyocd/pyOCD/discussions/1073"
resolution: "unresolved"
confidence: "low"
cause_origin: "issue-digest"
checked: "unsupported"
applies_to: {"tool": ["pyocd"], "device": ["HT32F52253"], "core": ["Cortex-M0+"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0001982:INFO:loader:Erased 0 bytes (0 sectors), programmed 0 bytes (0 pages), skipped 0 bytes (0 pages) at 0.00 kB/s`

## Cause

The maintainer suspected that the ELF has no programmable sections, for example because it is linked to run from RAM instead of flash; the thread does not confirm it.

## Fix

List the sections with arm-none-eabi-objdump -h <file>.elf to check their addresses and attributes, or try converting the ELF to a binary with arm-none-eabi-objcopy -O binary.

## Source

Resolution: unresolved

From [pyocd/pyOCD discussion 1073](https://github.com/pyocd/pyOCD/discussions/1073), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
