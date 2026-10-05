---
id: "iss-toolbox-118"
type: "troubleshooting"
domain: "pack"
title: "cpackget: Installing a local pack fails while resolving its dependencies"
summary: "Regression in the cpackget version of toolbox 2.3.0: the version of a dependency given with a modifier was lost, so an empty version was requested."
status: "draft"
tool: "cpackget"
symptoms: ["E: The latest release (1.15.0) in pack's pdsc (ARM.CMSIS-DSP.pdsc) does not match pack version \"\""]
symptom_regex: "E:\\s+The\\s+latest\\s+release\\s+\\(\\S+\\)\\s+in\\s+pack's\\s+pdsc\\s+\\(ARM\\.CMSIS\\-DSP\\.pdsc\\)\\s+does\\s+not\\s+match\\s+pack\\s+version\\s+\".*?\""
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/118"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/118"
resolution: "fixed-in-release"
versions: "2.3.0; fixed in 2.4.0"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: The latest release (1.15.0) in pack's pdsc (ARM.CMSIS-DSP.pdsc) does not match pack version ""`

## Cause

Regression in the cpackget version of toolbox 2.3.0: the version of a dependency given with a modifier was lost, so an empty version was requested.

## Fix

Use toolbox 2.2.1 until upgrading, or 2.4.0 and later where it is fixed; installing the dependency by hand with cpackget add <pack>@<version> also works.

## Source

Resolution: fixed-in-release

Versions: 2.3.0; fixed in 2.4.0

From [Open-CMSIS-Pack/cmsis-toolbox #118](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/118), summarized in own words; confidence high, checked against the thread, not reviewed yet.
