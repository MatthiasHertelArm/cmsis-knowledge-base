---
id: "iss-pyocd-1303"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: LPC55 factory-new chip: erase/flash fails after reset with memory transfer fault"
summary: "A new LPC55 starts with debug access locked; pyOCD unlocks it on connect but the reset done before flashing locks it again and the unlock was not repeated."
status: "draft"
tool: "pyocd"
symptoms: ["Core #0 is not accessible after reset", "link exception during target disconnect: Memory transfer fault @ 0xe000edf0-0xe000edf3"]
symptom_regex: "Core\\s+\\#\\S+\\s+is\\s+not\\s+accessible\\s+after\\s+reset"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1303"
doc_source: "https://github.com/pyocd/pyOCD/issues/1303"
resolution: "fixed-in-release"
versions: "0.32.3 broken, 0.33.0 fixed"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["LPC5526"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Core #0 is not accessible after reset`
`link exception during target disconnect: Memory transfer fault @ 0xe000edf0-0xe000edf3`

## Cause

A new LPC55 starts with debug access locked; pyOCD unlocks it on connect but the reset done before flashing locks it again and the unlock was not repeated.

## Fix

Fixed in v0.33.0: the unlock is re-run after reset.

## Source

Resolution: fixed-in-release

Versions: 0.32.3 broken, 0.33.0 fixed

From [pyocd/pyOCD #1303](https://github.com/pyocd/pyOCD/issues/1303), summarized in own words; confidence high, not reviewed yet.
