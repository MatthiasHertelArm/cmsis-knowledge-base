---
id: "iss-pyocd-1327"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: i.MX RT mass erase prints 'Mass erase failed' although flash is erased"
summary: "The erase actually succeeded; the reported failure was a spurious message in 0.33.1 and the chosen reset type was not honoured by the target class."
status: "draft"
tool: "pyocd"
symptoms: ["E Mass erase failed. [eraser]"]
symptom_regex: "E\\s+Mass\\s+erase\\s+failed\\."
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1327"
doc_source: "https://github.com/pyocd/pyOCD/issues/1327"
resolution: "fixed-in-release"
versions: "0.33.1"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"], "family": ["i.MX RT"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E Mass erase failed. [eraser]`

## Cause

The erase actually succeeded; the reported failure was a spurious message in 0.33.1 and the chosen reset type was not honoured by the target class.

## Fix

Verify by reading flash; the message is fixed in the next release.

## Source

Resolution: fixed-in-release

Versions: 0.33.1

From [pyocd/pyOCD #1327](https://github.com/pyocd/pyOCD/issues/1327), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
