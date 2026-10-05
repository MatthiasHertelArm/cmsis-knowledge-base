---
id: "iss-pyocd-1400"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pip install from git develop fails in setuptools_scm with GPG signature"
summary: "setuptools_scm 6.4.2 chokes on signed commits when git log shows signatures; fixed in 6.4.3."
status: "draft"
tool: "pyocd"
symptoms: ["Getting requirements to build wheel ... error"]
symptom_regex: "Getting\\s+requirements\\s+to\\s+build\\s+wheel\\s+\\.\\.\\.\\s+error"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1400"
doc_source: "https://github.com/pyocd/pyOCD/issues/1400"
resolution: "workaround"
versions: "setuptools_scm 6.4.2"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Getting requirements to build wheel ... error`

## Cause

setuptools_scm 6.4.2 chokes on signed commits when git log shows signatures; fixed in 6.4.3.

## Fix

Run 'git config --global log.showSignature false' before installing, or upgrade setuptools_scm.

## Source

Resolution: workaround

Versions: setuptools_scm 6.4.2

From [pyocd/pyOCD #1400](https://github.com/pyocd/pyOCD/issues/1400), summarized in own words; confidence medium, not reviewed yet.
