---
id: "iss-pyocd-1682"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd list shows no probe with Python 3.12 and 0.36.0 on Windows"
summary: "libusb-package had no wheel for Python 3.12, so pip tried to build it and, without Visual Studio, installed it without libusb-1.0.dll."
status: "draft"
tool: "pyocd"
symptoms: ["No available debug probes are connected"]
symptom_regex: "No\\s+available\\s+debug\\s+probes\\s+are\\s+connected"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1682"
doc_source: "https://github.com/pyocd/pyOCD/issues/1682"
resolution: "workaround"
versions: "0.36.0 with Python 3.12.2"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`No available debug probes are connected`

## Cause

libusb-package had no wheel for Python 3.12, so pip tried to build it and, without Visual Studio, installed it without libusb-1.0.dll.

## Fix

Place libusb-1.0.dll (from the libusb releases) in a location on the search path such as C:\Windows\System32, or use a Python/libusb-package combination that has a wheel.

## Source

Resolution: workaround

Versions: 0.36.0 with Python 3.12.2

From [pyocd/pyOCD #1682](https://github.com/pyocd/pyOCD/issues/1682), summarized in own words; confidence high, not reviewed yet.
