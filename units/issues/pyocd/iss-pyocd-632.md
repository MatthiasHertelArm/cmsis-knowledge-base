---
id: "iss-pyocd-632"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pip install pyocd fails in setup.py egg_info on Debian with bad marshal data"
summary: "The installed setuptools was older than 40, which pyOCD's setup (setuptools_scm based) needs."
status: "draft"
tool: "pyocd"
symptoms: ["ERROR: Complete output from command python setup.py egg_info:"]
symptom_regex: "Complete\\s+output\\s+from\\s+command\\s+python\\s+setup\\.py\\s+egg_info:"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/632"
doc_source: "https://github.com/pyocd/pyOCD/issues/632"
resolution: "user-error"
versions: "pyocd 0.2x with setuptools below 40"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ERROR: Complete output from command python setup.py egg_info:`

## Cause

The installed setuptools was older than 40, which pyOCD's setup (setuptools_scm based) needs.

## Fix

Upgrade pip and setuptools first (`pip install -U pip setuptools`), then reinstall pyOCD; `pip install --force-reinstall setuptools_scm_git_archive` can also repair a corrupt helper package.

## Source

Resolution: user-error

Versions: pyocd 0.2x with setuptools below 40

From [pyocd/pyOCD #632](https://github.com/pyocd/pyOCD/issues/632), summarized in own words; confidence high, not reviewed yet.
