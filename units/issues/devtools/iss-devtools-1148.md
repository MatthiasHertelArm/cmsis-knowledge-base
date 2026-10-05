---
id: "iss-devtools-1148"
type: "troubleshooting"
domain: "pack"
title: "svdconv: SVDConv rejects protection tag inside addressBlock"
summary: "The protection element in addressBlock is part of the SVD schema since 1.3.2, but SVDConv 3.3.46 did not know it there."
status: "draft"
tool: "svdconv"
symptoms: ["*** ERROR M201: test.svd (Line 28) \n  Tag <protection> unknown or not allowed on this level."]
symptom_regex: "test\\.svd\\s+\\(Line\\s+\\S+\\)\\s+\\\\s+Tag\\s+<protection>\\s+unknown\\s+or\\s+not\\s+allowed\\s+on\\s+this\\s+level\\."
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1148"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1148"
resolution: "fixed-in-release"
versions: "3.3.46"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["svdconv"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`*** ERROR M201: test.svd (Line 28) 
  Tag <protection> unknown or not allowed on this level.`

## Cause

The protection element in addressBlock is part of the SVD schema since 1.3.2, but SVDConv 3.3.46 did not know it there.

## Fix

Use an SVDConv release that supports the SVD 1.3.2 element (newer than 3.3.46) and make sure the file declares a matching schemaVersion.

## Source

Resolution: fixed-in-release

Versions: 3.3.46

From [Open-CMSIS-Pack/devtools #1148](https://github.com/Open-CMSIS-Pack/devtools/issues/1148), summarized in own words; confidence medium, not reviewed yet.
