---
id: "iss-pyocd-1585"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: XDS110-based LaunchPad: USB read timeout during flash"
summary: "The probe firmware does not cope with several outstanding CMSIS-DAP requests; reads time out."
status: "draft"
tool: "pyocd"
symptoms: ["usb.core.USBTimeoutError: [Errno 110] Operation timed out"]
symptom_regex: "usb\\.core\\.USBTimeoutError:\\s+\\[Errno\\s+\\S+\\]\\s+Operation\\s+timed\\s+out"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1585"
doc_source: "https://github.com/pyocd/pyOCD/issues/1585"
resolution: "workaround"
versions: "0.35.1"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["MSPM0G3507"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`usb.core.USBTimeoutError: [Errno 110] Operation timed out`

## Cause

The probe firmware does not cope with several outstanding CMSIS-DAP requests; reads time out.

## Fix

Add -Ocmsis_dap.limit_packets to prevent multiple outstanding commands. Note: reflashing an identical image is skipped by smart flash; use -Osmart_flash=0 to force programming.

## Source

Resolution: workaround

Versions: 0.35.1

From [pyocd/pyOCD #1585](https://github.com/pyocd/pyOCD/issues/1585), summarized in own words; confidence medium, not reviewed yet.
