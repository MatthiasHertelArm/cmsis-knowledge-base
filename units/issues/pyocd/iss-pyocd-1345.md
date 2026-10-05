---
id: "iss-pyocd-1345"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Session open fails: 'SYS_AP_PSoC64' object has no attribute 'core'"
summary: "GenericMemAPTarget inherits from CoreSightComponent instead of CoreSightCoreComponent (as it did in 0.32.3), so DebugContext's isinstance check fails when a session is opened."
status: "draft"
tool: "pyocd"
symptoms: ["'SYS_AP_PSoC64' object has no attribute 'core'"]
symptom_regex: "'.*?'\\s+object\\s+has\\s+no\\s+attribute\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1345"
doc_source: "https://github.com/pyocd/pyOCD/issues/1345"
resolution: "unresolved"
versions: "0.32.3"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`'SYS_AP_PSoC64' object has no attribute 'core'`

## Cause

GenericMemAPTarget inherits from CoreSightComponent instead of CoreSightCoreComponent (as it did in 0.32.3), so DebugContext's isinstance check fails when a session is opened.

## Fix

The maintainer said pull request #1350 should fix it; not confirmed in the thread.

## Source

Resolution: unresolved

Versions: 0.32.3

From [pyocd/pyOCD #1345](https://github.com/pyocd/pyOCD/issues/1345), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
