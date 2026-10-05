---
id: "iss-toolbox-450"
type: "troubleshooting"
domain: "project"
title: "cbuild: Legacy armasm sources produce unused-argument warnings for -MD/-MT/-MF"
summary: "Dependency-tracking flags added for all assembler files are not understood by the legacy armasm path."
status: "draft"
tool: "cbuild"
symptoms: ["armclang: warning: argument unused during compilation: '-MD' |  '-MT' | '-MF' [-Wunused-command-line-argument]"]
symptom_regex: "armclang:\\s+warning:\\s+argument\\s+unused\\s+during\\s+compilation:\\s+'.*?'\\s+\\|\\s+'.*?'\\s+\\|\\s+'.*?'\\s+\\[\\-Wunused\\-command\\-line\\-argument\\]"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/450"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/450"
resolution: "workaround"
confidence: "low"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cbuild"], "toolchain": ["AC6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`armclang: warning: argument unused during compilation: '-MD' |  '-MT' | '-MF' [-Wunused-command-line-argument]`

## Cause

Dependency-tracking flags added for all assembler files are not understood by the legacy armasm path.

## Fix

Harmless. No fix planned; migrate such files to GNU assembler syntax or the armclang integrated assembler.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/cmsis-toolbox #450](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/450), summarized in own words; confidence low, checked against the thread, not reviewed yet.
