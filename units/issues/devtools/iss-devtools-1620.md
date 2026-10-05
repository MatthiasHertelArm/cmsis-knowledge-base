---
id: "iss-devtools-1620"
type: "troubleshooting"
domain: "project"
title: "csolution: Build fails because an optional layer variable such as Shield-Layer is undefined"
summary: "Layer variables referenced in layers: must be defined; there is no implicit skipping of an optional layer."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1620"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1620"
resolution: "configuration"
versions: "CMSIS-Toolbox 2.5.0-devint3"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Layer variables referenced in layers: must be defined; there is no implicit skipping of an optional layer.

## Fix

Define the variable as an empty string in the target-type (variables: - Shield-Layer: ""); a layer entry with an empty path is ignored. The thread asked that layer detection list this empty variable in the cbuild-idx configurations, which was then reported to work.

## Source

Resolution: configuration

Versions: CMSIS-Toolbox 2.5.0-devint3

From [Open-CMSIS-Pack/devtools #1620](https://github.com/Open-CMSIS-Pack/devtools/issues/1620), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
