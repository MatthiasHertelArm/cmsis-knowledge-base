---
id: "iss-cmsis6-120"
type: "troubleshooting"
domain: "core"
title: "CMSIS-Core: Warning \"__ARM_FP is not defined\" with soft float"
summary: "The headers used __ARM_FP without defined() checks."
status: "draft"
tool: "cmsis-core"
symptoms: ["warning: \"__ARM_FP\" is not defined, evaluates to 0 [-Wundef]"]
symptom_regex: "\".*?\"\\s+is\\s+not\\s+defined,\\s+evaluates\\s+to\\s+\\S+\\s+\\[\\-Wundef\\]"
collection: "issues-cmsis6"
source: "https://github.com/ARM-software/CMSIS_6/issues/120"
doc_source: "https://github.com/ARM-software/CMSIS_6/issues/120"
resolution: "fixed-in-release"
versions: "6.0.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-core"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`warning: "__ARM_FP" is not defined, evaluates to 0 [-Wundef]`

## Cause

The headers used __ARM_FP without defined() checks.

## Fix

Fixed by guarding with defined(__ARM_FP) in all profiles (PR 124).

## Source

Resolution: fixed-in-release

Versions: 6.0.0

From [ARM-software/CMSIS_6 #120](https://github.com/ARM-software/CMSIS_6/issues/120), summarized in own words; confidence high, not reviewed yet.
