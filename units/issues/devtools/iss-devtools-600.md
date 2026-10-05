---
id: "iss-devtools-600"
type: "troubleshooting"
domain: "project"
title: "csolution: Component or variant names with parentheses etc. are rejected by the yml schema"
summary: "The component ID pattern in the csolution schemas was narrower than what the pack schema allows for Cclass, Cgroup, Csub and Cvariant (spaces, / ( ) . : + etc.)."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/600"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/600"
resolution: "fixed-in-release"
versions: "fixed in 1.5.0"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The component ID pattern in the csolution schemas was narrower than what the pack schema allows for Cclass, Cgroup, Csub and Cvariant (spaces, / ( ) . : + etc.).

## Fix

Pack and yml schemas were aligned in CMSIS-Toolbox 1.5.0; update the tools.

## Source

Resolution: fixed-in-release

Versions: fixed in 1.5.0

From [Open-CMSIS-Pack/devtools #600](https://github.com/Open-CMSIS-Pack/devtools/issues/600), summarized in own words; confidence medium, not reviewed yet.
