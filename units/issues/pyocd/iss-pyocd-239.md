---
id: "iss-pyocd-239"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: DAP TransferError when flashing a K64F with blank flash"
summary: "The error occurs when the K64F's flash has been erased and left blank."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/239"
doc_source: "https://github.com/pyocd/pyOCD/issues/239"
resolution: "fixed-in-release"
versions: "pyOCD 0.7.1; interface firmware 0226 and 0241"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["MK64FN1M0xxx12"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The error occurs when the K64F's flash has been erased and left blank.

## Fix

Suggested workaround: load another image over the mass-storage interface to recover the device. The maintainer later said that problems with blank flash on Kinetis devices should all be fixed, without naming a release.

## Source

Resolution: fixed-in-release

Versions: pyOCD 0.7.1; interface firmware 0226 and 0241

From [pyocd/pyOCD #239](https://github.com/pyocd/pyOCD/issues/239), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
