---
id: "iss-devtools-1314"
type: "troubleshooting"
domain: "project"
title: "cbuild: Macros from Pre_Include_Global.h are not visible to assembly files"
summary: "Pre_Include_Global.h is a C/C++ pre-include that the build adds only to C/C++ compilation."
status: "draft"
tool: "cbuild"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1314"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1314"
resolution: "not-a-bug"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Pre_Include_Global.h is a C/C++ pre-include that the build adds only to C/C++ compilation. Assembly files are not preprocessed with it; maintainers chose to handle C/C++ and assembly includes separately, so adding assembly support was declined.

## Fix

The thread gives no workaround for assembly macros. It only notes that the add-path-asm node was created to separate assembly include paths from add-path.

## Source

Resolution: not-a-bug

From [Open-CMSIS-Pack/devtools #1314](https://github.com/Open-CMSIS-Pack/devtools/issues/1314), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
