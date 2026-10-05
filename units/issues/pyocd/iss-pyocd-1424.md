---
id: "iss-pyocd-1424"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: File path containing '@' breaks flash/load"
summary: "The load command treats '@<address>' after a file name as a load address, so a directory name with '@' is cut apart."
status: "draft"
tool: "pyocd"
symptoms: ["invalid literal for int() with base 0:"]
symptom_regex: "invalid\\s+literal\\s+for\\s+int\\(\\)\\s+with\\s+base\\s+\\S+:"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1424"
doc_source: "https://github.com/pyocd/pyOCD/issues/1424"
resolution: "fixed-in-release"
versions: "0.33"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`invalid literal for int() with base 0:`

## Cause

The load command treats '@<address>' after a file name as a load address, so a directory name with '@' is cut apart.

## Fix

The maintainer planned to check whether the full argument is an existing file first. Meanwhile avoid '@' in paths or use --base-address.

## Source

Resolution: fixed-in-release

Versions: 0.33

From [pyocd/pyOCD #1424](https://github.com/pyocd/pyOCD/issues/1424), summarized in own words; confidence medium, not reviewed yet.
