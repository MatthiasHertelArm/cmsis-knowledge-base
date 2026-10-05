---
id: "iss-devtools-1451"
type: "troubleshooting"
domain: "project"
title: "cbuild: Linker error for symbol defined twice when two components reference the same source file"
summary: "Two components of the pack list the same source file. cbuild2cmake compiles it for each component and the linker reports duplicate symbols, while the RteModel and cbuildgen silently dropped the duplicate and hid the problem."
status: "draft"
tool: "cbuild"
symptoms: ["Error: L6200E: Symbol func multiply defined (by test.o and test.o)."]
symptom_regex: "L6200E:\\s+Symbol\\s+func\\s+multiply\\s+defined\\s+\\(by\\s+test\\.o\\s+and\\s+test\\.o\\)\\."
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1451"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1451"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild", "csolution"], "toolchain": ["AC6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Error: L6200E: Symbol func multiply defined (by test.o and test.o).`

## Cause

Two components of the pack list the same source file. cbuild2cmake compiles it for each component and the linker reports duplicate symbols, while the RteModel and cbuildgen silently dropped the duplicate and hid the problem.

## Fix

Treat it as a component design error in the pack and let only one selected component contribute the file, for example through a common component the others depend on; packchk is to detect such packs (devtools #1499).

## Source

Resolution: workaround

From [Open-CMSIS-Pack/devtools #1451](https://github.com/Open-CMSIS-Pack/devtools/issues/1451), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
