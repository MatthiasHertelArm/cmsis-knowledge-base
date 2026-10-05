---
id: "iss-pyocd-465"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: ImportError for pyocd.tools.gdb_server after upgrading to 0.13"
summary: "The 0.13.0 source package on PyPI shipped the package folder with mixed case (pyOCD) because the release was built on a case-insensitive filesystem; imports of pyocd then failed."
status: "draft"
tool: "pyocd"
symptoms: ["ImportError: No module named pyocd.tools.gdb_server"]
symptom_regex: "ImportError:\\s+No\\s+module\\s+named\\s+pyocd\\.tools\\.gdb_server"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/465"
doc_source: "https://github.com/pyocd/pyOCD/issues/465"
resolution: "fixed-in-release"
versions: "0.13.0 affected; 0.13.1 fixed"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ImportError: No module named pyocd.tools.gdb_server`

## Cause

The 0.13.0 source package on PyPI shipped the package folder with mixed case (pyOCD) because the release was built on a case-insensitive filesystem; imports of pyocd then failed.

## Fix

Install pyOCD 0.13.1 or newer; if stuck, reinstall in a clean virtualenv.

## Source

Resolution: fixed-in-release

Versions: 0.13.0 affected; 0.13.1 fixed

From [pyocd/pyOCD #465](https://github.com/pyocd/pyOCD/issues/465), summarized in own words; confidence medium, not reviewed yet.
