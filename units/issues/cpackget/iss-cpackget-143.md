---
id: "iss-cpackget-143"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget rejects pack names that start with a digit"
summary: "The name pattern required a letter as first character, whereas the pack schema allows digits, underscores and dashes in any position."
status: "draft"
tool: "cpackget"
symptoms: ["E: bad pack name: it should be one of the following formats: Vendor.Pack, Vendor.Pack.x.y.z, Vendor.Pack.x.y.z.pack, or Vendor.Pack.pdsc"]
symptom_regex: "E:\\s+bad\\s+pack\\s+name:\\s+it\\s+should\\s+be\\s+one\\s+of\\s+the\\s+following\\s+formats:\\s+Vendor\\.Pack,\\s+Vendor\\.Pack\\.x\\.y\\.z,\\s+Vendor\\.Pack\\.x\\.y\\.z\\.pack,\\s+or\\s+Vendor\\.Pack\\.pdsc"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/143"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/143"
resolution: "fixed-in-release"
versions: "0.9.0 affected"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: bad pack name: it should be one of the following formats: Vendor.Pack, Vendor.Pack.x.y.z, Vendor.Pack.x.y.z.pack, or Vendor.Pack.pdsc`

## Cause

The name pattern required a letter as first character, whereas the pack schema allows digits, underscores and dashes in any position.

## Fix

Use cpackget newer than 0.9.0, where the pattern follows the pack schema.

## Source

Resolution: fixed-in-release

Versions: 0.9.0 affected

From [Open-CMSIS-Pack/cpackget #143](https://github.com/Open-CMSIS-Pack/cpackget/issues/143), summarized in own words; confidence medium, not reviewed yet.
