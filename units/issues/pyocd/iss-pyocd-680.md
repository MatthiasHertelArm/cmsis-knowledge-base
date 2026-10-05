---
id: "iss-pyocd-680"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: gdbserver for PSoC6 (cy8c6xxa, cy8c6xx7) crashes: object has no attribute 'options'"
summary: "The PSoC6 target classes in 0.21.0 accessed an options attribute that did not exist yet during init (regression since 0.16)."
status: "draft"
tool: "pyocd"
symptoms: ["uncaught exception: 'CY8C6xx7' object has no attribute 'options'"]
symptom_regex: "uncaught\\s+exception:\\s+'.*?'\\s+object\\s+has\\s+no\\s+attribute\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/680"
doc_source: "https://github.com/pyocd/pyOCD/issues/680"
resolution: "fixed-in-release"
versions: "affected 0.21.0; fixed in 0.22.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "family": ["PSoC6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`uncaught exception: 'CY8C6xx7' object has no attribute 'options'`

## Cause

The PSoC6 target classes in 0.21.0 accessed an options attribute that did not exist yet during init (regression since 0.16).

## Fix

Upgrade to pyOCD 0.22.0 or later.

## Source

Resolution: fixed-in-release

Versions: affected 0.21.0; fixed in 0.22.0

From [pyocd/pyOCD #680](https://github.com/pyocd/pyOCD/issues/680), summarized in own words; confidence high, not reviewed yet.
