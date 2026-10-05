---
id: "iss-pyocd-226"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Flashing two boards at the same time on Linux fails with USB Resource busy"
summary: "Old pyOCD claimed all matching probes during enumeration, so a second instance collided with the first."
status: "draft"
tool: "pyocd"
symptoms: ["usb.core.USBError: [Errno 16] Resource busy"]
symptom_regex: "usb\\.core\\.USBError:\\s+\\[Errno\\s+\\S+\\]\\s+Resource\\s+busy"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/226"
doc_source: "https://github.com/pyocd/pyOCD/issues/226"
resolution: "fixed-in-release"
versions: "0.7.x"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`usb.core.USBError: [Errno 16] Resource busy`

## Cause

Old pyOCD claimed all matching probes during enumeration, so a second instance collided with the first.

## Fix

Use a version containing simultaneous multi-device access (PR #268) and select each probe by its unique id.

## Source

Resolution: fixed-in-release

Versions: 0.7.x

From [pyocd/pyOCD #226](https://github.com/pyocd/pyOCD/issues/226), summarized in own words; confidence medium, not reviewed yet.
