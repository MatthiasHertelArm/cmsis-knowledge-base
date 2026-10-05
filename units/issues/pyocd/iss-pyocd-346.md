---
id: "iss-pyocd-346"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd-gdbserver raises AssertionError on K64F when run under Python 3"
summary: "pyOCD did not yet support Python 3, and the reporter ran it under Python 3.6, so target initialisation failed with an AssertionError."
status: "draft"
tool: "pyocd"
symptoms: ["uncaught exception:", "AssertionError"]
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/346"
doc_source: "https://github.com/pyocd/pyOCD/issues/346"
resolution: "user-error"
versions: "Python 3.6 affected; Python 2.7 required"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["MK64FN1M0xxx12"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`uncaught exception:`
`AssertionError`

## Cause

pyOCD did not yet support Python 3, and the reporter ran it under Python 3.6, so target initialisation failed with an AssertionError.

## Fix

Run pyOCD with Python 2.7, as the maintainer advised; the reporter had switched to OpenOCD instead.

## Source

Resolution: user-error

Versions: Python 3.6 affected; Python 2.7 required

From [pyocd/pyOCD #346](https://github.com/pyocd/pyOCD/issues/346), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
