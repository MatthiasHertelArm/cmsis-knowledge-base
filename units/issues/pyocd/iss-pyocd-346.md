---
id: "iss-pyocd-346"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd-gdbserver raises AssertionError on K64F when run under Python 3"
summary: "The old pyOCD (0.8 era) only supported Python 2.7, so startup under Python 3.6 failed."
status: "draft"
tool: "pyocd"
symptoms: ["uncaught exception:", "AssertionError"]
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/346"
doc_source: "https://github.com/pyocd/pyOCD/issues/346"
resolution: "user-error"
versions: "pyocd 0.8 and older"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["MK64FN1M0xxx12"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`uncaught exception:`
`AssertionError`

## Cause

The old pyOCD (0.8 era) only supported Python 2.7, so startup under Python 3.6 failed.

## Fix

Run it with Python 2.7 or, better, a modern pyOCD that supports Python 3.

## Source

Resolution: user-error

Versions: pyocd 0.8 and older

From [pyocd/pyOCD #346](https://github.com/pyocd/pyOCD/issues/346), summarized in own words; confidence high, not reviewed yet.
