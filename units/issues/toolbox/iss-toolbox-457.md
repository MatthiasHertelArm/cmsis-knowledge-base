---
id: "iss-toolbox-457"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: CubeMX does not produce the cgen.yml after changing Project Manager settings"
summary: "cbridge cannot create the cgen.yml when no peripheral uses the HAL driver (for example all switched to LL)."
status: "draft"
tool: "cmsis-solution"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/457"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/457"
resolution: "workaround"
versions: "cbridge with toolbox 2.12.0"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbridge"], "family": ["STM32F4 Series"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

cbridge cannot create the cgen.yml when no peripheral uses the HAL driver (for example all switched to LL). Same limitation as an open generator-bridge issue.

## Fix

Keep HAL selected for at least one peripheral so cbridge can write the cgen.yml, then generate again.

## Source

Resolution: workaround

Versions: cbridge with toolbox 2.12.0

From [Open-CMSIS-Pack/cmsis-toolbox #457](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/457), summarized in own words; confidence medium, not reviewed yet.
