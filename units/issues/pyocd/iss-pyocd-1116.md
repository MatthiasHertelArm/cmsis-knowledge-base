---
id: "iss-pyocd-1116"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Picoprobe: exception when a probe UID is given but no Picoprobe is connected"
summary: "The Picoprobe enumeration code dereferenced a missing device when a unique ID filter was set and no matching probe existed."
status: "draft"
tool: "pyocd"
symptoms: ["uncaught exception: 'NoneType' object has no attribute 'serial_number'"]
symptom_regex: "uncaught\\s+exception:\\s+'.*?'\\s+object\\s+has\\s+no\\s+attribute\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1116"
doc_source: "https://github.com/pyocd/pyOCD/issues/1116"
resolution: "fixed-in-release"
versions: "affected 0.30.0"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`uncaught exception: 'NoneType' object has no attribute 'serial_number'`

## Cause

The Picoprobe enumeration code dereferenced a missing device when a unique ID filter was set and no matching probe existed.

## Fix

Fixed in a pyOCD 0.30.x patch release; upgrade.

## Source

Resolution: fixed-in-release

Versions: affected 0.30.0

From [pyocd/pyOCD #1116](https://github.com/pyocd/pyOCD/issues/1116), summarized in own words; confidence medium, not reviewed yet.
