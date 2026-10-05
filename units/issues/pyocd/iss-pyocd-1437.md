---
id: "iss-pyocd-1437"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: LPC54 devices use the LPC55 unlock sequence and cannot reset and halt"
summary: "The LPC5500 family regular expression also matched LPC54xx parts, so the LPC55 debug-mailbox unlock sequence ran on a chip that has no such access port."
status: "draft"
tool: "pyocd"
symptoms: ["W had to forcibly halt core after reset [target_lpc5500]"]
symptom_regex: "W\\s+had\\s+to\\s+forcibly\\s+halt\\s+core\\s+after\\s+reset"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1437"
doc_source: "https://github.com/pyocd/pyOCD/issues/1437"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "family": ["LPC54"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`W had to forcibly halt core after reset [target_lpc5500]`

## Cause

The LPC5500 family regular expression also matched LPC54xx parts, so the LPC55 debug-mailbox unlock sequence ran on a chip that has no such access port.

## Fix

Fixed by change #1440; upgrade.

## Source

Resolution: fixed-in-release

From [pyocd/pyOCD #1437](https://github.com/pyocd/pyOCD/issues/1437), summarized in own words; confidence high, not reviewed yet.
