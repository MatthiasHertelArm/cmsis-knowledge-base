---
id: "iss-devtools-1650"
type: "troubleshooting"
domain: "project"
title: "csolution: Partial component name resolves to an unexpected pack's component"
summary: "csolution 2.5.0-devint5 resolved the partly specified ARM::CMSIS Driver:USART to its best match ARM::CMSIS Driver:USART:Custom from ARM::CMSIS (Custom is a Csub)."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1650"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1650"
resolution: "configuration"
versions: "CMSIS-Toolbox 2.5.0-devint5"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

csolution 2.5.0-devint5 resolved the partly specified ARM::CMSIS Driver:USART to its best match ARM::CMSIS Driver:USART:Custom from ARM::CMSIS (Custom is a Csub). The documented rule is that :Csub is not selected for the user; after a later nightly partial identifiers such as CMSIS:OS Tick no longer resolved without their Csub.

## Fix

Write the full identifier including the Csub where the component has one, for example CMSIS:OS Tick:SysTick, as done for the csolution-examples in PR #41 and other Open-CMSIS-Pack projects.

## Source

Resolution: configuration

Versions: CMSIS-Toolbox 2.5.0-devint5

From [Open-CMSIS-Pack/devtools #1650](https://github.com/Open-CMSIS-Pack/devtools/issues/1650), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
