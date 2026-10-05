---
id: "iss-devtools-2127"
type: "troubleshooting"
domain: "project"
title: "csolution: list dependencies suggests components from other bundles of the same Cclass"
summary: "When a bundled component needed another component of the same Cclass, csolution offered candidates from all bundles although components of different bundles of one class cannot be selected together."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2127"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2127"
resolution: "fixed-in-release"
versions: "2.10.0"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

When a bundled component needed another component of the same Cclass, csolution offered candidates from all bundles although components of different bundles of one class cannot be selected together.

## Fix

Fixed in toolbox builds after 2.10.0; only components from the same bundle are proposed now.

## Source

Resolution: fixed-in-release

Versions: 2.10.0

From [Open-CMSIS-Pack/devtools #2127](https://github.com/Open-CMSIS-Pack/devtools/issues/2127), summarized in own words; confidence high, checked against the thread, not reviewed yet.
