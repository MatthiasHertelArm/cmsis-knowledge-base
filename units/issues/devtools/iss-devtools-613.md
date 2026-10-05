---
id: "iss-devtools-613"
type: "troubleshooting"
domain: "project"
title: "csolution: RTE/Device contains *.update@<version> files although no *.base@<version> exists"
summary: "An .update file is written whenever the pack's config file version differs from the one in the project or no base file is known; a base file can only be written when the original version is known."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/613"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/613"
resolution: "fixed-in-release"
versions: "csolution 1.3.0; changed in 1.4.0"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

An .update file is written whenever the pack's config file version differs from the one in the project or no base file is known; a base file can only be written when the original version is known. Mixed .base/.update output for one component was considered confusing.

## Fix

Behaviour changed in CMSIS-Toolbox 1.4.0: .base is created when a config file is first copied into the project RTE, and .update only if a .base exists.

## Source

Resolution: fixed-in-release

Versions: csolution 1.3.0; changed in 1.4.0

From [Open-CMSIS-Pack/devtools #613](https://github.com/Open-CMSIS-Pack/devtools/issues/613), summarized in own words; confidence medium, not reviewed yet.
