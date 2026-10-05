---
id: "iss-pyocd-678"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Target type from a pack is 'not recognized' unless typed in uppercase"
summary: "A case-sensitive comparison somewhere in the pack target lookup, although pyOCD is meant to compare target types case-insensitively; the maintainer reproduced it with pyocd pack --find."
status: "draft"
tool: "pyocd"
symptoms: ["CRITICAL:__main__:Target type 'mimxrt0164cvl5a' not recognized."]
symptom_regex: "Target\\s+type\\s+'.*?'\\s+not\\s+recognized\\."
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/678"
doc_source: "https://github.com/pyocd/pyOCD/issues/678"
resolution: "workaround"
versions: "NXP.MIMXRT1064_DFP 10.0.0"
confidence: "low"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`CRITICAL:__main__:Target type 'mimxrt0164cvl5a' not recognized.`

## Cause

A case-sensitive comparison somewhere in the pack target lookup, although pyOCD is meant to compare target types case-insensitively; the maintainer reproduced it with pyocd pack --find.

## Fix

Use the target name in upper case; the reporter changed the board's target name in pyocd/board/board_ids.py to upper case and the error went away.

## Source

Resolution: workaround

Versions: NXP.MIMXRT1064_DFP 10.0.0

From [pyocd/pyOCD #678](https://github.com/pyocd/pyOCD/issues/678), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
