---
id: "iss-pyocd-1116"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Picoprobe: exception when a probe UID is given but no Picoprobe is connected"
summary: "The Picoprobe enumeration code passes the result of a USB search to PicoLink without checking it, so it dereferences None when a probe UID is given but no Picoprobe is connected."
status: "draft"
tool: "pyocd"
symptoms: ["uncaught exception: 'NoneType' object has no attribute 'serial_number'"]
symptom_regex: "uncaught\\s+exception:\\s+'.*?'\\s+object\\s+has\\s+no\\s+attribute\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1116"
doc_source: "https://github.com/pyocd/pyOCD/issues/1116"
resolution: "unresolved"
confidence: "low"
cause_origin: "issue-digest"
checked: "unsupported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`uncaught exception: 'NoneType' object has no attribute 'serial_number'`

## Cause

The Picoprobe enumeration code passes the result of a USB search to PicoLink without checking it, so it dereferences None when a probe UID is given but no Picoprobe is connected.

## Fix

The thread gives no confirmed fix.

## Source

Resolution: unresolved

From [pyocd/pyOCD #1116](https://github.com/pyocd/pyOCD/issues/1116), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
