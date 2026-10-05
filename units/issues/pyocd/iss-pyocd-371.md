---
id: "iss-pyocd-371"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: hidapi 'Unable to open device' on macOS with system Python"
summary: "With the Python shipped by macOS (or one with an empty hidapi path) the HID device path came back empty so the CMSIS-DAP interface could not be opened."
status: "draft"
tool: "pyocd"
symptoms: ["uncaught exception: Unable to open device"]
symptom_regex: "uncaught\\s+exception:\\s+Unable\\s+to\\s+open\\s+device"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/371"
doc_source: "https://github.com/pyocd/pyOCD/issues/371"
resolution: "workaround"
versions: "pyocd master of mid-2018"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`uncaught exception: Unable to open device`

## Cause

With the Python shipped by macOS (or one with an empty hidapi path) the HID device path came back empty so the CMSIS-DAP interface could not be opened.

## Fix

Use a different Python install such as one from Homebrew, and reinstall pyOCD and hidapi with its pip.

## Source

Resolution: workaround

Versions: pyocd master of mid-2018

From [pyocd/pyOCD #371](https://github.com/pyocd/pyOCD/issues/371), summarized in own words; confidence medium, not reviewed yet.
