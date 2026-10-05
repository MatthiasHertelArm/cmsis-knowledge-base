---
id: "iss-cpackget-98"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget rejects pack versions with leading zeros such as 1.22.02"
summary: "The strict semantic-versioning regular expression disallowed leading zeros in numeric fields, but the pack schema permits them."
status: "draft"
tool: "cpackget"
symptoms: ["E: bad pack name: it should be one of the following formats: Vendor.Pack, Vendor.Pack.x.y.z, Vendor.Pack.x.y.z.pack, or Vendor.Pack.pdsc"]
symptom_regex: "E:\\s+bad\\s+pack\\s+name:\\s+it\\s+should\\s+be\\s+one\\s+of\\s+the\\s+following\\s+formats:\\s+Vendor\\.Pack,\\s+Vendor\\.Pack\\.x\\.y\\.z,\\s+Vendor\\.Pack\\.x\\.y\\.z\\.pack,\\s+or\\s+Vendor\\.Pack\\.pdsc"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/98"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/98"
resolution: "fixed-in-release"
versions: "0.5.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: bad pack name: it should be one of the following formats: Vendor.Pack, Vendor.Pack.x.y.z, Vendor.Pack.x.y.z.pack, or Vendor.Pack.pdsc`

## Cause

The strict semantic-versioning regular expression disallowed leading zeros in numeric fields, but the pack schema permits them.

## Fix

Use a cpackget after 0.5.0 where the expression was relaxed (install folders keep the leading zeros).

## Source

Resolution: fixed-in-release

Versions: 0.5.0

From [Open-CMSIS-Pack/cpackget #98](https://github.com/Open-CMSIS-Pack/cpackget/issues/98), summarized in own words; confidence high, not reviewed yet.
