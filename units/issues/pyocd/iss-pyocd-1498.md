---
id: "iss-pyocd-1498"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: 'Target type ... not recognized' for an STM32 board; pack not installed"
summary: "The target comes from a CMSIS-Pack that was not installed."
status: "draft"
tool: "pyocd"
symptoms: ["Target type stm32f407vgtx not recognized. Use 'pyocd list --targets' to see currently available target types."]
symptom_regex: "Target\\s+type\\s+stm32f407vgtx\\s+not\\s+recognized\\.\\s+Use\\s+'.*?'\\s+to\\s+see\\s+currently\\s+available\\s+target\\s+types\\."
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1498"
doc_source: "https://github.com/pyocd/pyOCD/issues/1498"
resolution: "configuration"
versions: "0.34.3"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Target type stm32f407vgtx not recognized. Use 'pyocd list --targets' to see currently available target types.`

## Cause

The target comes from a CMSIS-Pack that was not installed. Errors from 'pyocd pack update' about vendor servers are expected, and large packs download slowly without progress.

## Fix

Run 'pyocd pack update' then 'pyocd pack install <part>' and wait for the download to finish.

## Source

Resolution: configuration

Versions: 0.34.3

From [pyocd/pyOCD #1498](https://github.com/pyocd/pyOCD/issues/1498), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
