---
id: "iss-pyocd-614"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd gdbserver aborts with 'The device has no langid' when an Android phone is attached"
summary: "While enumerating USB devices pyOCD read string descriptors of every device; one device (a phone) has none and pyusb raised ValueError, which killed the probe scan."
status: "draft"
tool: "pyocd"
symptoms: ["0000506:ERROR:__main__:uncaught exception: The device has no langid"]
symptom_regex: "\\S+:ERROR:__main__:uncaught\\s+exception:\\s+The\\s+device\\s+has\\s+no\\s+langid"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/614"
doc_source: "https://github.com/pyocd/pyOCD/issues/614"
resolution: "fixed-in-release"
versions: "regression after 0.19; fixed on master"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0000506:ERROR:__main__:uncaught exception: The device has no langid`

## Cause

While enumerating USB devices pyOCD read string descriptors of every device; one device (a phone) has none and pyusb raised ValueError, which killed the probe scan.

## Fix

Use pyOCD after the fix that tolerates such devices (merged shortly after 0.20.0), or unplug the other device.

## Source

Resolution: fixed-in-release

Versions: regression after 0.19; fixed on master

From [pyocd/pyOCD #614](https://github.com/pyocd/pyOCD/issues/614), summarized in own words; confidence high, not reviewed yet.
