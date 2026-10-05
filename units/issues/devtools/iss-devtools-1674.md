---
id: "iss-devtools-1674"
type: "troubleshooting"
domain: "project"
title: "csolution: --toolchain GCC conflicts with layer that fixes compiler AC6"
summary: "For projects with layers, the compiler given with --toolchain was not applied consistently: the layer still set AC6 afterwards and the redefinition was rejected."
status: "draft"
tool: "csolution"
symptoms: ["warning csolution: redefinition from 'AC6' into 'GCC'", "error csolution: redefinition from 'GCC' into 'AC6' is not allowed"]
symptom_regex: "redefinition\\s+from\\s+'.*?'\\s+into\\s+'.*?'"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1674"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1674"
resolution: "fixed-in-release"
versions: "2.5.0"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution", "cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`warning csolution: redefinition from 'AC6' into 'GCC'`
`error csolution: redefinition from 'GCC' into 'AC6' is not allowed`

## Cause

For projects with layers, the compiler given with --toolchain was not applied consistently: the layer still set AC6 afterwards and the redefinition was rejected.

## Fix

Fixed in a toolbox release after 2.5.0 (internal release at the time). Update, or remove compiler: from the layer.

## Source

Resolution: fixed-in-release

Versions: 2.5.0

From [Open-CMSIS-Pack/devtools #1674](https://github.com/Open-CMSIS-Pack/devtools/issues/1674), summarized in own words; confidence medium, not reviewed yet.
