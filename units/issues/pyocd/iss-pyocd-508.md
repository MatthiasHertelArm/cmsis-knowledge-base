---
id: "iss-pyocd-508"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pip install pyocd 0.14.x fails in CI because of a non-UTF-8 locale"
summary: "setup.py read README.md with the default encoding, which was ASCII in the CI container, so a non-ASCII byte made decoding fail."
status: "draft"
tool: "pyocd"
symptoms: ["Command \"python setup.py egg_info\" failed with error code 1"]
symptom_regex: "Command\\s+\".*?\"\\s+failed\\s+with\\s+error\\s+code\\s+\\S+"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/508"
doc_source: "https://github.com/pyocd/pyOCD/issues/508"
resolution: "fixed-in-release"
versions: "0.14.3 affected; 0.15.0 fixed"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Command "python setup.py egg_info" failed with error code 1`

## Cause

setup.py read README.md with the default encoding, which was ASCII in the CI container, so a non-ASCII byte made decoding fail.

## Fix

Upgrade to pyOCD 0.15.0, which the maintainer said should fix it (#495), or declare a UTF-8 locale before calling pip.

## Source

Resolution: fixed-in-release

Versions: 0.14.3 affected; 0.15.0 fixed

From [pyocd/pyOCD #508](https://github.com/pyocd/pyOCD/issues/508), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
