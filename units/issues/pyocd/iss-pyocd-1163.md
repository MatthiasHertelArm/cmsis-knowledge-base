---
id: "iss-pyocd-1163"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pack --install with a short STM32L4 name installs a pack that has no such device"
summary: "Newer versions of the vendor pack renamed devices to include package suffixes (for example stm32l4a6vgtx), and pyOCD always uses only the newest pack version in the index, so the old short name no longer matches."
status: "draft"
tool: "pyocd"
symptoms: ["Target type 'stm32l4a6vg' not recognized."]
symptom_regex: "Target\\s+type\\s+'.*?'\\s+not\\s+recognized\\."
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1163"
doc_source: "https://github.com/pyocd/pyOCD/issues/1163"
resolution: "configuration"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"], "family": ["STM32L4 Series"], "device": ["STM32L4A6VGTx"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Target type 'stm32l4a6vg' not recognized.`

## Cause

Newer versions of the vendor pack renamed devices to include package suffixes (for example stm32l4a6vgtx), and pyOCD always uses only the newest pack version in the index, so the old short name no longer matches.

## Fix

Search with `pyocd pack --find <part>` and install or select the full device name including the suffix, e.g. `pyocd pack --install stm32l4a6vgtx`.

## Source

Resolution: configuration

From [pyocd/pyOCD #1163](https://github.com/pyocd/pyOCD/issues/1163), summarized in own words; confidence high, checked against the thread, not reviewed yet.
