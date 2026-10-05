---
id: "iss-devtools-2527"
type: "troubleshooting"
domain: "project"
title: "csolution: Layer search finds nothing when the project names only a board and no device"
summary: "Layer detection required device: to be given and did not derive the device from the board's mounted device."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2527"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2527"
resolution: "fixed-in-release"
versions: "CMSIS-Toolbox 2.14 affected"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Layer detection required device: to be given and did not derive the device from the board's mounted device.

## Fix

Use the CMSIS-Toolbox nightly (as included in the CMSIS Solution extension of 2026-07-28 or later): the device is derived from the board and the layer selection appears. The pack that holds the layer must still be installed.

## Source

Resolution: fixed-in-release

Versions: CMSIS-Toolbox 2.14 affected

From [Open-CMSIS-Pack/devtools #2527](https://github.com/Open-CMSIS-Pack/devtools/issues/2527), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
