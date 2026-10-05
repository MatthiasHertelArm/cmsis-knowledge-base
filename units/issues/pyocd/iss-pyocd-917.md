---
id: "iss-pyocd-917"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: J-Link probe with leading zeros in serial number is not found by pyocd"
summary: "The J-Link driver treats the serial number as an integer, so pyocd lists and matches it without leading zeros, while the USB descriptor shows them."
status: "draft"
tool: "pyocd"
symptoms: ["pylink.errors.JLinkException: No emulator with serial number 261002616 found."]
symptom_regex: "pylink\\.errors\\.JLinkException:\\s+No\\s+emulator\\s+with\\s+serial\\s+number\\s+\\S+\\s+found\\."
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/917"
doc_source: "https://github.com/pyocd/pyOCD/issues/917"
resolution: "workaround"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`pylink.errors.JLinkException: No emulator with serial number 261002616 found.`

## Cause

The J-Link driver treats the serial number as an integer, so pyocd lists and matches it without leading zeros, while the USB descriptor shows them.

## Fix

Select the probe by the number as pyocd list prints it (leading zeros dropped) or any unique part of it. Passing the zero-padded USB serial does not match.

## Source

Resolution: workaround

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #917](https://github.com/pyocd/pyOCD/issues/917), summarized in own words; confidence low, not reviewed yet.
