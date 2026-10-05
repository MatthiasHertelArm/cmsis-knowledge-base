---
id: "iss-pyocd-1076"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd 0.29 crashes (NoneType) on probes without a USB serial string"
summary: "pyocd needs a serial number string from every probe to identify it."
status: "draft"
tool: "pyocd"
symptoms: ["0000542:CRITICAL:__main__:uncaught exception: 'NoneType' object is not subscriptable"]
symptom_regex: "\\S+:CRITICAL:__main__:uncaught\\s+exception:\\s+'.*?'\\s+object\\s+is\\s+not\\s+subscriptable"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1076"
doc_source: "https://github.com/pyocd/pyOCD/issues/1076"
resolution: "workaround"
versions: "0.29.0 on Linux"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0000542:CRITICAL:__main__:uncaught exception: 'NoneType' object is not subscriptable`

## Cause

pyocd needs a serial number string from every probe to identify it. A CMSIS-DAP firmware that has no USB serial descriptor leaves it None. The earlier version seemed to work only because Windows had cached an old descriptor.

## Fix

Give the probe firmware a USB serial number string. A pyocd change that synthesises a stable ID from other USB data for such probes was in review at the time (CMSIS-DAP v1 via pyusb first).

## Source

Resolution: workaround

Versions: 0.29.0 on Linux

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1076](https://github.com/pyocd/pyOCD/issues/1076), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
