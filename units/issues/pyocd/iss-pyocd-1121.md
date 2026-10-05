---
id: "iss-pyocd-1121"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: WCH-Link CMSIS-DAP probe is not listed by pyocd on macOS"
summary: "pyOCD recognises HID CMSIS-DAP probes by the string 'CMSIS-DAP' in the product name; the WCH-Link's product string lacks it and its HID interface string descriptor is broken, so the probe was ignored on macOS (it was found on Windows …"
status: "draft"
tool: "pyocd"
symptoms: ["No available debug probes are connected"]
symptom_regex: "No\\s+available\\s+debug\\s+probes\\s+are\\s+connected"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1121"
doc_source: "https://github.com/pyocd/pyOCD/issues/1121"
resolution: "fixed-in-release"
versions: "seen with 0.30.3 on macOS"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`No available debug probes are connected`

## Cause

pyOCD recognises HID CMSIS-DAP probes by the string 'CMSIS-DAP' in the product name; the WCH-Link's product string lacks it and its HID interface string descriptor is broken, so the probe was ignored on macOS (it was found on Windows through the path string).

## Fix

Use a pyOCD build with the hidapi interface-name/UID detection fix (a maintainer branch was offered for testing); later releases include the improved detection.

## Source

Resolution: fixed-in-release

Versions: seen with 0.30.3 on macOS

From [pyocd/pyOCD #1121](https://github.com/pyocd/pyOCD/issues/1121), summarized in own words; confidence medium, not reviewed yet.
