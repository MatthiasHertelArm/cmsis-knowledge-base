---
id: "iss-pyocd-584"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Running pyOCD tests from a source tree fails: No module named pyocd._version"
summary: "The pyocd._version module is missing when the tests run from a source tree in which pyOCD was not installed."
status: "draft"
tool: "pyocd"
symptoms: ["ModuleNotFoundError: No module named 'pyocd._version'"]
symptom_regex: "ModuleNotFoundError:\\s+No\\s+module\\s+named\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/584"
doc_source: "https://github.com/pyocd/pyOCD/issues/584"
resolution: "configuration"
versions: "0.18.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ModuleNotFoundError: No module named 'pyocd._version'`

## Cause

The pyocd._version module is missing when the tests run from a source tree in which pyOCD was not installed.

## Fix

Run `pip install -r dev-requirements.txt` in the repository root (not in a subfolder), which installs pyOCD in development mode; the reporter had first worked around it by adding a _version.py with version='0.18.0' by hand.

## Source

Resolution: configuration

Versions: 0.18.0

From [pyocd/pyOCD #584](https://github.com/pyocd/pyOCD/issues/584), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
