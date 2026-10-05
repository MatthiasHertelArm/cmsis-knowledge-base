---
id: "iss-devtools-799"
type: "troubleshooting"
domain: "project"
title: "cbuild: ERROR M204 on RTE/_Target_1 for a project converted from uVision with no build-type"
summary: "A converted solution with target-types but no build-type makes csolution generate RTE/_<target-type> while cbuildgen 1.5.0 expects a phantom RTE/_Target_1. cbuild also no longer modifies the RTE directory by default."
status: "draft"
tool: "cbuild"
symptoms: ["ERROR M204: Path not found: c:\\projectpath\\RTE\\_Target_1"]
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/799"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/799"
resolution: "workaround"
versions: "1.5.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ERROR M204: Path not found: c:\projectpath\RTE\_Target_1`

## Cause

A converted solution with target-types but no build-type makes csolution generate RTE/_<target-type> while cbuildgen 1.5.0 expects a phantom RTE/_Target_1. cbuild also no longer modifies the RTE directory by default.

## Fix

Workaround: declare a build-type in csolution.yml (build-types: - type: any), or create the missing directory. Making target-type mandatory was discussed, and the cbuildgen behaviour was fixed in 1.7.0 (see the same symptom in the related issue).

## Source

Resolution: workaround

Versions: 1.5.0

From [Open-CMSIS-Pack/devtools #799](https://github.com/Open-CMSIS-Pack/devtools/issues/799), summarized in own words; confidence high, not reviewed yet.
