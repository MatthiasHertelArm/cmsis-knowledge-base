---
id: "iss-toolbox-269"
type: "troubleshooting"
domain: "project"
title: "csolution: Packs reported not installed after upgrading to toolbox 2.7.0 (vendor case mismatch)"
summary: "Version 2.7.0 checked the letter case of pack vendor names strictly."
status: "draft"
tool: "csolution"
symptoms: ["error csolution: required pack: ARM::CMSIS-DSP@1.14.4 not installed, version fixed in *.cbuild-pack.yml file"]
symptom_regex: "required\\s+pack:\\s+ARM::CMSIS\\-DSP@\\S+\\s+not\\s+installed,\\s+version\\s+fixed\\s+in\\s+\\*\\.cbuild\\-pack\\.yml\\s+file"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/269"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/269"
resolution: "fixed-in-release"
versions: "regression in 2.7.0; reverted in 2.8.0"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: required pack: ARM::CMSIS-DSP@1.14.4 not installed, version fixed in *.cbuild-pack.yml file`

## Cause

Version 2.7.0 checked the letter case of pack vendor names strictly. On Windows packs with ARM and Arm vendor spellings share one folder, so some were not found.

## Fix

Upgrade to 2.8.0 where the strict check was reverted, or stay on 2.6.1 meanwhile.

## Source

Resolution: fixed-in-release

Versions: regression in 2.7.0; reverted in 2.8.0

From [Open-CMSIS-Pack/cmsis-toolbox #269](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/269), summarized in own words; confidence high, checked against the thread, not reviewed yet.
