---
id: "iss-pyocd-226"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Flashing two boards at the same time on Linux fails with USB Resource busy"
summary: "pyOCD lacked support for simultaneous access to several devices, so a second instance failed with 'Resource busy' when claiming a USB interface while enumerating the boards."
status: "draft"
tool: "pyocd"
symptoms: ["usb.core.USBError: [Errno 16] Resource busy"]
symptom_regex: "usb\\.core\\.USBError:\\s+\\[Errno\\s+\\S+\\]\\s+Resource\\s+busy"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/226"
doc_source: "https://github.com/pyocd/pyOCD/issues/226"
resolution: "fixed-in-release"
versions: "pyOCD 0.6.1 affected"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`usb.core.USBError: [Errno 16] Resource busy`

## Cause

pyOCD lacked support for simultaneous access to several devices, so a second instance failed with 'Resource busy' when claiming a USB interface while enumerating the boards.

## Fix

Use a pyOCD version containing PR #268, which adds simultaneous device access; the reporter confirmed that two devices then worked concurrently.

## Source

Resolution: fixed-in-release

Versions: pyOCD 0.6.1 affected

From [pyocd/pyOCD #226](https://github.com/pyocd/pyOCD/issues/226), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
