---
id: "iss-devtools-2648"
type: "troubleshooting"
domain: "pack"
title: "svdconv: svdconv M352: one peripheral's address block overlaps another peripheral's range"
summary: "The SVD describes one peripheral with a single address block whose size spans a range that includes another peripheral's address (POK)."
status: "draft"
tool: "svdconv"
symptoms: ["AddressBlock of Peripheral 'POK' (@0x500A9000) [0x500A90FF ... 0x500A9000] overlaps 'ASG' (@0x50097000) [0x58027FFF ... 0x50097000]"]
symptom_regex: "AddressBlock\\s+of\\s+Peripheral\\s+'.*?'\\s+\\(@\\S+\\)\\s+\\[\\S+\\s+\\.\\.\\.\\s+\\S+\\]\\s+overlaps\\s+'.*?'\\s+\\(@\\S+\\)\\s+\\[\\S+\\s+\\.\\.\\.\\s+\\S+\\]"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2648"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2648"
resolution: "configuration"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["svdconv"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`AddressBlock of Peripheral 'POK' (@0x500A9000) [0x500A90FF ... 0x500A9000] overlaps 'ASG' (@0x50097000) [0x58027FFF ... 0x50097000]`

## Cause

The SVD describes one peripheral with a single address block whose size spans a range that includes another peripheral's address (POK). The peripheral has two separate register banks with a gap between them, so one contiguous block spans the other peripheral's range.

## Fix

Split the peripheral into two SVD peripherals, one per register bank, each with its own baseAddress and a small addressBlock covering only its own range (for example ASG-low at 0x50097000 and ASG-high at 0x58010000, both with groupName ASG, each with a 0x1000 size block). The thread offers this split as a suggestion; it does not confirm the warning is gone.

## Source

Resolution: configuration

From [Open-CMSIS-Pack/devtools #2648](https://github.com/Open-CMSIS-Pack/devtools/issues/2648), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
