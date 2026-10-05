---
id: "iss-devtools-816"
type: "troubleshooting"
domain: "project"
title: "csolution: Component ID schema check rejects vendor names with a hyphen (MDK-Packs::)"
summary: "The regular expression for the component ID in the yml schema did not allow a hyphen in the vendor part; the component itself is valid."
status: "draft"
tool: "csolution"
symptoms: ["String does not match the pattern of \"(^[A-Za-z\\d][\\w+()'\\/\\- \\.]+$)|(^([A-Za-z\\d][A-Za-z\\d ]+::)?"]
symptom_regex: "String\\s+does\\s+not\\s+match\\s+the\\s+pattern\\s+of\\s+\"\\(\\^\\[A\\-Za\\-z\\\\d\\]\\[\\\\w\\+\\(\\)'\\\\/\\\\\\-\\s+\\\\\\.\\]\\+\\$\\)\\|\\(\\^\\(\\[A\\-Za\\-z\\\\d\\]\\[A\\-Za\\-z\\\\d\\s+\\]\\+::\\)\\?"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/816"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/816"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`String does not match the pattern of "(^[A-Za-z\d][\w+()'\/\- \.]+$)|(^([A-Za-z\d][A-Za-z\d ]+::)?`

## Cause

The regular expression for the component ID in the yml schema did not allow a hyphen in the vendor part; the component itself is valid.

## Fix

Fixed in the next tools release (duplicate of devtools #805); update the tools.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/devtools #816](https://github.com/Open-CMSIS-Pack/devtools/issues/816), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
