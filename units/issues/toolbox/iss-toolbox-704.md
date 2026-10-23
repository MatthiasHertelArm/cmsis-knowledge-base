---
id: "iss-toolbox-704"
type: "troubleshooting"
domain: "project"
title: "cbuild: cbuild --rebuild --active cleans contexts outside the active target set"
summary: "With --rebuild, cbuild cleaned every context of the project instead of only the contexts selected by the active target set, so outputs of another target type that the active target consumes as external inputs (such as a secure HEX …"
status: "draft"
tool: "cbuild"
symptoms: ["ninja: error: '<project>/out/CM33_s/AVH/Debug/CM33_s_CMSE_Lib.o', needed by '<project>/out/CM33_ns/AVH-NS-only/Debug/CM33_ns.elf', missing and no known rule to make it"]
symptom_regex: "ninja:\\s+error:\\s+'.*?',\\s+needed\\s+by\\s+'.*?',\\s+missing\\s+and\\s+no\\s+known\\s+rule\\s+to\\s+make\\s+it"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/704"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/704"
resolution: "unresolved"
versions: "Reported with cbuild 2.14.x; fix is in cbuild PR 684 and was validated on nightly build 2026-10-09 (no released version named)."
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

With --rebuild, cbuild cleaned every context of the project instead of only the contexts selected by the active target set, so outputs of another target type that the active target consumes as external inputs (such as a secure HEX image and import library) were deleted. A separate misconfiguration in the example's target-set, which pointed one target at the wrong project-context, also made the report look like a single cause.

## Fix

Update to a cbuild build that includes the fix from cbuild PR 684, then rerun the --rebuild --active command. Check that the target-set references the intended project-context.

## Source

Resolution: unresolved

Versions: Reported with cbuild 2.14.x; fix is in cbuild PR 684 and was validated on nightly build 2026-10-09 (no released version named).

From [Open-CMSIS-Pack/cmsis-toolbox #704](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/704), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
