---
id: "iss-pyocd-893"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Windows: pyocd list prints usb _objfinalizer exceptions (libusb)"
summary: "A long-standing pyusb bug showed up after libusb changed its allocation handling; the fix lived in pyusb but was not released for a long time."
status: "draft"
tool: "pyocd"
symptoms: ["Exception ignored in: <function _AutoFinalizedObjectBase.__del__"]
symptom_regex: "Exception\\s+ignored\\s+in:\\s+<function\\s+_AutoFinalizedObjectBase\\.__del__"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/893"
doc_source: "https://github.com/pyocd/pyOCD/issues/893"
resolution: "fixed-in-release"
versions: "fixed in pyusb 1.1.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Exception ignored in: <function _AutoFinalizedObjectBase.__del__`

## Cause

A long-standing pyusb bug showed up after libusb changed its allocation handling; the fix lived in pyusb but was not released for a long time.

## Fix

Run `pip install -U pyusb` (1.1.0 or newer), or `pip install -U --upgrade-strategy=eager pyocd` to refresh all dependencies.

## Source

Resolution: fixed-in-release

Versions: fixed in pyusb 1.1.0

From [pyocd/pyOCD #893](https://github.com/pyocd/pyOCD/issues/893), summarized in own words; confidence high, not reviewed yet.
