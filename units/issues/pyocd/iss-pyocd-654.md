---
id: "iss-pyocd-654"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: STM32L4 pack target: gdbserver errors with IntervalTree has no attribute overlap on halt"
summary: "The Python environment had intervaltree 2.1.0 installed, while pyOCD needs 3.x."
status: "draft"
tool: "pyocd"
symptoms: ["ERROR:gdbserver:Unhandled exception in handle_message: 'IntervalTree' object has no attribute 'overlap'"]
symptom_regex: "Unhandled\\s+exception\\s+in\\s+handle_message:\\s+'.*?'\\s+object\\s+has\\s+no\\s+attribute\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/654"
doc_source: "https://github.com/pyocd/pyOCD/issues/654"
resolution: "user-error"
versions: "intervaltree 2.1.0 (Python 2 install)"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "family": ["STM32L4 Series"], "core": ["Cortex-M4"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ERROR:gdbserver:Unhandled exception in handle_message: 'IntervalTree' object has no attribute 'overlap'`

## Cause

The Python environment had intervaltree 2.1.0 installed, while pyOCD needs 3.x. A source or editable install does not refresh dependencies after pulling new code. The generic cortex_m target avoided the error only because it has no memory map to cache.

## Fix

Upgrade intervaltree to 3.0.2 or newer (reinstall pyOCD or `pip install -r dev-requirements.txt`), preferably in a clean Python 3 virtualenv.

## Source

Resolution: user-error

Versions: intervaltree 2.1.0 (Python 2 install)

From [pyocd/pyOCD #654](https://github.com/pyocd/pyOCD/issues/654), summarized in own words; confidence high, not reviewed yet.
