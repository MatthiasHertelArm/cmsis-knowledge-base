---
id: "iss-pyocd-1955"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Pack defines DHCSR_Addr in <debugvars>: 'attempt to modify read-only variable'"
summary: "Variables declared in a pack's global debugvars are read-only."
status: "draft"
tool: "pyocd"
symptoms: ["RuntimeError: attempt to modify read-only variable 'DHCSR_Addr'"]
symptom_regex: "RuntimeError:\\s+attempt\\s+to\\s+modify\\s+read\\-only\\s+variable\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1955"
doc_source: "https://github.com/pyocd/pyOCD/issues/1955"
resolution: "fixed-in-release"
versions: "broken 0.44.0, fixed 0.44.1"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "family": ["SAML11"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`RuntimeError: attempt to modify read-only variable 'DHCSR_Addr'`

## Cause

Variables declared in a pack's global debugvars are read-only. From 0.44.0 the default debug sequences (such as DebugCoreStart) are used when a pack lacks its own, and they declared locals with the same names, which clashed with the pack's global.

## Fix

Upgrade to 0.44.1, where the locals in the default sequences carry a '__' prefix. Alternatively avoid reusing the register-address variable names as global debugvars.

## Source

Resolution: fixed-in-release

Versions: broken 0.44.0, fixed 0.44.1

From [pyocd/pyOCD #1955](https://github.com/pyocd/pyOCD/issues/1955), summarized in own words; confidence high, not reviewed yet.
