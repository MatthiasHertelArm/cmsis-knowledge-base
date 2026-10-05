---
id: "iss-pyocd-1600"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: HC32F460 flash fails with IPSR=3 after 0.35: wrong target name used with the pack"
summary: "Not confirmed by the reporter: a contributor who could not reproduce it with the built-in target hc32f460xe on 0.35.1 said the failure seems to come from using the pack part name hc32f460jeua instead of the built-in names hc32f460xc or hc32f460xe."
status: "draft"
tool: "pyocd"
symptoms: ["C target was not halted as expected after calling flash algorithm routine (IPSR=3) [__main__]"]
symptom_regex: "C\\s+target\\s+was\\s+not\\s+halted\\s+as\\s+expected\\s+after\\s+calling\\s+flash\\s+algorithm\\s+routine\\s+\\(IPSR=\\S+\\)"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1600"
doc_source: "https://github.com/pyocd/pyOCD/issues/1600"
resolution: "workaround"
versions: "0.34.3 works; 0.35.0 and 0.35.1 fail"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["HC32F460"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`C target was not halted as expected after calling flash algorithm routine (IPSR=3) [__main__]`

## Cause

Not confirmed by the reporter: a contributor who could not reproduce it with the built-in target hc32f460xe on 0.35.1 said the failure seems to come from using the pack part name hc32f460jeua instead of the built-in names hc32f460xc or hc32f460xe. The maintainer noted that 0.35 moved the flash algorithm to the end of RAM, and that 0.34 may not have programmed at all because smart flash skipped unchanged contents.

## Fix

Try -t hc32f460xe (or hc32f460xc) instead of the pack part name; when comparing versions, pass -Osmart_flash=0 to force programming.

## Source

Resolution: workaround

Versions: 0.34.3 works; 0.35.0 and 0.35.1 fail

From [pyocd/pyOCD #1600](https://github.com/pyocd/pyOCD/issues/1600), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
