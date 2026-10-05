---
id: "iss-pyocd-877"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Scanning probes raises 'J-Link is already open' when another tool uses a J-Link"
summary: "The J-Link probe class opened every probe during enumeration and let the error propagate if another application held it."
status: "draft"
tool: "pyocd"
symptoms: ["ProbeError: J-Link is already open"]
symptom_regex: "ProbeError:\\s+J\\-Link\\s+is\\s+already\\s+open"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/877"
doc_source: "https://github.com/pyocd/pyOCD/issues/877"
resolution: "fixed-in-release"
versions: "fixed in 0.28.3"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ProbeError: J-Link is already open`

## Cause

The J-Link probe class opened every probe during enumeration and let the error propagate if another application held it.

## Fix

Fixed in pyOCD 0.28.3. Meanwhile prefix the probe UID with the plugin name, e.g. `--probe=cmsisdap:<uid>`, to restrict probing.

## Source

Resolution: fixed-in-release

Versions: fixed in 0.28.3

From [pyocd/pyOCD #877](https://github.com/pyocd/pyOCD/issues/877), summarized in own words; confidence high, not reviewed yet.
