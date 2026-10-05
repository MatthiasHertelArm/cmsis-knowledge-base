---
id: "iss-devtools-1124"
type: "troubleshooting"
domain: "project"
title: "csolution: Component with older API major version gets the wrong API from the newest pack"
summary: "With two versions of a pack loaded, the newest one always wins when no version is given, so a component implementing API 0.1.0 was built against the incompatible API 1.0.0."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1124"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1124"
resolution: "fixed-in-release"
versions: "2.1.0, fixed in 2.2"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

With two versions of a pack loaded, the newest one always wins when no version is given, so a component implementing API 0.1.0 was built against the incompatible API 1.0.0.

## Fix

Fixed by new API resolution in the 2.2 timeframe: the highest API version inside the major version the component requires is chosen, an error is raised if none fits. Also avoid specifying two major pack versions concurrently.

## Source

Resolution: fixed-in-release

Versions: 2.1.0, fixed in 2.2

From [Open-CMSIS-Pack/devtools #1124](https://github.com/Open-CMSIS-Pack/devtools/issues/1124), summarized in own words; confidence high, not reviewed yet.
