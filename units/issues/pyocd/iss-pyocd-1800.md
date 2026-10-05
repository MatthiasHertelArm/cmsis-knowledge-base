---
id: "iss-pyocd-1800"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Connect fails on devices with an extra core not described in the debug topology"
summary: "Discovery found a second core (the HSM's Cortex-M0+ on AP #1) that the pack's debug topology does not list, and the pack target's lookup of that AP in processors_ap_map raised a KeyError during session open."
status: "draft"
tool: "pyocd"
symptoms: ["C Error: <APv1Address@0x1d6da825540 #1 dp=0> [__main__]"]
symptom_regex: "C\\s+Error:\\s+<APv1Address@\\S+\\s+\\#\\S+\\s+dp=\\S+>"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1800"
doc_source: "https://github.com/pyocd/pyOCD/issues/1800"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["PIC32CK2051SG01144"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`C Error: <APv1Address@0x1d6da825540 #1 dp=0> [__main__]`

## Cause

Discovery found a second core (the HSM's Cortex-M0+ on AP #1) that the pack's debug topology does not list, and the pack target's lookup of that AP in processors_ap_map raised a KeyError during session open.

## Fix

Use a pyOCD version containing #1865, which the maintainers said fixes it. They then planned to change it so cores missing from the debug topology are not added to the core list but stay reachable through direct AP access.

## Source

Resolution: fixed-in-release

From [pyocd/pyOCD #1800](https://github.com/pyocd/pyOCD/issues/1800), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
