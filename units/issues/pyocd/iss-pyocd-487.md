---
id: "iss-pyocd-487"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pip install pyocd 0.14 fails with pip 18 and old setuptools"
summary: "The install requirements use environment markers that need a newer setuptools than the one installed (older than about 20.5)."
status: "draft"
tool: "pyocd"
symptoms: ["Command \"python setup.py egg_info\" failed with error code 1"]
symptom_regex: "Command\\s+\".*?\"\\s+failed\\s+with\\s+error\\s+code\\s+\\S+"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/487"
doc_source: "https://github.com/pyocd/pyOCD/issues/487"
resolution: "user-error"
versions: "0.12 to 0.14"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Command "python setup.py egg_info" failed with error code 1`

## Cause

The install requirements use environment markers that need a newer setuptools than the one installed (older than about 20.5).

## Fix

Upgrade setuptools (`pip install -U setuptools`) and retry.

## Source

Resolution: user-error

Versions: 0.12 to 0.14

From [pyocd/pyOCD #487](https://github.com/pyocd/pyOCD/issues/487), summarized in own words; confidence high, not reviewed yet.
