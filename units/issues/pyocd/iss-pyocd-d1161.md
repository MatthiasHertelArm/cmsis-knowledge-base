---
id: "iss-pyocd-d1161"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: micro:bit v2 not recognised and falls back to generic cortex_m target"
summary: "The micro:bit v2 uses an nRF52833 with a new board ID that older pyOCD releases did not know, and there was no built-in nRF52833 target."
status: "draft"
tool: "pyocd"
symptoms: ["Board ID 9904 is not recognised, using generic cortex_m target."]
symptom_regex: "Board\\s+ID\\s+\\S+\\s+is\\s+not\\s+recognised,\\s+using\\s+generic\\s+cortex_m\\s+target\\."
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/discussions/1161"
doc_source: "https://github.com/pyocd/pyOCD/discussions/1161"
resolution: "fixed-in-release"
versions: "Fixed in pyOCD 0.31.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["nRF52833"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Board ID 9904 is not recognised, using generic cortex_m target.`

## Cause

The micro:bit v2 uses an nRF52833 with a new board ID that older pyOCD releases did not know, and there was no built-in nRF52833 target.

## Fix

Upgrade pyOCD to 0.31.0 or later, which includes micro:bit v2 and the nRF52833 target.

## Source

Resolution: fixed-in-release

Versions: Fixed in pyOCD 0.31.0

From [pyocd/pyOCD discussion 1161](https://github.com/pyocd/pyOCD/discussions/1161), summarized in own words; confidence high, not reviewed yet.
