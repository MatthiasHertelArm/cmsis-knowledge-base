---
id: "iss-devtools-343"
type: "troubleshooting"
domain: "project"
title: "csolution: Generated cprj references a pack version that was not requested for a local pack"
summary: "The thread gives no analysis: the cprj requested basic_trace 0.1.0 while local_repository.pidx listed 0.0.3, so the build could not find the requested version of the local pack."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/343"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/343"
resolution: "fixed-in-release"
versions: "csolution 0.9.5, cbuild 0.9.1; considered fixed in 1.0.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The thread gives no analysis: the cprj requested basic_trace 0.1.0 while local_repository.pidx listed 0.0.3, so the build could not find the requested version of the local pack.

## Fix

The maintainer considered it fixed in CMSIS-Toolbox 1.0.0 (not validated by the reporter); the tools read the version of a local pack from the pdsc file.

## Source

Resolution: fixed-in-release

Versions: csolution 0.9.5, cbuild 0.9.1; considered fixed in 1.0.0

From [Open-CMSIS-Pack/devtools #343](https://github.com/Open-CMSIS-Pack/devtools/issues/343), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
