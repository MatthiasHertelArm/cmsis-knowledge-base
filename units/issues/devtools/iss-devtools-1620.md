---
id: "iss-devtools-1620"
type: "troubleshooting"
domain: "project"
title: "csolution: Build fails because an optional layer variable such as Shield-Layer is undefined"
summary: "Layer variables referenced in layers: must be defined; there is no implicit skipping of an optional layer."
status: "draft"
tool: "csolution"
symptoms: ["error csolution: undefined variables in <name>.csolution.yml:\n  - $Shield-Layer$"]
symptom_regex: "undefined\\s+variables\\s+in\\s+<name>\\.csolution\\.yml:\\\\s+\\-\\s+\\$Shield\\-Layer\\$"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1620"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1620"
resolution: "configuration"
versions: "2.5.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: undefined variables in <name>.csolution.yml:
  - $Shield-Layer$`

## Cause

Layer variables referenced in layers: must be defined; there is no implicit skipping of an optional layer.

## Fix

Define the variable as an empty string in the target-type (variables: - Shield-Layer: ""); an entry with an empty layer path is ignored. Layer detection writes this into the cbuild-idx configurations from 2.6 on.

## Source

Resolution: configuration

Versions: 2.5.0

From [Open-CMSIS-Pack/devtools #1620](https://github.com/Open-CMSIS-Pack/devtools/issues/1620), summarized in own words; confidence high, not reviewed yet.
