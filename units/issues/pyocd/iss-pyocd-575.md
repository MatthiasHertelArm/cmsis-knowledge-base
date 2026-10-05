---
id: "iss-pyocd-575"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: STLink probe appears and disappears with 'The device has no langid' on Windows"
summary: "Probe discovery used a custom USB match that opened every device; on Windows reading the string descriptor failed at times, so the probe list flickered between filled and empty."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/575"
doc_source: "https://github.com/pyocd/pyOCD/issues/575"
resolution: "fixed-in-release"
versions: "0.19 to 0.20"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Probe discovery used a custom USB match that opened every device; on Windows reading the string descriptor failed at times, so the probe list flickered between filled and empty.

## Fix

Upgrade to a pyOCD release that fixed probe enumeration (confirmed by the reporter after the maintainer's change); a workaround was to match the ST-Link VID/PID directly.

## Source

Resolution: fixed-in-release

Versions: 0.19 to 0.20

From [pyocd/pyOCD #575](https://github.com/pyocd/pyOCD/issues/575), summarized in own words; confidence medium, not reviewed yet.
