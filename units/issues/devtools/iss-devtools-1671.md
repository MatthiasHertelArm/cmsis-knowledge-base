---
id: "iss-devtools-1671"
type: "troubleshooting"
domain: "project"
title: "csolution: board with vendor prefix not found although the pack is installed"
summary: "The board identifier was built from the device vendor (ABOV Semiconductor) or pack vendor string instead of the board's vendor attribute; the board is defined with a different vendor attribute than the pack vendor."
status: "draft"
tool: "csolution"
symptoms: ["error csolution: board 'ABOV::StarterKit-A31G112CL:V1.1' was not found"]
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1671"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1671"
resolution: "fixed-in-release"
versions: "2.5.0"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: board 'ABOV::StarterKit-A31G112CL:V1.1' was not found`

## Cause

The board identifier was built from the device vendor (ABOV Semiconductor) or pack vendor string instead of the board's vendor attribute; the board is defined with a different vendor attribute than the pack vendor.

## Fix

Fixed in csolution nightlies after 2.5.0: csolution list boards now prints the matching board id (ABOV::StarterKit-A31G112CL:V1.1). Use the id from csolution list boards -f <name>.

## Source

Resolution: fixed-in-release

Versions: 2.5.0

From [Open-CMSIS-Pack/devtools #1671](https://github.com/Open-CMSIS-Pack/devtools/issues/1671), summarized in own words; confidence medium, not reviewed yet.
