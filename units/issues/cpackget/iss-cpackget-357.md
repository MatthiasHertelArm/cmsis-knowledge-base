---
id: "iss-cpackget-357"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add of a newly published pack: 'pack version not found in the pdsc file'"
summary: "The local .Web/index.pidx and pdsc are older than the publication of that pack version, so the requested release is not listed yet."
status: "draft"
tool: "cpackget"
symptoms: ["E: pack version not found in the pdsc file"]
symptom_regex: "E:\\s+pack\\s+version\\s+not\\s+found\\s+in\\s+the\\s+pdsc\\s+file"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/357"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/357"
resolution: "fixed-in-release"
versions: "cpackget 2.1.4"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: pack version not found in the pdsc file`

## Cause

The local .Web/index.pidx and pdsc are older than the publication of that pack version, so the requested release is not listed yet.

## Fix

Run cpackget update-index and repeat. From the CMSIS-Toolbox nightly of 2024-12-09 cpackget add refreshes an outdated index and downloads the missing pdsc itself.

## Source

Resolution: fixed-in-release

Versions: cpackget 2.1.4

From [Open-CMSIS-Pack/cpackget #357](https://github.com/Open-CMSIS-Pack/cpackget/issues/357), summarized in own words; confidence high, not reviewed yet.
