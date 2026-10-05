---
id: "iss-pyocd-917"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: J-Link probe with leading zeros in serial number is not found by pyocd"
summary: "The J-Link driver handles the serial number as an integer, so pyocd lists and matches J-Link probes without the leading zeros that the USB descriptor shows, and the zero-padded serial does not match."
status: "draft"
tool: "pyocd"
symptoms: ["pylink.errors.JLinkException: No emulator with serial number 261002616 found."]
symptom_regex: "pylink\\.errors\\.JLinkException:\\s+No\\s+emulator\\s+with\\s+serial\\s+number\\s+\\S+\\s+found\\."
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/917"
doc_source: "https://github.com/pyocd/pyOCD/issues/917"
resolution: "unresolved"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
checked: "unsupported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`pylink.errors.JLinkException: No emulator with serial number 261002616 found.`

## Cause

The J-Link driver handles the serial number as an integer, so pyocd lists and matches J-Link probes without the leading zeros that the USB descriptor shows, and the zero-padded serial does not match. On Linux, opening a probe by the unique_id that pyocd itself reported (without zeros) still failed with 'No emulator with serial number ... found'; no cause was found for that.

## Fix

On macOS the maintainer could select the probe with the serial as pyocd list prints it (no leading zeros) or any unique part of it; this did not help the Linux API user, and the thread ends without a fix.

## Source

Resolution: unresolved

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #917](https://github.com/pyocd/pyOCD/issues/917), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
