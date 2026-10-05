---
id: "iss-pyocd-1600"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: HC32F460 flash fails with IPSR=3 after 0.35: wrong target name used with the pack"
summary: "The user selected the part name hc32f460jeua; the valid target names are hc32f460xc and hc32f460xe."
status: "draft"
tool: "pyocd"
symptoms: ["C target was not halted as expected after calling flash algorithm routine (IPSR=3) [__main__]"]
symptom_regex: "C\\s+target\\s+was\\s+not\\s+halted\\s+as\\s+expected\\s+after\\s+calling\\s+flash\\s+algorithm\\s+routine\\s+\\(IPSR=\\S+\\)"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1600"
doc_source: "https://github.com/pyocd/pyOCD/issues/1600"
resolution: "user-error"
versions: "0.35.0 and 0.35.1"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["HC32F460"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`C target was not halted as expected after calling flash algorithm routine (IPSR=3) [__main__]`

## Cause

The user selected the part name hc32f460jeua; the valid target names are hc32f460xc and hc32f460xe. Also, 0.35 changed flash algorithm RAM layout and 0.34 might have skipped programming through smart flash.

## Fix

Use -t hc32f460xe (or xc). Pass -Osmart_flash=0 to force programming when comparing versions.

## Source

Resolution: user-error

Versions: 0.35.0 and 0.35.1

From [pyocd/pyOCD #1600](https://github.com/pyocd/pyOCD/issues/1600), summarized in own words; confidence medium, not reviewed yet.
