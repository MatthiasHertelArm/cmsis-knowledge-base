---
id: "iss-devtools-343"
type: "troubleshooting"
domain: "project"
title: "csolution: Generated cprj references a pack version that was not requested for a local pack"
summary: "The version of a locally registered pack came from local_repository.pidx and could differ from the pdsc."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/343"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/343"
resolution: "fixed-in-release"
versions: "fixed in 1.0.0"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The version of a locally registered pack came from local_repository.pidx and could differ from the pdsc.

## Fix

Fixed in CMSIS-Toolbox 1.0.0: tools read the version from the pdsc file.

## Source

Resolution: fixed-in-release

Versions: fixed in 1.0.0

From [Open-CMSIS-Pack/devtools #343](https://github.com/Open-CMSIS-Pack/devtools/issues/343), summarized in own words; confidence medium, not reviewed yet.
