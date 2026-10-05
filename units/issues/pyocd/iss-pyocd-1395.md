---
id: "iss-pyocd-1395"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: WCH-Link CMSIS-DAP probe not detected"
summary: "pyOCD matches probes by name strings rather than VID/PID, and this WCH-Link answers string descriptor requests incorrectly in some conditions."
status: "draft"
tool: "pyocd"
symptoms: ["No available debug probes are connected"]
symptom_regex: "No\\s+available\\s+debug\\s+probes\\s+are\\s+connected"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1395"
doc_source: "https://github.com/pyocd/pyOCD/issues/1395"
resolution: "fixed-in-release"
versions: "0.33.1"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`No available debug probes are connected`

## Cause

pyOCD matches probes by name strings rather than VID/PID, and this WCH-Link answers string descriptor requests incorrectly in some conditions.

## Fix

Matching by VID/PID pair was added in change #1399; upgrade. Workaround on Linux: use the hidapi backend (PYOCD_USB_BACKEND=hidapiusb) after allowing the product name.

## Source

Resolution: fixed-in-release

Versions: 0.33.1

From [pyocd/pyOCD #1395](https://github.com/pyocd/pyOCD/issues/1395), summarized in own words; confidence medium, not reviewed yet.
