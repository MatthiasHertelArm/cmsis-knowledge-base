---
id: "iss-pyocd-1553"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: RTT 'Control block not found' after upgrading from 0.34.3 to 0.35"
summary: "The search compared a full 16-byte padded ID, so a block whose ID string is followed by non-zero bytes ('SEGGER RTT' is shorter than 16) was missed."
status: "draft"
tool: "pyocd"
symptoms: ["C Control block not found [__main__]"]
symptom_regex: "C\\s+Control\\s+block\\s+not\\s+found"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1553"
doc_source: "https://github.com/pyocd/pyOCD/issues/1553"
resolution: "workaround"
versions: "broken 0.35.0 and 0.35.1"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`C Control block not found [__main__]`

## Cause

The search compared a full 16-byte padded ID, so a block whose ID string is followed by non-zero bytes ('SEGGER RTT' is shorter than 16) was missed.

## Fix

Fix the search to match only the real ID length; a local fix worked and a maintainer asked for a pull request. Downgrading to 0.34.3 is a stop-gap.

## Source

Resolution: workaround

Versions: broken 0.35.0 and 0.35.1

From [pyocd/pyOCD #1553](https://github.com/pyocd/pyOCD/issues/1553), summarized in own words; confidence low, not reviewed yet.
