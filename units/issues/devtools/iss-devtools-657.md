---
id: "iss-devtools-657"
type: "troubleshooting"
domain: "project"
title: "csolution: Segmentation fault in csolution convert when a pack file name ends with a folder path"
summary: "A pack <file> element whose name attribute is a directory (path/) instead of path/name.ext crashed the parser, and packchk did not flag it."
status: "draft"
tool: "csolution"
symptoms: ["Segmentation fault (core dumped)"]
symptom_regex: "Segmentation\\s+fault\\s+\\(core\\s+dumped\\)"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/657"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/657"
resolution: "fixed-in-release"
versions: "Seen in 1.3.0; fixed in 1.5.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution", "packchk"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Segmentation fault (core dumped)`

## Cause

A pack <file> element whose name attribute is a directory (path/) instead of path/name.ext crashed the parser, and packchk did not flag it.

## Fix

Use proper file names in the pdsc. Fixed in packchk 1.3.98, shipped with CMSIS-Toolbox 1.5.0.

## Source

Resolution: fixed-in-release

Versions: Seen in 1.3.0; fixed in 1.5.0

From [Open-CMSIS-Pack/devtools #657](https://github.com/Open-CMSIS-Pack/devtools/issues/657), summarized in own words; confidence high, not reviewed yet.
