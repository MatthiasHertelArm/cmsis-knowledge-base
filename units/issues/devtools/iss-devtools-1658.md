---
id: "iss-devtools-1658"
type: "troubleshooting"
domain: "project"
title: "csolution: Layer detection fails on a multi-core device: processor must be specified"
summary: "Like board and device names, the processor name (Pname) must be fixed before layers are filtered from packs, even if the layer itself names the core."
status: "draft"
tool: "csolution"
symptoms: ["error csolution: one of the following processors must be specified:", "error csolution: error occurred during layer detection. Please review the project and its dependencies"]
symptom_regex: "one\\s+of\\s+the\\s+following\\s+processors\\s+must\\s+be\\s+specified:"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1658"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1658"
resolution: "configuration"
versions: "2.5.0"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: one of the following processors must be specified:`
`error csolution: error occurred during layer detection. Please review the project and its dependencies`

## Cause

Like board and device names, the processor name (Pname) must be fixed before layers are filtered from packs, even if the layer itself names the core.

## Fix

Add the processor to the device in the target-type, for example device: NXP::LPC55S69JBD100:cm33_core0.

## Source

Resolution: configuration

Versions: 2.5.0

From [Open-CMSIS-Pack/devtools #1658](https://github.com/Open-CMSIS-Pack/devtools/issues/1658), summarized in own words; confidence high, checked against the thread, not reviewed yet.
