---
id: "iss-toolbox-704"
type: "troubleshooting"
domain: "project"
title: "cbuild: --rebuild with --active also cleans outputs of unrelated target types"
summary: "With --rebuild, cbuild cleaned every context of the project rather than only the contexts selected by the active target set."
status: "draft"
tool: "cbuild"
symptoms: ["ninja: error: '<project>/out/CM33_s/AVH/Debug/CM33_s_CMSE_Lib.o', needed by '<project>/out/CM33_ns/AVH-NS-only/Debug/CM33_ns.axf', missing and no known rule to make it"]
symptom_regex: "ninja:\\s+error:\\s+'.*?',\\s+needed\\s+by\\s+'.*?',\\s+missing\\s+and\\s+no\\s+known\\s+rule\\s+to\\s+make\\s+it"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/704"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/704"
resolution: "unresolved"
versions: "Reported with CMSIS-Toolbox cbuild 2.14.x; fix validated on nightly build 2026-10-09 (PR 684)."
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild"], "core": ["Cortex-M33"], "toolchain": ["AC6", "GCC"], "compiler": ["AC6", "GCC"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ninja: error: '<project>/out/CM33_s/AVH/Debug/CM33_s_CMSE_Lib.o', needed by '<project>/out/CM33_ns/AVH-NS-only/Debug/CM33_ns.axf', missing and no known rule to make it`

## Cause

With --rebuild, cbuild cleaned every context of the project rather than only the contexts selected by the active target set. Output directories of another target type that the active target consumes as external inputs were therefore deleted, so the build failed. A separate misconfiguration in the example project (a target-set pointing at the wrong project-context) caused a related wrong selection in the original CI run.

## Fix

Upgrade to a cbuild build that includes the fix from PR 684, which the thread gives as the fix for this issue. Nightly build 2026-10-09 was validated with a normal --active AVH-NS-only@Debug build; the thread does not confirm the --rebuild case. Also check that each target-set references the project-context matching its set name.

## Source

Resolution: unresolved

Versions: Reported with CMSIS-Toolbox cbuild 2.14.x; fix validated on nightly build 2026-10-09 (PR 684).

From [Open-CMSIS-Pack/cmsis-toolbox #704](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/704), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
