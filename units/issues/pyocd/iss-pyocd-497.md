---
id: "iss-pyocd-497"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: KeyError: 0 on Nucleo with cortex_m target: no AP found, old ST-Link firmware"
summary: "pyOCD found no CoreSight access port even though the DP ID read worked."
status: "draft"
tool: "pyocd"
symptoms: ["0000857:ERROR:__main__:uncaught exception: 0"]
symptom_regex: "\\S+:ERROR:__main__:uncaught\\s+exception:\\s+\\S+"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/497"
doc_source: "https://github.com/pyocd/pyOCD/issues/497"
resolution: "workaround"
versions: "0.14.3"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["STM32F401RETx"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0000857:ERROR:__main__:uncaught exception: 0`

## Cause

pyOCD found no CoreSight access port even though the DP ID read worked. The on-board ST-Link firmware was very old (2015 build).

## Fix

Update the ST-Link firmware, then rerun; the AP and ROM table scan succeeded afterwards.

## Source

Resolution: workaround

Versions: 0.14.3

From [pyocd/pyOCD #497](https://github.com/pyocd/pyOCD/issues/497), summarized in own words; confidence high, not reviewed yet.
