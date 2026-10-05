---
id: "iss-devtools-1242"
type: "troubleshooting"
domain: "pack"
title: "cpackget: Installing a local .pack with spaces in the path fails with bad pack name"
summary: "The MDK Pack Installer (uVision 5.39) called cpackget without quoting the pack path, so a path containing a space was split into two arguments."
status: "draft"
tool: "cpackget"
symptoms: ["E: bad pack name: it should be one of the following formats: Vendor.Pack, Vendor.Pack.x.y.z, Vendor.Pack.x.y.z.pack, or Vendor.Pack.pdsc", "E: file not found"]
symptom_regex: "E:\\s+bad\\s+pack\\s+name:\\s+it\\s+should\\s+be\\s+one\\s+of\\s+the\\s+following\\s+formats:\\s+Vendor\\.Pack,\\s+Vendor\\.Pack\\.x\\.y\\.z,\\s+Vendor\\.Pack\\.x\\.y\\.z\\.pack,\\s+or\\s+Vendor\\.Pack\\.pdsc"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1242"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1242"
resolution: "workaround"
versions: "MDK 5.39"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: bad pack name: it should be one of the following formats: Vendor.Pack, Vendor.Pack.x.y.z, Vendor.Pack.x.y.z.pack, or Vendor.Pack.pdsc`
`E: file not found`

## Cause

The MDK Pack Installer (uVision 5.39) called cpackget without quoting the pack path, so a path containing a space was split into two arguments.

## Fix

Not a cpackget defect: running cpackget add "<path with spaces>\Vendor.Pack.1.0.0.pack" with quotes works. The problem was tracked as a product bug of the Pack Installer; meanwhile install from a path without spaces or from the command line.

## Source

Resolution: workaround

Versions: MDK 5.39

From [Open-CMSIS-Pack/devtools #1242](https://github.com/Open-CMSIS-Pack/devtools/issues/1242), summarized in own words; confidence high, not reviewed yet.
