---
id: "iss-cpackget-307"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add: 'zip: not a valid zip file' for a damaged downloaded pack"
summary: "The downloaded pack file was corrupted; installing the same damaged file again reproduces the error."
status: "draft"
tool: "cpackget"
symptoms: ["E: Can't decompress \"<cache>/arm/packs/.Download/AlifSemiconductor.Ensemble.1.1.3.pack\": zip: not a valid zip file", "E: fail to decompress file"]
symptom_regex: "E:\\s+Can't\\s+decompress\\s+\".*?\":\\s+zip:\\s+not\\s+a\\s+valid\\s+zip\\s+file"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/307"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/307"
resolution: "workaround"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: Can't decompress "<cache>/arm/packs/.Download/AlifSemiconductor.Ensemble.1.1.3.pack": zip: not a valid zip file`
`E: fail to decompress file`

## Cause

The downloaded pack file was corrupted; installing the same damaged file again reproduces the error.

## Fix

Delete the file (cpackget rm --purge for the pack or remove it from .Download) and download it again.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/cpackget #307](https://github.com/Open-CMSIS-Pack/cpackget/issues/307), summarized in own words; confidence low, not reviewed yet.
