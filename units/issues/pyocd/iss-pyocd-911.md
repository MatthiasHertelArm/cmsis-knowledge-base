---
id: "iss-pyocd-911"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: J-Link session open fails with AttributeError: JLinkProbe has no attribute '_lock'"
summary: "Regression in 0.27: the J-Link probe class used a lock attribute before it was created."
status: "draft"
tool: "pyocd"
symptoms: ["'JLinkProbe' object has no attribute '_lock'"]
symptom_regex: "'.*?'\\s+object\\s+has\\s+no\\s+attribute\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/911"
doc_source: "https://github.com/pyocd/pyOCD/issues/911"
resolution: "fixed-in-release"
versions: "affected 0.27.0"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`'JLinkProbe' object has no attribute '_lock'`

## Cause

Regression in 0.27: the J-Link probe class used a lock attribute before it was created.

## Fix

Upgrade to the next 0.27.x patch or later, where the maintainer fixed it.

## Source

Resolution: fixed-in-release

Versions: affected 0.27.0

From [pyocd/pyOCD #911](https://github.com/pyocd/pyOCD/issues/911), summarized in own words; confidence low, not reviewed yet.
