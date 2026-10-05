---
id: "iss-pyocd-306"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: gdbserver crashes with KeyError 'kl27z' for a FRDM-KL27Z without -t"
summary: "The board table named the target kl27z while the target registry used kl27z4, so the automatic lookup failed."
status: "draft"
tool: "pyocd"
symptoms: ["uncaught exception: 'kl27z'"]
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/306"
doc_source: "https://github.com/pyocd/pyOCD/issues/306"
resolution: "fixed-in-release"
versions: "0.8.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["MKL27Z64xxx4"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`uncaught exception: 'kl27z'`

## Cause

The board table named the target kl27z while the target registry used kl27z4, so the automatic lookup failed.

## Fix

Pass `-t kl27z4` or use a pyOCD version with the corrected board table (fix #307).

## Source

Resolution: fixed-in-release

Versions: 0.8.0

From [pyocd/pyOCD #306](https://github.com/pyocd/pyOCD/issues/306), summarized in own words; confidence high, not reviewed yet.
