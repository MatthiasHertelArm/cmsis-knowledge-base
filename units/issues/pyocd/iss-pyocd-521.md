---
id: "iss-pyocd-521"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyOCD 0.12 install pulls enum34 on Python 3.4+ and breaks the standard library"
summary: "The requirements listed enum34 unconditionally."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/521"
doc_source: "https://github.com/pyocd/pyOCD/issues/521"
resolution: "fixed-in-release"
versions: "0.12.0 affected; 0.12.1 fixed"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The requirements listed enum34 unconditionally. Installed on Python 3.4 or newer it shadows the standard enum module and breaks code that needs IntFlag.

## Fix

Install pyOCD 0.12.1 or later, which restricts enum34 to Python below 3.4; or uninstall enum34.

## Source

Resolution: fixed-in-release

Versions: 0.12.0 affected; 0.12.1 fixed

From [pyocd/pyOCD #521](https://github.com/pyocd/pyOCD/issues/521), summarized in own words; confidence high, not reviewed yet.
