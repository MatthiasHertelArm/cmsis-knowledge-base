---
id: "iss-pyocd-1424"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: File path containing '@' breaks flash/load"
summary: "The flash/load command treats an '@<address>' suffix on a file name as the load address, so a path containing '@' is split and the rest parsed as an integer."
status: "draft"
tool: "pyocd"
symptoms: ["invalid literal for int() with base 0:"]
symptom_regex: "invalid\\s+literal\\s+for\\s+int\\(\\)\\s+with\\s+base\\s+\\S+:"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1424"
doc_source: "https://github.com/pyocd/pyOCD/issues/1424"
resolution: "unresolved"
confidence: "low"
cause_origin: "issue-digest"
checked: "unsupported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`invalid literal for int() with base 0:`

## Cause

The flash/load command treats an '@<address>' suffix on a file name as the load address, so a path containing '@' is split and the rest parsed as an integer.

## Fix

No fix in the thread; the maintainer planned to check whether a file with the full argument exists before processing the '@' suffix.

## Source

Resolution: unresolved

From [pyocd/pyOCD #1424](https://github.com/pyocd/pyOCD/issues/1424), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
