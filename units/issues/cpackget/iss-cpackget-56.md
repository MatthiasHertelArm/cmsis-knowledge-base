---
id: "iss-cpackget-56"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget index/update-index fails with 'Access is denied' when index.pidx is read-only"
summary: "Pack folders are kept read-only by design."
status: "draft"
tool: "cpackget"
symptoms: ["E: Can't move file \"<packs>\\.Download\\index.pidx\" to \"<packs>\\.Web\\index.pidx\": rename ... Access is denied."]
symptom_regex: "E:\\s+Can't\\s+move\\s+file\\s+\".*?\"\\s+to\\s+\".*?\":\\s+rename\\s+\\.\\.\\.\\s+Access\\s+is\\s+denied\\."
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/56"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/56"
resolution: "workaround"
versions: "2022"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: Can't move file "<packs>\.Download\index.pidx" to "<packs>\.Web\index.pidx": rename ... Access is denied.`

## Cause

Pack folders are kept read-only by design. A folder created by another tool (MDK Pack Installer) had a read-only index.pidx that cpackget could not overwrite.

## Fix

Remove the read-only attribute from the files in the pack root (or let cpackget manage the folder); later cpackget releases handle the read-only flag when replacing files.

## Source

Resolution: workaround

Versions: 2022

From [Open-CMSIS-Pack/cpackget #56](https://github.com/Open-CMSIS-Pack/cpackget/issues/56), summarized in own words; confidence medium, not reviewed yet.
