---
id: "iss-pyocd-921"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd from a distribution package (Arch AUR) fails with an import traceback at start"
summary: "The distribution package missed a Python dependency (python-future) that pip would have installed."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/921"
doc_source: "https://github.com/pyocd/pyOCD/issues/921"
resolution: "user-error"
versions: "seen with 0.27.2"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The distribution package missed a Python dependency (python-future) that pip would have installed.

## Fix

Install the missing module (pip install future) or install pyocd with pip in a virtualenv; report to the package maintainer.

## Source

Resolution: user-error

Versions: seen with 0.27.2

From [pyocd/pyOCD #921](https://github.com/pyocd/pyOCD/issues/921), summarized in own words; confidence high, not reviewed yet.
