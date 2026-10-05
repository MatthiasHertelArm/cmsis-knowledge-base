---
id: "iss-pyocd-1825"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Low-speed USB CMSIS-DAP v1 probe fails on Windows: packet size error then 'already open'"
summary: "On Windows the hidapi backend took the HID report size from the endpoint size (8 bytes for a low-speed device) instead of the 64 bytes in the HID report descriptor, so opening failed; the reporter suspected the failed open …"
status: "draft"
tool: "pyocd"
symptoms: ["DAP_Info Packet Size 64 exceeds endpoint wMaxPacketSize 8", "Error: already open"]
symptom_regex: "DAP_Info\\s+Packet\\s+Size\\s+\\S+\\s+exceeds\\s+endpoint\\s+wMaxPacketSize\\s+\\S+"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1825"
doc_source: "https://github.com/pyocd/pyOCD/issues/1825"
resolution: "fixed-in-release"
versions: "seen on 0.39.0; macOS also broke in 0.40.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`DAP_Info Packet Size 64 exceeds endpoint wMaxPacketSize 8`
`Error: already open`

## Cause

On Windows the hidapi backend took the HID report size from the endpoint size (8 bytes for a low-speed device) instead of the 64 bytes in the HID report descriptor, so opening failed; the reporter suspected the failed open was not cleaned up, which gives 'already open' on the next attempt. On Linux pyOCD uses the PyUSB backend instead.

## Fix

Use a pyOCD version with change #1854 (hidapi backend revision), which the reporter confirmed works on Windows and macOS. Linux, which uses the PyUSB backend, remained broken in the thread.

## Source

Resolution: fixed-in-release

Versions: seen on 0.39.0; macOS also broke in 0.40.0

From [pyocd/pyOCD #1825](https://github.com/pyocd/pyOCD/issues/1825), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
