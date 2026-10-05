---
id: "iss-devtools-2139"
type: "troubleshooting"
domain: "project"
title: "csolution: cbuild-run.yml output list wrong for dual-core; AC6 .bin is a directory"
summary: "With fromelf, converting an image with several load regions to --bin creates a directory instead of a single file, so the expected .bin file seems missing."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2139"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2139"
resolution: "fixed-in-release"
versions: "CMSIS-Toolbox 2.10"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"], "toolchain": ["AC6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

With fromelf, converting an image with several load regions to --bin creates a directory instead of a single file, so the expected .bin file seems missing. A load: given for a project-context without type: was applied to all generated types, including hex and bin.

## Fix

PR #2171 makes the project-context load: apply only to the generated ELF and no longer allows type: there. Per the agreed rule, with AC6 and a generated HEX the image should come from the HEX and the symbols from the AXF; the reporter found an explicit load: image+symbols still did not follow it, and the thread ends there.

## Source

Resolution: fixed-in-release

Versions: CMSIS-Toolbox 2.10

From [Open-CMSIS-Pack/devtools #2139](https://github.com/Open-CMSIS-Pack/devtools/issues/2139), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
