---
id: "iss-cpackget-283"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add of a BSP fails to install required packs: 'does not match pack version \"\"'"
summary: "Regression in cpackget 2.1.1: for dependencies of the form >=x.y.z cpackget uses an internal open upper bound (x.y.z:_) that the range comparison did not support, and the version and range arguments were swapped in the modifier resolution."
status: "draft"
tool: "cpackget"
symptoms: ["E: The latest release (18.0.0) in pack's pdsc (NXP.MIMXRT1064_DFP.pdsc) does not match pack version \"\"", "E: pack version is not the latest in the pdsc file"]
symptom_regex: "E:\\s+The\\s+latest\\s+release\\s+\\(\\S+\\)\\s+in\\s+pack's\\s+pdsc\\s+\\(NXP\\.MIMXRT1064_DFP\\.pdsc\\)\\s+does\\s+not\\s+match\\s+pack\\s+version\\s+\".*?\""
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/283"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/283"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: The latest release (18.0.0) in pack's pdsc (NXP.MIMXRT1064_DFP.pdsc) does not match pack version ""`
`E: pack version is not the latest in the pdsc file`

## Cause

Regression in cpackget 2.1.1: for dependencies of the form >=x.y.z cpackget uses an internal open upper bound (x.y.z:_) that the range comparison did not support, and the version and range arguments were swapped in the modifier resolution.

## Fix

Use a cpackget newer than 2.1.1 that contains both corrections; version 2.0.1 still installed the requirements correctly.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/cpackget #283](https://github.com/Open-CMSIS-Pack/cpackget/issues/283), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
