---
id: "iss-devtools-312"
type: "troubleshooting"
domain: "project"
title: "cbuild: AC6 assembler error: unexpected token at start of statement for an ST startup .s file"
summary: "The startup file is written in armasm syntax (; comments) but armclang assembles it as GNU assembler by default."
status: "draft"
tool: "cbuild"
symptoms: ["error: unexpected token at start of statement"]
symptom_regex: "unexpected\\s+token\\s+at\\s+start\\s+of\\s+statement"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/312"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/312"
resolution: "configuration"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild"], "toolchain": ["AC6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error: unexpected token at start of statement`

## Cause

The startup file is written in armasm syntax (; comments) but armclang assembles it as GNU assembler by default.

## Fix

Add misc: - ASM: - -masm=auto to the build type (written as a single option with = and no spaces).

## Source

Resolution: configuration

From [Open-CMSIS-Pack/devtools #312](https://github.com/Open-CMSIS-Pack/devtools/issues/312), summarized in own words; confidence high, not reviewed yet.
