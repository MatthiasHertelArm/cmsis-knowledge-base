---
id: "iss-pyocd-1400"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pip install from git develop fails in setuptools_scm with GPG signature"
summary: "setuptools_scm 6.4.2 fails on GPG-signed commits when git log shows signatures; the upstream fix (pypa/setuptools_scm#548) was due in 6.4.3, not yet released at the time."
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
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Getting requirements to build wheel ... error`

## Cause

setuptools_scm 6.4.2 fails on GPG-signed commits when git log shows signatures; the upstream fix (pypa/setuptools_scm#548) was due in 6.4.3, not yet released at the time.

## Fix

Disable signatures globally with 'git config --global log.showSignature false' before installing (setting it only in the repository did not help), or use setuptools_scm 6.4.3 once it is released.

## Source

Resolution: workaround

Versions: setuptools_scm 6.4.2

From [pyocd/pyOCD #1400](https://github.com/pyocd/pyOCD/issues/1400), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
