---
id: "iss-pyocd-1661"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: RTT control block not found when its ID string straddles a 32-byte boundary"
summary: "pyOCD's RTT control block search failed when the control block ID string crossed a 32-byte boundary."
status: "draft"
tool: "pyocd"
symptoms: ["C Control block not found [__main__]"]
symptom_regex: "C\\s+Control\\s+block\\s+not\\s+found"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1661"
doc_source: "https://github.com/pyocd/pyOCD/issues/1661"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`C Control block not found [__main__]`

## Cause

pyOCD's RTT control block search failed when the control block ID string crossed a 32-byte boundary.

## Fix

Workaround: shift the search start by 16 bytes (one of -a 0x20000000 or -a 0x20000010 works) or align the control block to 16 bytes. The fix (#1669) is merged into pyOCD's develop branch.

## Source

Resolution: fixed-in-release

From [pyocd/pyOCD #1661](https://github.com/pyocd/pyOCD/issues/1661), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
