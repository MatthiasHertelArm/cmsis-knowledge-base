---
id: "iss-pyocd-467"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: mbedgt fails with 'No module named pyOCD.board' after upgrading pyOCD to 0.13 or newer"
summary: "htrun (mbed-host-tests, used by greentea) was not compatible with pyOCD 0.13 and later and still looked for the pyOCD.board module."
status: "draft"
tool: "pyocd"
symptoms: ["mbedgt: No module named pyOCD.board"]
symptom_regex: "mbedgt:\\s+No\\s+module\\s+named\\s+pyOCD\\.board"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/467"
doc_source: "https://github.com/pyocd/pyOCD/issues/467"
resolution: "fixed-in-release"
versions: "pyOCD 0.13 to 0.14.2 with mbed-host-tests below 1.4.4; mbed-host-tests 1.4.4 fixed"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`mbedgt: No module named pyOCD.board`

## Cause

htrun (mbed-host-tests, used by greentea) was not compatible with pyOCD 0.13 and later and still looked for the pyOCD.board module.

## Fix

Upgrade mbed-host-tests to 1.4.4 or newer (upgrading mbed-greentea also brings a newer one); downgrading pyOCD to 0.12 also avoided the error.

## Source

Resolution: fixed-in-release

Versions: pyOCD 0.13 to 0.14.2 with mbed-host-tests below 1.4.4; mbed-host-tests 1.4.4 fixed

From [pyocd/pyOCD #467](https://github.com/pyocd/pyOCD/issues/467), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
