---
id: "iss-pyocd-467"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: mbedgt fails with 'No module named pyOCD.board' after upgrading pyOCD to 0.13 or newer"
summary: "pyOCD 0.13 renamed the package to lowercase pyocd; the greentea host tests (htrun) still imported the old name."
status: "draft"
tool: "pyocd"
symptoms: ["mbedgt: No module named pyOCD.board"]
symptom_regex: "mbedgt:\\s+No\\s+module\\s+named\\s+pyOCD\\.board"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/467"
doc_source: "https://github.com/pyocd/pyOCD/issues/467"
resolution: "fixed-in-release"
versions: "pyOCD 0.13 and later with htrun below 1.4.4"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`mbedgt: No module named pyOCD.board`

## Cause

pyOCD 0.13 renamed the package to lowercase pyocd; the greentea host tests (htrun) still imported the old name.

## Fix

Upgrade mbed-host-tests to 1.4.4 or newer (and mbed-greentea), or keep greentea in its own virtualenv with an old pyOCD.

## Source

Resolution: fixed-in-release

Versions: pyOCD 0.13 and later with htrun below 1.4.4

From [pyocd/pyOCD #467](https://github.com/pyocd/pyOCD/issues/467), summarized in own words; confidence high, not reviewed yet.
