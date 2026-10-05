---
id: "iss-pyocd-1363"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd reset with hardware reset does nothing on K64F"
summary: "The hardware reset path was broken for this target; software reset worked."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1363"
doc_source: "https://github.com/pyocd/pyOCD/issues/1363"
resolution: "fixed-in-release"
versions: "0.29.0"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["K64F"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The hardware reset path was broken for this target; software reset worked.

## Fix

Use 'pyocd reset -m sw' meanwhile; fixed in a later release.

## Source

Resolution: fixed-in-release

Versions: 0.29.0

From [pyocd/pyOCD #1363](https://github.com/pyocd/pyOCD/issues/1363), summarized in own words; confidence medium, not reviewed yet.
