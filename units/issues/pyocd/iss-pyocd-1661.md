---
id: "iss-pyocd-1661"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: RTT control block not found when its ID string straddles a 32-byte boundary"
summary: "The control block search code read memory in chunks and missed an ID string that crossed a chunk boundary."
status: "draft"
tool: "pyocd"
symptoms: ["C Control block not found [__main__]"]
symptom_regex: "C\\s+Control\\s+block\\s+not\\s+found"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1661"
doc_source: "https://github.com/pyocd/pyOCD/issues/1661"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`C Control block not found [__main__]`

## Cause

The control block search code read memory in chunks and missed an ID string that crossed a chunk boundary.

## Fix

Workaround: start the search 16 bytes later (change -a address by 0x10) or force 16-byte alignment of the block. Fixed by change #1669 in a later release.

## Source

Resolution: fixed-in-release

From [pyocd/pyOCD #1661](https://github.com/pyocd/pyOCD/issues/1661), summarized in own words; confidence high, not reviewed yet.
