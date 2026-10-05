---
id: "iss-toolbox-338"
type: "troubleshooting"
domain: "project"
title: "cbuild: LLVM embedded 20.1.0 link fails with duplicate symbol _start"
summary: "The Clang 20 runtime already links crt0 itself, so the extra -lcrt0 in the default linker options defined the start symbols twice."
status: "draft"
tool: "cbuild"
symptoms: ["ld.lld: error: duplicate symbol: _start"]
symptom_regex: "ld\\.lld:\\s+error:\\s+duplicate\\s+symbol:\\s+_start"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/338"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/338"
resolution: "fixed-in-release"
versions: "CLANG 20.1.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild"], "toolchain": ["CLANG"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ld.lld: error: duplicate symbol: _start`

## Cause

The Clang 20 runtime already links crt0 itself, so the extra -lcrt0 in the default linker options defined the start symbols twice.

## Fix

Remove -lcrt0 from the Clang linker options in cdefault.yml, or use a toolbox nightly after 6 May 2025 (devtools PR 2066).

## Source

Resolution: fixed-in-release

Versions: CLANG 20.1.0

From [Open-CMSIS-Pack/cmsis-toolbox #338](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/338), summarized in own words; confidence high, not reviewed yet.
