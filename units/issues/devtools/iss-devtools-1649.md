---
id: "iss-devtools-1649"
type: "troubleshooting"
domain: "project"
title: "cbuild: cbuild prints 'bad pack name' from cpackget with --context-set"
summary: "A regression in a 2.5.0 pre-release: csolution list packs output with --context-set began with an info line about cbuild-set.yml, which cbuild parsed as a pack name."
status: "draft"
tool: "cbuild"
symptoms: ["E: bad pack name: it should be one of the following formats: Vendor.Pack, Vendor.Pack.x.y.z, Vendor.Pack.x.y.z.pack, or Vendor.Pack.pdsc"]
symptom_regex: "E:\\s+bad\\s+pack\\s+name:\\s+it\\s+should\\s+be\\s+one\\s+of\\s+the\\s+following\\s+formats:\\s+Vendor\\.Pack,\\s+Vendor\\.Pack\\.x\\.y\\.z,\\s+Vendor\\.Pack\\.x\\.y\\.z\\.pack,\\s+or\\s+Vendor\\.Pack\\.pdsc"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1649"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1649"
resolution: "fixed-in-release"
versions: "2.5.0-devint5"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild", "cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: bad pack name: it should be one of the following formats: Vendor.Pack, Vendor.Pack.x.y.z, Vendor.Pack.x.y.z.pack, or Vendor.Pack.pdsc`

## Cause

A regression in a 2.5.0 pre-release: csolution list packs output with --context-set began with an info line about cbuild-set.yml, which cbuild parsed as a pack name.

## Fix

Fixed before the 2.5.0 release; use the final 2.5.0 or later.

## Source

Resolution: fixed-in-release

Versions: 2.5.0-devint5

From [Open-CMSIS-Pack/devtools #1649](https://github.com/Open-CMSIS-Pack/devtools/issues/1649), summarized in own words; confidence high, not reviewed yet.
