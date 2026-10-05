---
id: "iss-devtools-2139"
type: "troubleshooting"
domain: "project"
title: "csolution: cbuild-run.yml output list wrong for dual-core; AC6 .bin is a directory"
summary: "With armlink/fromelf, converting an image with several load regions to --bin creates a directory instead of a single file, so the expected .bin file seems missing."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2139"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2139"
resolution: "fixed-in-release"
versions: "2.10"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"], "toolchain": ["AC6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

With armlink/fromelf, converting an image with several load regions to --bin creates a directory instead of a single file, so the expected .bin file seems missing. Also, load: image+symbols from a project-context was applied to hex and bin outputs too.

## Fix

Fixed in toolbox builds after 2.10: project-context load: now applies only to the generated ELF, and the type: node is no longer allowed there. For AC6 the image still comes from the hex file when one is generated, with symbols from the AXF.

## Source

Resolution: fixed-in-release

Versions: 2.10

From [Open-CMSIS-Pack/devtools #2139](https://github.com/Open-CMSIS-Pack/devtools/issues/2139), summarized in own words; confidence medium, not reviewed yet.
