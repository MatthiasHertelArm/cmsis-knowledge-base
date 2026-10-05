---
id: "iss-pyocd-1693"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyOCD cannot find CMSIS-DAP v2 or ST-Link probes on Windows with Python 3.12 or 3.13"
summary: "The libusb DLL is not found by the USB backend in this Python and pyOCD combination, so all libusb based probe types are disabled."
status: "draft"
tool: "pyocd"
symptoms: ["STLink, CMSIS-DAPv2 and PicoProbe probes are not supported because no libusb library was found."]
symptom_regex: "STLink,\\s+CMSIS\\-DAPv2\\s+and\\s+PicoProbe\\s+probes\\s+are\\s+not\\s+supported\\s+because\\s+no\\s+libusb\\s+library\\s+was\\s+found\\."
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1693"
doc_source: "https://github.com/pyocd/pyOCD/issues/1693"
resolution: "workaround"
versions: "pyOCD 0.36 with Python 3.12 and 3.13."
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`STLink, CMSIS-DAPv2 and PicoProbe probes are not supported because no libusb library was found.`

## Cause

The libusb DLL is not found by the USB backend in this Python and pyOCD combination, so all libusb based probe types are disabled. Copying libusb-1.0.dll next to python.exe or into system32 did not help.

## Fix

Workaround reported: put the folder holding libusb-1.0.dll on PATH from Python before the backend loads, e.g. os.environ['PATH'] = r'<libusb dll dir>' + os.pathsep + os.environ['PATH'] at the top of pyocd/probe/pydapaccess/interface/pyusb_v2_backend.py. Python 3.11 works without this.

## Source

Resolution: workaround

Versions: pyOCD 0.36 with Python 3.12 and 3.13.

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1693](https://github.com/pyocd/pyOCD/issues/1693), summarized in own words; confidence low, checked against the thread, not reviewed yet.
