---
id: "iss-pyocd-1825"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Low-speed USB CMSIS-DAP v1 probe fails on Windows: packet size error then 'already open'"
summary: "On Windows and Linux the hidapi backend derives HID report size from the endpoint size (8 bytes for a low-speed device) instead of the HID report descriptor, which says 64."
status: "draft"
tool: "pyocd"
symptoms: ["DAP_Info Packet Size 64 exceeds endpoint wMaxPacketSize 8", "Error: already open"]
symptom_regex: "DAP_Info\\s+Packet\\s+Size\\s+\\S+\\s+exceeds\\s+endpoint\\s+wMaxPacketSize\\s+\\S+"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1825"
doc_source: "https://github.com/pyocd/pyOCD/issues/1825"
resolution: "fixed-in-release"
versions: "seen on 0.39.0"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`DAP_Info Packet Size 64 exceeds endpoint wMaxPacketSize 8`
`Error: already open`

## Cause

On Windows and Linux the hidapi backend derives HID report size from the endpoint size (8 bytes for a low-speed device) instead of the HID report descriptor, which says 64. The failed open leaves the device open so a retry errors.

## Fix

Windows and macOS were fixed by the hidapi backend rework (change #1854). Linux uses the pyusb backend and remained broken in the thread.

## Source

Resolution: fixed-in-release

Versions: seen on 0.39.0

From [pyocd/pyOCD #1825](https://github.com/pyocd/pyOCD/issues/1825), summarized in own words; confidence medium, not reviewed yet.
