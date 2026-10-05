---
id: "iss-pyocd-d1088"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd list finds no CMSIS-DAP v1 probe because of the HID report descriptor"
summary: "pyOCD itself ignores the HID report descriptor, but on Windows and macOS the OS HID driver and the hidapi or pywinusb backends depend on it, as the kernel driver cannot be detached."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/discussions/1088"
doc_source: "https://github.com/pyocd/pyOCD/discussions/1088"
resolution: "configuration"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

pyOCD itself ignores the HID report descriptor, but on Windows and macOS the OS HID driver and the hidapi or pywinusb backends depend on it, as the kernel driver cannot be detached. A descriptor with unsuitable input and output items, or without a vendor usage on older Windows, makes the probe invisible. On Linux libusb is used directly and the descriptor does not matter.

## Fix

Use a vendor-defined usage page with a vendor usage, a 64-byte report size and both input and output reports declared (for example Input/Output with the Data, Variable, Absolute flags), and check the descriptor with the USB-IF HID descriptor tool.

## Source

Resolution: configuration

From [pyocd/pyOCD discussion 1088](https://github.com/pyocd/pyOCD/discussions/1088), summarized in own words; confidence medium, not reviewed yet.
