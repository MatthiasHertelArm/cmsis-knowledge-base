---
id: "iss-pyocd-2019"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: J-Link SWO reader thread dies with IndexError: invalid index"
summary: "The J-Link probe's SWO read passed the byte count straight to pylink, even when no data was available (count 0), which pylink cannot turn into a buffer."
status: "draft"
tool: "pyocd"
symptoms: ["IndexError: invalid index"]
symptom_regex: "IndexError:\\s+invalid\\s+index"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/2019"
doc_source: "https://github.com/pyocd/pyOCD/issues/2019"
resolution: "fixed-in-release"
versions: "seen on 0.45.1"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`IndexError: invalid index`

## Cause

The J-Link probe's SWO read passed the byte count straight to pylink, even when no data was available (count 0), which pylink cannot turn into a buffer.

## Fix

Skip the read when the available byte count is zero. Fixed in pyOCD by a follow-up change; update pyOCD. A monkey patch returning an empty list for a zero count works meanwhile.

## Source

Resolution: fixed-in-release

Versions: seen on 0.45.1

From [pyocd/pyOCD #2019](https://github.com/pyocd/pyOCD/issues/2019), summarized in own words; confidence high, not reviewed yet.
