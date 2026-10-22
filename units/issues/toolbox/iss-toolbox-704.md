---
id: "iss-toolbox-704"
type: "troubleshooting"
domain: "project"
title: "cbuild: --rebuild with --active cleans outputs of other target types and breaks the build"
summary: "With --rebuild, cbuild cleaned every context of the active target set rather than only the contexts it selected, so outputs of the other target type (AVH) that the active target consumes as external inputs were deleted."
status: "draft"
tool: "cbuild"
symptoms: ["ninja: error: '<project>/out/CM33_s/AVH/Debug/CM33_s_CMSE_Lib.o', needed by '<project>/out/CM33_ns/AVH-NS-only/Debug/CM33_ns.elf', missing and no known rule to make it"]
symptom_regex: "ninja:\\s+error:\\s+'.*?',\\s+needed\\s+by\\s+'.*?',\\s+missing\\s+and\\s+no\\s+known\\s+rule\\s+to\\s+make\\s+it"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/704"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/704"
resolution: "unresolved"
versions: "Reported with cbuild 2.14.x using AC6 and GCC; fix linked as cbuild PR 684; validated on nightly build 2026-10-09 (AC6 only)."
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild"], "core": ["Cortex-M33"], "toolchain": ["AC6", "GCC"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ninja: error: '<project>/out/CM33_s/AVH/Debug/CM33_s_CMSE_Lib.o', needed by '<project>/out/CM33_ns/AVH-NS-only/Debug/CM33_ns.elf', missing and no known rule to make it`

## Cause

With --rebuild, cbuild cleaned every context of the active target set rather than only the contexts it selected, so outputs of the other target type (AVH) that the active target consumes as external inputs were deleted. A separate misconfiguration in the example, a target-set entry referencing the Release project-context instead of Debug, was proposed as a possible related cause in the reporter's CI.

## Fix

Update cbuild to a build that includes the fix from PR 684, which the thread links as the fix. Nightly build 2026-10-09 built the AC6 secure and non-secure contexts without the missing-file error. Also check that each target-set entry references the intended project-context (for example CM33_ns.Debug, not CM33_ns.Release).

## Source

Resolution: unresolved

Versions: Reported with cbuild 2.14.x using AC6 and GCC; fix linked as cbuild PR 684; validated on nightly build 2026-10-09 (AC6 only).

From [Open-CMSIS-Pack/cmsis-toolbox #704](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/704), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
