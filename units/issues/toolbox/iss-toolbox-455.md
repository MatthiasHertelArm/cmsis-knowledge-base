---
id: "iss-toolbox-455"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: cbridge writes wrong relative paths for middleware files in cgen.yml (e.g. FreeRTOS)"
summary: "For middleware selected in the CubeMX .ioc the relative path of the files was computed without the STM32CubeMX folder prefix, so the build did not find the sources."
status: "draft"
tool: "cmsis-solution"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/455"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/455"
resolution: "fixed-in-release"
versions: "fixed in toolbox 2.13.0"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cbridge"], "family": ["STM32H5 Series"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

For middleware selected in the CubeMX .ioc the relative path of the files was computed without the STM32CubeMX folder prefix, so the build did not find the sources.

## Fix

Use cbridge 0.9.19-23 or later (toolbox 2.13.0 and CMSIS Solution 1.64.2) and let CubeMX regenerate to rewrite the cgen.yml.

## Source

Resolution: fixed-in-release

Versions: fixed in toolbox 2.13.0

From [Open-CMSIS-Pack/cmsis-toolbox #455](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/455), summarized in own words; confidence high, checked against the thread, not reviewed yet.
