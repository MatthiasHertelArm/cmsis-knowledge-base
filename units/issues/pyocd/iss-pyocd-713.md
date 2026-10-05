---
id: "iss-pyocd-713"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Flashing PSoC6 fails with \"'CY8C6xxA' object has no attribute 'options'\""
summary: "Bug in the PSoC6 (CY8C6xxA) target class in 0.21.0, a duplicate of #680."
status: "draft"
tool: "pyocd"
symptoms: ["uncaught exception: 'CY8C6xxA' object has no attribute 'options'"]
symptom_regex: "uncaught\\s+exception:\\s+'.*?'\\s+object\\s+has\\s+no\\s+attribute\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/713"
doc_source: "https://github.com/pyocd/pyOCD/issues/713"
resolution: "fixed-in-release"
versions: "0.21.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`uncaught exception: 'CY8C6xxA' object has no attribute 'options'`

## Cause

Bug in the PSoC6 (CY8C6xxA) target class in 0.21.0, a duplicate of #680.

## Fix

Fixed on master; use a pyOCD version after 0.21.0 that includes the fix.

## Source

Resolution: fixed-in-release

Versions: 0.21.0

From [pyocd/pyOCD #713](https://github.com/pyocd/pyOCD/issues/713), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
