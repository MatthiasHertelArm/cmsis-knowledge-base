---
id: "iss-pyocd-1754"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: CMSIS-DAP bulk SWO: 'read thread exited unexpectedly'"
summary: "A flag marking the SWO thread as finished stayed set when the USB interface was closed and reused, so the reader reported failure although the thread was running."
status: "draft"
tool: "pyocd"
symptoms: ["pyocd.core.exceptions.ProbeError: Probe 0123456789 read thread exited unexpectedly"]
symptom_regex: "pyocd\\.core\\.exceptions\\.ProbeError:\\s+Probe\\s+\\S+\\s+read\\s+thread\\s+exited\\s+unexpectedly"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1754"
doc_source: "https://github.com/pyocd/pyOCD/issues/1754"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`pyocd.core.exceptions.ProbeError: Probe 0123456789 read thread exited unexpectedly`

## Cause

A flag marking the SWO thread as finished stayed set when the USB interface was closed and reused, so the reader reported failure although the thread was running.

## Fix

Fixed by changes #1755 and #1824; update pyOCD.

## Source

Resolution: fixed-in-release

From [pyocd/pyOCD #1754](https://github.com/pyocd/pyOCD/issues/1754), summarized in own words; confidence high, checked against the thread, not reviewed yet.
