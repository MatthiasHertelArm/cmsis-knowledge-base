---
id: "iss-devtools-740"
type: "troubleshooting"
domain: "project"
title: "csolution: Partly specified component is not resolved using isDefaultVariant of the pack"
summary: "csolution first collects the matching components and then picks one, ahead of the RTE model logic that honours isDefaultVariant, so the pack's default variant was ignored."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/740"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/740"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

csolution first collects the matching components and then picks one, ahead of the RTE model logic that honours isDefaultVariant, so the pack's default variant was ignored. A partly specified component resolves only to a single match (Cversion not considered), and then the highest Cversion is taken.

## Fix

Give the full component ID including the Cvariant so that it resolves to one match. Respecting isDefaultVariant was announced for CMSIS-Toolbox 2.0.0-dev3; a trailing & to denote an empty Cvariant was proposed.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/devtools #740](https://github.com/Open-CMSIS-Pack/devtools/issues/740), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
