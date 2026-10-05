---
id: "iss-toolbox-399"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget rejects pack files whose version is not semantic (e.g. NAMEv0.051)"
summary: "cpackget validates pack names and requires numeric major.minor.patch versions in file name and pdsc release tag."
status: "draft"
tool: "cpackget"
symptoms: ["E: bad pack name: it must be either a PackID:  packVendor::Pack[@version|@~version|@^version|@>=version] or a local Pack file: <path>/Vendor.Pack.version.pack or a local Pack Description file: <path>/"]
symptom_regex: "E:\\s+bad\\s+pack\\s+name:\\s+it\\s+must\\s+be\\s+either\\s+a\\s+PackID:\\s+packVendor::Pack\\[@version\\|@\\~version\\|@\\^version\\|@>=version\\]\\s+or\\s+a\\s+local\\s+Pack\\s+file:\\s+<path>/Vendor\\.Pack\\.version\\.pack\\s+or\\s+a\\s+local\\s+Pack\\s+Description\\s+file:\\s+<path>/"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/399"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/399"
resolution: "workaround"
versions: "cpackget 2.1.8"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: bad pack name: it must be either a PackID:  packVendor::Pack[@version|@~version|@^version|@>=version] or a local Pack file: <path>/Vendor.Pack.version.pack or a local Pack Description file: <path>/`

## Cause

cpackget validates pack names and requires numeric major.minor.patch versions in file name and pdsc release tag. Legacy packs with other version strings fail.

## Fix

Install such packs with the Keil_v5/UV4/packunzip tool instead.

## Source

Resolution: workaround

Versions: cpackget 2.1.8

From [Open-CMSIS-Pack/cmsis-toolbox #399](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/399), summarized in own words; confidence high, checked against the thread, not reviewed yet.
