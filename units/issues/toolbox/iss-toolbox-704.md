---
id: "iss-toolbox-704"
type: "troubleshooting"
domain: "project"
title: "cbuild: cbuild --rebuild --active removes secure outputs needed by the non-secure target"
summary: "Two separate effects."
status: "draft"
tool: "cbuild"
symptoms: ["ninja: error: '.../out/CM33_s/AVH/Debug/CM33_s_CMSE_Lib.o', needed by '.../out/CM33_ns/AVH-NS-only/Debug/CM33_ns.elf', missing and no known rule to make it"]
symptom_regex: "ninja:\\s+error:\\s+'.*?',\\s+needed\\s+by\\s+'.*?',\\s+missing\\s+and\\s+no\\s+known\\s+rule\\s+to\\s+make\\s+it"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/704"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/704"
resolution: "user-error"
versions: "CMSIS-Toolbox/cbuild 2.14.x"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild"], "toolchain": ["AC6", "GCC"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ninja: error: '.../out/CM33_s/AVH/Debug/CM33_s_CMSE_Lib.o', needed by '.../out/CM33_ns/AVH-NS-only/Debug/CM33_ns.elf', missing and no known rule to make it`

## Cause

Two separate effects. In the reported project the target-set of the non-secure-only target pointed at the Release project context while the Debug set was selected, so the wrong context was built. In addition, --rebuild with --active cleans all contexts, not only those of the selected target-set, which deletes the prebuilt secure artifacts that the non-secure image consumes.

## Fix

Make each target-set reference the project contexts of its own build type (CM33_ns.Debug in the Debug set). Building the non-secure context directly with --context does not remove the secure artifacts. The --rebuild cleaning behaviour has no fix in the thread.

## Source

Resolution: user-error

Versions: CMSIS-Toolbox/cbuild 2.14.x

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/cmsis-toolbox #704](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/704), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
