---
id: "iss-pyocd-632"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pip install pyocd fails in setup.py egg_info on Debian with bad marshal data"
summary: "The installed setuptools was older than 40, which pyOCD's setup.py requires (its setup_requires for setuptools >= 40.0 had no effect)."
status: "draft"
tool: "pyocd"
symptoms: ["ERROR: Complete output from command python setup.py egg_info:"]
symptom_regex: "Complete\\s+output\\s+from\\s+command\\s+python\\s+setup\\.py\\s+egg_info:"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/632"
doc_source: "https://github.com/pyocd/pyOCD/issues/632"
resolution: "user-error"
versions: "setuptools below 40; pip 19.1"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ERROR: Complete output from command python setup.py egg_info:`

## Cause

The installed setuptools was older than 40, which pyOCD's setup.py requires (its setup_requires for setuptools >= 40.0 had no effect).

## Fix

Upgrade setuptools (e.g. pip install -U pip setuptools), then install pyOCD again; pip install --force-reinstall setuptools_scm_git_archive was suggested for a corrupt helper package.

## Source

Resolution: user-error

Versions: setuptools below 40; pip 19.1

From [pyocd/pyOCD #632](https://github.com/pyocd/pyOCD/issues/632), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
