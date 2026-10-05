---
id: "iss-devtools-1451"
type: "troubleshooting"
domain: "project"
title: "cbuild: Linker error for symbol defined twice when two components reference the same source file"
summary: "Two components of a pack list the same source module."
status: "draft"
tool: "cbuild"
symptoms: ["Error: L6200E: Symbol func multiply defined (by test.o and test.o)."]
symptom_regex: "L6200E:\\s+Symbol\\s+func\\s+multiply\\s+defined\\s+\\(by\\s+test\\.o\\s+and\\s+test\\.o\\)\\."
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1451"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1451"
resolution: "workaround"
versions: "2.3 to 2.5"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild", "csolution"], "toolchain": ["AC6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Error: L6200E: Symbol func multiply defined (by test.o and test.o).`

## Cause

Two components of a pack list the same source module. The modular CMake backend compiles it once per component, so the linker sees duplicate symbols; the older RteModel silently overwrote duplicates and hid this.

## Fix

Make only one component of the pack reference the file. Newer toolboxes report the duplicates in csolution and then hide the duplicate from later components (see the 2.5.0 duplicate-source error).

## Source

Resolution: workaround

Versions: 2.3 to 2.5

From [Open-CMSIS-Pack/devtools #1451](https://github.com/Open-CMSIS-Pack/devtools/issues/1451), summarized in own words; confidence medium, not reviewed yet.
