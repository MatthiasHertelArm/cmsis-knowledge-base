---
id: "iss-pyocd-921"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd from a distribution package (Arch AUR) fails with an import traceback at start"
summary: "The Arch AUR package did not install python-future, which pylink-square (a pyOCD dependency) requires and which pip would have installed."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/921"
doc_source: "https://github.com/pyocd/pyOCD/issues/921"
resolution: "not-a-bug"
versions: "0.27.2"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The Arch AUR package did not install python-future, which pylink-square (a pyOCD dependency) requires and which pip would have installed.

## Fix

Install the missing python-future package, or install pyOCD with pip (e.g. in an isolated environment); report it to the distribution package maintainer.

## Source

Resolution: not-a-bug

Versions: 0.27.2

From [pyocd/pyOCD #921](https://github.com/pyocd/pyOCD/issues/921), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
