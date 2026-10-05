---
id: "iss-devtools-805"
type: "troubleshooting"
domain: "project"
title: "csolution: Regex pattern error for a component whose vendor name contains a hyphen"
summary: "The component-ID schema pattern did not allow a hyphen in the vendor part (for example Arm-Packs:: or MDK-Packs::), so schema validation rejected valid component names."
status: "draft"
tool: "csolution"
symptoms: ["error csolution: instance does not match regex pattern: (^[A-Za-z\\d][\\w+()'\\/\\- \\.]+$)|(^([A-Za-z\\d][A-Za-z\\d ]+::)?"]
symptom_regex: "instance\\s+does\\s+not\\s+match\\s+regex\\s+pattern:\\s+\\(\\^\\[A\\-Za\\-z\\\\d\\]\\[\\\\w\\+\\(\\)'\\\\/\\\\\\-\\s+\\\\\\.\\]\\+\\$\\)\\|\\(\\^\\(\\[A\\-Za\\-z\\\\d\\]\\[A\\-Za\\-z\\\\d\\s+\\]\\+::\\)\\?"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/805"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/805"
resolution: "fixed-in-release"
versions: "Fixed after 1.5.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: instance does not match regex pattern: (^[A-Za-z\d][\w+()'\/\- \.]+$)|(^([A-Za-z\d][A-Za-z\d ]+::)?`

## Cause

The component-ID schema pattern did not allow a hyphen in the vendor part (for example Arm-Packs:: or MDK-Packs::), so schema validation rejected valid component names.

## Fix

Fixed after 1.5.0 (devtools PR 777). Workarounds: omit the vendor in the component name or run csolution with --no-check-schema.

## Source

Resolution: fixed-in-release

Versions: Fixed after 1.5.0

From [Open-CMSIS-Pack/devtools #805](https://github.com/Open-CMSIS-Pack/devtools/issues/805), summarized in own words; confidence high, not reviewed yet.
