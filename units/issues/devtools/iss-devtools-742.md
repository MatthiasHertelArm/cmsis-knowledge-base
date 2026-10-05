---
id: "iss-devtools-742"
type: "troubleshooting"
domain: "project"
title: "csolution: Generated code ends up in ./generated instead of RTE/Device/<device> for CubeMX generator"
summary: "csolution used its own generator directory even when the pack's <generator> element prescribes workingDir and gpdsc location (for example $PRTE/Device), so MDK/Eclipse and csolution disagreed."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/742"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/742"
resolution: "fixed-in-release"
versions: "fixed in 1.5.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

csolution used its own generator directory even when the pack's <generator> element prescribes workingDir and gpdsc location (for example $PRTE/Device), so MDK/Eclipse and csolution disagreed.

## Fix

Fixed in CMSIS-Toolbox 1.5.0: when the pack's generator element sets workingDir or gpdsc with a fixed location, the user cannot override the directory in csolution.yml.

## Source

Resolution: fixed-in-release

Versions: fixed in 1.5.0

From [Open-CMSIS-Pack/devtools #742](https://github.com/Open-CMSIS-Pack/devtools/issues/742), summarized in own words; confidence high, not reviewed yet.
