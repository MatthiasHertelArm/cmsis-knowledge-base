---
id: "iss-pyocd-241"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: 'The device has no langid' on Linux is an USB permission problem"
summary: "pyusb stores an empty language list when the descriptor read is denied, and then raises ValueError."
status: "draft"
tool: "pyocd"
symptoms: ["uncaught exception: The device has no langid"]
symptom_regex: "uncaught\\s+exception:\\s+The\\s+device\\s+has\\s+no\\s+langid"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/241"
doc_source: "https://github.com/pyocd/pyOCD/issues/241"
resolution: "configuration"
versions: "0.7.1"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`uncaught exception: The device has no langid`

## Cause

pyusb stores an empty language list when the descriptor read is denied, and then raises ValueError. The real cause is missing access rights to the USB device.

## Fix

Add a udev rule for the probe or run as root; later pyOCD versions handle the error and log a permission hint.

## Source

Resolution: configuration

Versions: 0.7.1

From [pyocd/pyOCD #241](https://github.com/pyocd/pyOCD/issues/241), summarized in own words; confidence medium, not reviewed yet.
