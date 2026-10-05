---
id: "iss-pyocd-614"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd gdbserver aborts with 'The device has no langid' when an Android phone is attached"
summary: "While scanning USB devices, pyOCD's pyusb backend read the interface name strings of every device; an Android phone without a language ID made pyusb raise ValueError, which aborted the probe scan (likely a regression from PR #595)."
status: "draft"
tool: "pyocd"
symptoms: ["0000506:ERROR:__main__:uncaught exception: The device has no langid"]
symptom_regex: "\\S+:ERROR:__main__:uncaught\\s+exception:\\s+The\\s+device\\s+has\\s+no\\s+langid"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/614"
doc_source: "https://github.com/pyocd/pyOCD/issues/614"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0000506:ERROR:__main__:uncaught exception: The device has no langid`

## Cause

While scanning USB devices, pyOCD's pyusb backend read the interface name strings of every device; an Android phone without a language ID made pyusb raise ValueError, which aborted the probe scan (likely a regression from PR #595).

## Fix

Use a pyOCD with the workaround from PR #616 (verified on master), or unplug the other device.

## Source

Resolution: fixed-in-release

From [pyocd/pyOCD #614](https://github.com/pyocd/pyOCD/issues/614), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
