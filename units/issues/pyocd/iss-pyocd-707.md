---
id: "iss-pyocd-707"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: MemoryError when reading a large memory block with 'savemem' on 32-bit Python"
summary: "A 32-bit Python process ran out of memory while building the buffer for a large savemem block read (pyOCD represents data as lists of integers)."
status: "draft"
tool: "pyocd"
symptoms: ["MemoryError"]
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/707"
doc_source: "https://github.com/pyocd/pyOCD/issues/707"
resolution: "workaround"
versions: "Python 2.7 32-bit"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`MemoryError`

## Cause

A 32-bit Python process ran out of memory while building the buffer for a large savemem block read (pyOCD represents data as lists of integers).

## Fix

Use 64-bit Python; the reporter confirmed it works there.

## Source

Resolution: workaround

Versions: Python 2.7 32-bit

From [pyocd/pyOCD #707](https://github.com/pyocd/pyOCD/issues/707), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
