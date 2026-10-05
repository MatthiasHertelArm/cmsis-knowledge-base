---
id: "iss-pyocd-678"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Target type from a pack is 'not recognized' unless typed in uppercase"
summary: "A case-sensitive comparison somewhere in the pack target lookup contradicted the rule that target names are case-insensitive."
status: "draft"
tool: "pyocd"
symptoms: ["CRITICAL:__main__:Target type 'mimxrt0164cvl5a' not recognized."]
symptom_regex: "Target\\s+type\\s+'.*?'\\s+not\\s+recognized\\."
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/678"
doc_source: "https://github.com/pyocd/pyOCD/issues/678"
resolution: "workaround"
versions: "seen with 0.21.x"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`CRITICAL:__main__:Target type 'mimxrt0164cvl5a' not recognized.`

## Cause

A case-sensitive comparison somewhere in the pack target lookup contradicted the rule that target names are case-insensitive.

## Fix

Use the exact (upper-case) device name as listed by `pyocd pack --find`; the maintainer acknowledged the bug.

## Source

Resolution: workaround

Versions: seen with 0.21.x

From [pyocd/pyOCD #678](https://github.com/pyocd/pyOCD/issues/678), summarized in own words; confidence low, not reviewed yet.
