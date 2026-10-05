---
id: "iss-devtools-1649"
type: "troubleshooting"
domain: "project"
title: "cbuild: cbuild prints 'bad pack name' from cpackget with --context-set"
summary: "A regression in the 2.5.0 pre-release (2.5.0-devint5): with --context-set, the output of csolution list packs began with an info line about cbuild-set.yml, which cbuild passed to cpackget as a pack name."
status: "draft"
tool: "cbuild"
symptoms: ["E: bad pack name: it should be one of the following formats: Vendor.Pack, Vendor.Pack.x.y.z, Vendor.Pack.x.y.z.pack, or Vendor.Pack.pdsc"]
symptom_regex: "E:\\s+bad\\s+pack\\s+name:\\s+it\\s+should\\s+be\\s+one\\s+of\\s+the\\s+following\\s+formats:\\s+Vendor\\.Pack,\\s+Vendor\\.Pack\\.x\\.y\\.z,\\s+Vendor\\.Pack\\.x\\.y\\.z\\.pack,\\s+or\\s+Vendor\\.Pack\\.pdsc"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1649"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1649"
resolution: "fixed-in-release"
versions: "CMSIS-Toolbox 2.5.0-devint5"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild", "cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: bad pack name: it should be one of the following formats: Vendor.Pack, Vendor.Pack.x.y.z, Vendor.Pack.x.y.z.pack, or Vendor.Pack.pdsc`

## Cause

A regression in the 2.5.0 pre-release (2.5.0-devint5): with --context-set, the output of csolution list packs began with an info line about cbuild-set.yml, which cbuild passed to cpackget as a pack name.

## Fix

Fixed in a cbuild PR, validated on Windows; the maintainers aimed to ship it before the 2.5.0 release.

## Source

Resolution: fixed-in-release

Versions: CMSIS-Toolbox 2.5.0-devint5

From [Open-CMSIS-Pack/devtools #1649](https://github.com/Open-CMSIS-Pack/devtools/issues/1649), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
