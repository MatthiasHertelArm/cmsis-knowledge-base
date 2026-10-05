---
id: "iss-pyocd-911"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: J-Link session open fails with AttributeError: JLinkProbe has no attribute '_lock'"
summary: "Regression in 0.27: JLinkProbe lacks the _lock attribute that DebugProbe.lock() uses, so opening a session with a J-Link fails."
status: "draft"
tool: "pyocd"
symptoms: ["'JLinkProbe' object has no attribute '_lock'"]
symptom_regex: "'.*?'\\s+object\\s+has\\s+no\\s+attribute\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/911"
doc_source: "https://github.com/pyocd/pyOCD/issues/911"
resolution: "unresolved"
versions: "0.27"
confidence: "low"
cause_origin: "issue-digest"
checked: "unsupported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`'JLinkProbe' object has no attribute '_lock'`

## Cause

Regression in 0.27: JLinkProbe lacks the _lock attribute that DebugProbe.lock() uses, so opening a session with a J-Link fails.

## Fix

The previous pyOCD version worked for the reporter; the maintainer said he would get a fix out soon.

## Source

Resolution: unresolved

Versions: 0.27

From [pyocd/pyOCD #911](https://github.com/pyocd/pyOCD/issues/911), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
