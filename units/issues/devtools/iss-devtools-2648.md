---
id: "iss-devtools-2648"
type: "troubleshooting"
domain: "pack"
title: "svdconv: svdconv M352: address block of a peripheral overlaps another peripheral"
summary: "The SVD describes one peripheral with a single address block whose size spans a large range that contains a second bus interface of the same module."
status: "draft"
tool: "svdconv"
symptoms: ["AddressBlock of Peripheral 'POK' (@0x500A9000) [0x500A90FF ... 0x500A9000] overlaps 'ASG' (@0x50097000) [0x58027FFF ... 0x50097000]"]
symptom_regex: "AddressBlock\\s+of\\s+Peripheral\\s+'.*?'\\s+\\(@\\S+\\)\\s+\\[\\S+\\s+\\.\\.\\.\\s+\\S+\\]\\s+overlaps\\s+'.*?'\\s+\\(@\\S+\\)\\s+\\[\\S+\\s+\\.\\.\\.\\s+\\S+\\]"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2648"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2648"
resolution: "workaround"
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

The SVD describes one peripheral with a single address block whose size spans a large range that contains a second bus interface of the same module. Since the block is assumed to be one continuous range, its extent runs into the address range of another peripheral, which svdconv reports as an overlap.

## Fix

Split the module into two peripherals, ASG-low at 0x50097000 and ASG-high at 0x58010000, each with a compact 0x1000 address block covering its register range and sharing groupName ASG. This is the workaround suggested by a commenter; the thread does not confirm that it removes the warning.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/devtools #2648](https://github.com/Open-CMSIS-Pack/devtools/issues/2648), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
