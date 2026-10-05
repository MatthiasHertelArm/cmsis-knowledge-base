---
id: "iss-pyocd-805"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: CMSIS-DAP probe with a plain product name (AK-CMSIS-DAP) is not detected"
summary: "pyOCD's pyusb backend required 'CMSIS-DAP' in the USB interface string, which is only mandatory for composite devices."
status: "draft"
tool: "pyocd"
symptoms: ["No available debug probes are connected"]
symptom_regex: "No\\s+available\\s+debug\\s+probes\\s+are\\s+connected"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/805"
doc_source: "https://github.com/pyocd/pyOCD/issues/805"
resolution: "fixed-in-release"
versions: "affected 0.24.1; fixed in 0.25.0"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`No available debug probes are connected`

## Cause

pyOCD's pyusb backend required 'CMSIS-DAP' in the USB interface string, which is only mandatory for composite devices.

## Fix

Upgrade to pyOCD 0.25.0 or newer, which relaxes the interface name requirement.

## Source

Resolution: fixed-in-release

Versions: affected 0.24.1; fixed in 0.25.0

From [pyocd/pyOCD #805](https://github.com/pyocd/pyOCD/issues/805), summarized in own words; confidence high, checked against the thread, not reviewed yet.
