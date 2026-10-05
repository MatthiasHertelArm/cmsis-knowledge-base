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
versions: "RTE model 2.1.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

With two versions of a pack loaded, the newest one always wins when no version is given, so a component implementing API 0.1.0 was built against the incompatible API 1.0.0.

## Fix

Fixed by PR #1130: the API resolves to the highest available version inside the major version the component requires (at least the required one); an error is raised if none fits, and a conflict error if selected components require different major versions. The thread names no release.

## Source

Resolution: fixed-in-release

Versions: RTE model 2.1.0

From [Open-CMSIS-Pack/devtools #1124](https://github.com/Open-CMSIS-Pack/devtools/issues/1124), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
