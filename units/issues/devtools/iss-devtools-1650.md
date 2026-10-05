---
id: "iss-devtools-1650"
type: "troubleshooting"
domain: "project"
title: "csolution: Partial component name resolves to an unexpected pack's component"
summary: "Partly specified component identifiers resolve to the best match, so ARM::CMSIS Driver:USART silently selected a Custom variant from another pack, and CMSIS:OS Tick stopped resolving where several subgroups exist."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1650"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1650"
resolution: "configuration"
versions: "2.5.0"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Partly specified component identifiers resolve to the best match, so ARM::CMSIS Driver:USART silently selected a Custom variant from another pack, and CMSIS:OS Tick stopped resolving where several subgroups exist.

## Fix

Write the full identifier including Csub (for example CMSIS:OS Tick:SysTick) and the vendor you want. Partial identifiers are only safe where a default implementation exists without Csub.

## Source

Resolution: configuration

Versions: 2.5.0

From [Open-CMSIS-Pack/devtools #1650](https://github.com/Open-CMSIS-Pack/devtools/issues/1650), summarized in own words; confidence medium, not reviewed yet.
