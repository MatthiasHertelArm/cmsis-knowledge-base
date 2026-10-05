---
id: "iss-cpackget-143"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget rejects pack names that start with a digit"
summary: "The name pattern of cpackget 0.9.0 ([a-zA-Z][0-9a-zA-Z_\\-]+) required a letter as first character, whereas the pack schema allows digits, underscores and dashes in any position ([-_A-Za-z0-9]+)."
status: "draft"
tool: "cpackget"
symptoms: ["E: bad pack name: it should be one of the following formats: Vendor.Pack, Vendor.Pack.x.y.z, Vendor.Pack.x.y.z.pack, or Vendor.Pack.pdsc"]
symptom_regex: "E:\\s+bad\\s+pack\\s+name:\\s+it\\s+should\\s+be\\s+one\\s+of\\s+the\\s+following\\s+formats:\\s+Vendor\\.Pack,\\s+Vendor\\.Pack\\.x\\.y\\.z,\\s+Vendor\\.Pack\\.x\\.y\\.z\\.pack,\\s+or\\s+Vendor\\.Pack\\.pdsc"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/143"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/143"
resolution: "unresolved"
versions: "0.9.0"
confidence: "low"
cause_origin: "issue-digest"
checked: "unsupported"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: bad pack name: it should be one of the following formats: Vendor.Pack, Vendor.Pack.x.y.z, Vendor.Pack.x.y.z.pack, or Vendor.Pack.pdsc`

## Cause

The name pattern of cpackget 0.9.0 ([a-zA-Z][0-9a-zA-Z_\-]+) required a letter as first character, whereas the pack schema allows digits, underscores and dashes in any position ([-_A-Za-z0-9]+).

## Fix

No fix in the thread; the maintainer planned to adapt cpackget to the pack schema's name pattern.

## Source

Resolution: unresolved

Versions: 0.9.0

From [Open-CMSIS-Pack/cpackget #143](https://github.com/Open-CMSIS-Pack/cpackget/issues/143), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
