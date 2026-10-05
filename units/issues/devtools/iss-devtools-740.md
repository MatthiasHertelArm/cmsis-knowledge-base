---
id: "iss-devtools-740"
type: "troubleshooting"
domain: "project"
title: "csolution: Partly specified component is not resolved using isDefaultVariant of the pack"
summary: "csolution first collects all matching components and picks the best one, rather than using the pack's default variant like the RTE model does; a partial name is accepted only if it has exactly one match, otherwise the highest version wins."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/740"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/740"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

csolution first collects all matching components and picks the best one, rather than using the pack's default variant like the RTE model does; a partial name is accepted only if it has exactly one match, otherwise the highest version wins.

## Fix

Name the Cvariant explicitly in the component ID (an empty variant can be written as a trailing &). Behaviour change released in CMSIS-Toolbox 2.0.0-dev3.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/devtools #740](https://github.com/Open-CMSIS-Pack/devtools/issues/740), summarized in own words; confidence medium, not reviewed yet.
