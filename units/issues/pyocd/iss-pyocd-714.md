---
id: "iss-pyocd-714"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Intermittent 'STLink error (20): DP wait' on ST boards after power cycling"
summary: "After a power cycle the Mbed OS application sleeps in a low-power mode with debug disabled; pyOCD cannot wake the debug port of a sleeping target."
status: "draft"
tool: "pyocd"
symptoms: ["CRITICAL:__main__:STLink error (20): DP wait"]
symptom_regex: "STLink\\s+error\\s+\\(\\S+\\):\\s+DP\\s+wait"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/714"
doc_source: "https://github.com/pyocd/pyOCD/issues/714"
resolution: "configuration"
versions: "seen with 0.21.0"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`CRITICAL:__main__:STLink error (20): DP wait`

## Cause

After a power cycle the Mbed OS application sleeps in a low-power mode with debug disabled; pyOCD cannot wake the debug port of a sleeping target.

## Fix

Build firmware with the debug profile so it never sleeps, or set the DBGMCU_CR sleep bits in firmware at startup; update ST-Link firmware; connect under reset where supported.

## Source

Resolution: configuration

Versions: seen with 0.21.0

From [pyocd/pyOCD #714](https://github.com/pyocd/pyOCD/issues/714), summarized in own words; confidence medium, not reviewed yet.
