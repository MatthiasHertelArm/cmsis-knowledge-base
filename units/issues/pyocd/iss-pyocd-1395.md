---
id: "iss-pyocd-1395"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: WCH-Link CMSIS-DAP probe not detected"
summary: "pyOCD matches probes by product and interface name strings rather than VID/PID, and this WCH-Link (2a86:8011) is not fully USB compliant: it fails to answer string descriptor requests properly in some conditions."
status: "draft"
tool: "pyocd"
symptoms: ["No available debug probes are connected"]
symptom_regex: "No\\s+available\\s+debug\\s+probes\\s+are\\s+connected"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1395"
doc_source: "https://github.com/pyocd/pyOCD/issues/1395"
resolution: "workaround"
versions: "0.33.1"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`No available debug probes are connected`

## Cause

pyOCD matches probes by product and interface name strings rather than VID/PID, and this WCH-Link (2a86:8011) is not fully USB compliant: it fails to answer string descriptor requests properly in some conditions.

## Fix

Matching by VID/PID pair was added on the develop branch (commit a926e94; PR #1399 discussed). Workaround on Linux: edit hidapi_backend.py to also accept 'WCH-Link' in the product name and run with PYOCD_USB_BACKEND=hidapiusb (with hidapi installed instead of hid).

## Source

Resolution: workaround

Versions: 0.33.1

From [pyocd/pyOCD #1395](https://github.com/pyocd/pyOCD/issues/1395), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
