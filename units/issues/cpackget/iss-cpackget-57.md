---
id: "iss-cpackget-57"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add of an older pack version fails with 'URL for the pack cannot be determined'"
summary: "In 2022 cpackget searched index.pidx for vendor, name and the requested version, but the index only lists the latest version of each pack; the pdsc should have been located by vendor and name and the version taken from its releases."
status: "draft"
tool: "cpackget"
symptoms: ["E: URL for the pack cannot be determined. Please consider updating the public index. Ex: cpackget update-index"]
symptom_regex: "E:\\s+URL\\s+for\\s+the\\s+pack\\s+cannot\\s+be\\s+determined\\.\\s+Please\\s+consider\\s+updating\\s+the\\s+public\\s+index\\.\\s+Ex:\\s+cpackget\\s+update\\-index"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/57"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/57"
resolution: "fixed-in-release"
versions: "0.4.x"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: URL for the pack cannot be determined. Please consider updating the public index. Ex: cpackget update-index`

## Cause

In 2022 cpackget searched index.pidx for vendor, name and the requested version, but the index only lists the latest version of each pack; the pdsc should have been located by vendor and name and the version taken from its releases.

## Fix

Use a cpackget release after 0.4.x (fixed 2022), or run cpackget update-index. The message itself was later corrected to name update-index.

## Source

Resolution: fixed-in-release

Versions: 0.4.x

From [Open-CMSIS-Pack/cpackget #57](https://github.com/Open-CMSIS-Pack/cpackget/issues/57), summarized in own words; confidence high, not reviewed yet.
