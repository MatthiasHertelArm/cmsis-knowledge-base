---
id: "iss-devtools-1846"
type: "troubleshooting"
domain: "project"
title: "csolution: Regions header not found when board: includes the vendor and $Bname$ is used"
summary: "$Bname$ expanded to the whole board string including vendor::, so the file name looked up differs from the generated regions_<board>.h."
status: "draft"
tool: "csolution"
symptoms: ["RTE/Device/MCXN947VDF_cm33_core0/regions_NXP::FRDM-MCXN947.h - warning csolution: specified regions header was not found"]
symptom_regex: "specified\\s+regions\\s+header\\s+was\\s+not\\s+found"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1846"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1846"
resolution: "fixed-in-release"
versions: "2.6.1"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`RTE/Device/MCXN947VDF_cm33_core0/regions_NXP::FRDM-MCXN947.h - warning csolution: specified regions header was not found`

## Cause

$Bname$ expanded to the whole board string including vendor::, so the file name looked up differs from the generated regions_<board>.h.

## Fix

Workaround: write board: without the vendor:: prefix. Fixed in toolbox nightlies after 2.6.1.

## Source

Resolution: fixed-in-release

Versions: 2.6.1

From [Open-CMSIS-Pack/devtools #1846](https://github.com/Open-CMSIS-Pack/devtools/issues/1846), summarized in own words; confidence high, checked against the thread, not reviewed yet.
