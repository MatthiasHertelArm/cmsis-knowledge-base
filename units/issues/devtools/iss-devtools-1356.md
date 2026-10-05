---
id: "iss-devtools-1356"
type: "troubleshooting"
domain: "project"
title: "csolution: Warning that a required pack is not loaded or not specified"
summary: "A pack in use (for example a BSP) lists other packs under requirements in its pdsc; csolution warns when those are not part of the pack selection, as a hint where an unresolved component or dependency could come from."
status: "draft"
tool: "csolution"
symptoms: ["warning csolution: context 'Project.Debug+SSE-310-MPS3_FVP': required pack 'ARM::CMSIS-Compiler@2.0.0' is not loaded"]
symptom_regex: "context\\s+'.*?':\\s+required\\s+pack\\s+'.*?'\\s+is\\s+not\\s+loaded"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1356"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1356"
resolution: "not-a-bug"
versions: "2.2.1"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`warning csolution: context 'Project.Debug+SSE-310-MPS3_FVP': required pack 'ARM::CMSIS-Compiler@2.0.0' is not loaded`

## Cause

A pack in use (for example a BSP) lists other packs under requirements in its pdsc; csolution warns when those are not part of the pack selection, as a hint where an unresolved component or dependency could come from.

## Fix

Informational. Add the named pack to packs: if a component or dependency is not resolved; otherwise the warning can be ignored. The text was reworded to name the pack that requires it.

## Source

Resolution: not-a-bug

Versions: 2.2.1

From [Open-CMSIS-Pack/devtools #1356](https://github.com/Open-CMSIS-Pack/devtools/issues/1356), summarized in own words; confidence medium, not reviewed yet.
