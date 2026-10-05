---
id: "iss-pyocd-1054"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: ST-Link no longer listed on Windows 7 after an ST-Link firmware upgrade"
summary: "The firmware upgrade removed the libusb driver association for the ST-Link on Windows 7; its WinUSB driver mode is only available from Windows 8 on, so libusb found nothing."
status: "draft"
tool: "pyocd"
symptoms: ["No available debug probes are connected"]
symptom_regex: "No\\s+available\\s+debug\\s+probes\\s+are\\s+connected"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1054"
doc_source: "https://github.com/pyocd/pyOCD/issues/1054"
resolution: "workaround"
versions: "seen with 0.28.3, ST-Link V2J37M27"
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

The firmware upgrade removed the libusb driver association for the ST-Link on Windows 7; its WinUSB driver mode is only available from Windows 8 on, so libusb found nothing.

## Fix

Use Zadig to assign the libusb-win32 driver to the ST-Link debug interface.

## Source

Resolution: workaround

Versions: seen with 0.28.3, ST-Link V2J37M27

From [pyocd/pyOCD #1054](https://github.com/pyocd/pyOCD/issues/1054), summarized in own words; confidence high, checked against the thread, not reviewed yet.
