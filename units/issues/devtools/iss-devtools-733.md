---
id: "iss-devtools-733"
type: "troubleshooting"
domain: "project"
title: "cbuild: IAR assembler error because the same define is passed globally and per file"
summary: "Defines are additive over the hierarchy, so a define listed at project and at file level appears twice on the command line, which the IAR assembler rejects."
status: "draft"
tool: "cbuild"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/733"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/733"
resolution: "fixed-in-release"
versions: "fixed in 1.5.0"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild"], "toolchain": ["IAR"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Defines are additive over the hierarchy, so a define listed at project and at file level appears twice on the command line, which the IAR assembler rejects.

## Fix

csolution removes duplicate defines when generating the cprj (CMSIS-Toolbox 1.5.0); until then list a define only once.

## Source

Resolution: fixed-in-release

Versions: fixed in 1.5.0

From [Open-CMSIS-Pack/devtools #733](https://github.com/Open-CMSIS-Pack/devtools/issues/733), summarized in own words; confidence medium, not reviewed yet.
