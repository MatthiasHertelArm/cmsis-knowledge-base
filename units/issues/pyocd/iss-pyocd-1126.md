---
id: "iss-pyocd-1126"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd list fails with 'No backend available' when libusb is missing"
summary: "The Picoprobe probe class raised an exception while enumerating when no libusb backend was installed, instead of just reporting no probes."
status: "draft"
tool: "pyocd"
symptoms: ["STLink and CMSIS-DAPv2 probes are not supported because no libusb library was found.", "CRITICAL:__main__:No backend available"]
symptom_regex: "STLink\\s+and\\s+CMSIS\\-DAPv2\\s+probes\\s+are\\s+not\\s+supported\\s+because\\s+no\\s+libusb\\s+library\\s+was\\s+found\\."
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1126"
doc_source: "https://github.com/pyocd/pyOCD/issues/1126"
resolution: "fixed-in-release"
versions: "affected 0.30.0; fixed by #1128 in following release"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`STLink and CMSIS-DAPv2 probes are not supported because no libusb library was found.`
`CRITICAL:__main__:No backend available`

## Cause

The Picoprobe probe class raised an exception while enumerating when no libusb backend was installed, instead of just reporting no probes.

## Fix

Fixed in a pyOCD 0.30.x patch release (PR #1128); installing libusb is also a workaround.

## Source

Resolution: fixed-in-release

Versions: affected 0.30.0; fixed by #1128 in following release

From [pyocd/pyOCD #1126](https://github.com/pyocd/pyOCD/issues/1126), summarized in own words; confidence medium, not reviewed yet.
