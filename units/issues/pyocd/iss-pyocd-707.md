---
id: "iss-pyocd-707"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: MemoryError when reading a large memory block with 'savemem' on 32-bit Python"
summary: "A 32-bit Python process ran out of address space while building the block read buffer."
status: "draft"
tool: "pyocd"
symptoms: ["MemoryError"]
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/707"
doc_source: "https://github.com/pyocd/pyOCD/issues/707"
resolution: "user-error"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`MemoryError`

## Cause

A 32-bit Python process ran out of address space while building the block read buffer.

## Fix

Use 64-bit Python, or read in smaller chunks.

## Source

Resolution: user-error

From [pyocd/pyOCD #707](https://github.com/pyocd/pyOCD/issues/707), summarized in own words; confidence high, not reviewed yet.
