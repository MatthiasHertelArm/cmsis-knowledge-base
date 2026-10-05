---
id: "iss-pyocd-442"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pip install pyocd 0.13.0 fails on Linux in setup.py egg_info"
summary: "Same release mistake as the lowercase-rename problem: the sdist carried a mixed-case package folder, which broke the setuptools_scm based install on Linux."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/442"
doc_source: "https://github.com/pyocd/pyOCD/issues/442"
resolution: "fixed-in-release"
versions: "0.13.0 affected; 0.13.1 fixed"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Same release mistake as the lowercase-rename problem: the sdist carried a mixed-case package folder, which broke the setuptools_scm based install on Linux.

## Fix

Use pyOCD 0.13.1 or newer.

## Source

Resolution: fixed-in-release

Versions: 0.13.0 affected; 0.13.1 fixed

From [pyocd/pyOCD #442](https://github.com/pyocd/pyOCD/issues/442), summarized in own words; confidence high, checked against the thread, not reviewed yet.
