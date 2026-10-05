---
id: "iss-pyocd-237"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Installing pyOCD from a GitHub source zip fails: setuptools-scm unable to detect version"
summary: "GitHub's archive downloads lack the git metadata that setuptools_scm uses to derive the version."
status: "draft"
tool: "pyocd"
symptoms: ["LookupError: setuptools-scm was unable to detect version for"]
symptom_regex: "LookupError:\\s+setuptools\\-scm\\s+was\\s+unable\\s+to\\s+detect\\s+version\\s+for"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/237"
doc_source: "https://github.com/pyocd/pyOCD/issues/237"
resolution: "fixed-in-release"
versions: "0.7.0 affected; fixed in 0.12.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`LookupError: setuptools-scm was unable to detect version for`

## Cause

GitHub's archive downloads lack the git metadata that setuptools_scm uses to derive the version.

## Fix

Install from PyPI or from a git clone (`pip install git+https://github.com/...`); the problem was avoided for release zips from 0.12.0.

## Source

Resolution: fixed-in-release

Versions: 0.7.0 affected; fixed in 0.12.0

From [pyocd/pyOCD #237](https://github.com/pyocd/pyOCD/issues/237), summarized in own words; confidence high, not reviewed yet.
