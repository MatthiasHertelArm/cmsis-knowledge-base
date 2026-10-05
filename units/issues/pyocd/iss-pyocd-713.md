---
id: "iss-pyocd-713"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Flashing PSoC6 fails with \"'CY8C6xxA' object has no attribute 'options'\""
summary: "Bug in the PSoC6 target class in 0.21.0 (tracked as #680)."
status: "draft"
tool: "pyocd"
symptoms: ["uncaught exception: 'CY8C6xxA' object has no attribute 'options'"]
symptom_regex: "uncaught\\s+exception:\\s+'.*?'\\s+object\\s+has\\s+no\\s+attribute\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/713"
doc_source: "https://github.com/pyocd/pyOCD/issues/713"
resolution: "fixed-in-release"
versions: "affected 0.21.0; fixed in 0.22.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`uncaught exception: 'CY8C6xxA' object has no attribute 'options'`

## Cause

Bug in the PSoC6 target class in 0.21.0 (tracked as #680).

## Fix

Fixed on master after 0.21.0; upgrade pyOCD.

## Source

Resolution: fixed-in-release

Versions: affected 0.21.0; fixed in 0.22.0

From [pyocd/pyOCD #713](https://github.com/pyocd/pyOCD/issues/713), summarized in own words; confidence high, not reviewed yet.
