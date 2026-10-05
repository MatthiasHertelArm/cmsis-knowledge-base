---
id: "iss-pyocd-1810"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Semihosting read of zero bytes crashes the gdbserver with TypeError"
summary: "The semihosting console read computed the result from the data length before checking that any data was returned."
status: "draft"
tool: "pyocd"
symptoms: ["TypeError: object of type 'NoneType' has no len()"]
symptom_regex: "TypeError:\\s+object\\s+of\\s+type\\s+'.*?'\\s+has\\s+no\\s+len\\(\\)"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1810"
doc_source: "https://github.com/pyocd/pyOCD/issues/1810"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`TypeError: object of type 'NoneType' has no len()`

## Cause

The semihosting console read computed the result from the data length before checking that any data was returned.

## Fix

Fixed in change #1811; update pyOCD.

## Source

Resolution: fixed-in-release

From [pyocd/pyOCD #1810](https://github.com/pyocd/pyOCD/issues/1810), summarized in own words; confidence high, checked against the thread, not reviewed yet.
