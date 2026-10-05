---
id: "iss-pyocd-508"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pip install pyocd 0.14.x fails in CI because of a non-UTF-8 locale"
summary: "setup.py read a text file with the default encoding."
status: "draft"
tool: "pyocd"
symptoms: ["Command \"python setup.py egg_info\" failed with error code 1"]
symptom_regex: "Command\\s+\".*?\"\\s+failed\\s+with\\s+error\\s+code\\s+\\S+"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/508"
doc_source: "https://github.com/pyocd/pyOCD/issues/508"
resolution: "fixed-in-release"
versions: "0.14.3 affected; 0.15.0 fixed"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Command "python setup.py egg_info" failed with error code 1`

## Cause

setup.py read a text file with the default encoding. In containers with a C or POSIX locale (and on Windows with a legacy code page) decoding failed.

## Fix

Upgrade to pyOCD 0.15.0 or later, or set a UTF-8 locale (for example LANG and LC_ALL) before running pip.

## Source

Resolution: fixed-in-release

Versions: 0.14.3 affected; 0.15.0 fixed

From [pyocd/pyOCD #508](https://github.com/pyocd/pyOCD/issues/508), summarized in own words; confidence high, not reviewed yet.
