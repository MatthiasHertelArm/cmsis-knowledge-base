---
id: "iss-pyocd-822"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd erase does nothing and prints 'No operation performed'"
summary: "Without positional addresses, erase intentionally does nothing unless --chip or --mass-erase is given."
status: "draft"
tool: "pyocd"
symptoms: ["WARNING:loader:No operation performed"]
symptom_regex: "No\\s+operation\\s+performed"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/822"
doc_source: "https://github.com/pyocd/pyOCD/issues/822"
resolution: "user-error"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`WARNING:loader:No operation performed`

## Cause

Without positional addresses, erase intentionally does nothing unless --chip or --mass-erase is given.

## Fix

Run `pyocd erase --chip` (or --mass-erase), or give sector addresses.

## Source

Resolution: user-error

From [pyocd/pyOCD #822](https://github.com/pyocd/pyOCD/issues/822), summarized in own words; confidence high, checked against the thread, not reviewed yet.
