---
id: "iss-devtools-1668"
type: "troubleshooting"
domain: "project"
title: "csolution: found multiple mounted devices although device: is specified"
summary: "The board in the pack lists two mountedDevice entries with the same deviceIndex, which the specification does not allow, and csolution 2.5.0 did not cope with it even when device: named one of them."
status: "draft"
tool: "csolution"
symptoms: ["error csolution: found multiple mounted devices", "error csolution: one of the following devices must be specified:"]
symptom_regex: "found\\s+multiple\\s+mounted\\s+devices"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1668"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1668"
resolution: "fixed-in-release"
versions: "2.5.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: found multiple mounted devices`
`error csolution: one of the following devices must be specified:`

## Cause

The board in the pack lists two mountedDevice entries with the same deviceIndex, which the specification does not allow, and csolution 2.5.0 did not cope with it even when device: named one of them.

## Fix

Fixed in a toolbox release after 2.5.0 so the specified device selects the mounted device. The pack should also use distinct deviceIndex values.

## Source

Resolution: fixed-in-release

Versions: 2.5.0

From [Open-CMSIS-Pack/devtools #1668](https://github.com/Open-CMSIS-Pack/devtools/issues/1668), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
