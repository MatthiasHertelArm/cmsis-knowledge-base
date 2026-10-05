---
id: "iss-pyocd-241"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: 'The device has no langid' on Linux is an USB permission problem"
summary: "pyusb catches the error when reading the langids and stores an empty tuple, then raises ValueError."
status: "draft"
tool: "pyocd"
symptoms: ["uncaught exception: The device has no langid"]
symptom_regex: "uncaught\\s+exception:\\s+The\\s+device\\s+has\\s+no\\s+langid"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/241"
doc_source: "https://github.com/pyocd/pyOCD/issues/241"
resolution: "configuration"
versions: "pyOCD 0.7.1; pyusb 1.0.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`uncaught exception: The device has no langid`

## Cause

pyusb catches the error when reading the langids and stores an empty tuple, then raises ValueError. The real cause is missing access rights to the USB device ([Errno 13] Access denied).

## Fix

Run pyocd-gdbserver as root (sudo); the issue was closed because PR #262 addresses it, without a release named.

## Source

Resolution: configuration

Versions: pyOCD 0.7.1; pyusb 1.0.0

From [pyocd/pyOCD #241](https://github.com/pyocd/pyOCD/issues/241), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
