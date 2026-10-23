---
id: "iss-devtools-2648"
type: "troubleshooting"
domain: "pack"
title: "svdconv: svdconv M352 overlap warning caused by one peripheral spanning two address ranges"
summary: "The SVD describes one peripheral with a single addressBlock whose size covers two separate register regions with a gap between them."
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

The SVD describes one peripheral with a single addressBlock whose size covers two separate register regions with a gap between them. That range runs into the address space of another peripheral, so svdconv reports an overlap. The SVD format assumes each peripheral occupies one contiguous block.

## Fix

Split the peripheral into two peripherals, one per contiguous region, each with its own baseAddress and a small addressBlock (for example, a 0x1000 size for each). Keep the same groupName so both still belong to the same group.

## Source

Resolution: configuration

From [Open-CMSIS-Pack/devtools #2648](https://github.com/Open-CMSIS-Pack/devtools/issues/2648), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
