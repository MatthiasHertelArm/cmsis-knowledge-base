---
id: "iss-toolbox-469"
type: "troubleshooting"
domain: "project"
title: "csolution: Missing .cmsis/*.dbgconf aborts build with an error"
summary: "csolution convert without RTE update treated a missing dbgconf like a missing component config and failed, although neither the build nor the debug session needs the file (defaults come from debug-vars)."
status: "draft"
tool: "csolution"
symptoms: ["error csolution: file '.../.cmsis/project+target.dbgconf' not found; use --update-rte"]
symptom_regex: "file\\s+'.*?'\\s+not\\s+found;\\s+use\\s+\\-\\-update\\-rte"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/469"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/469"
resolution: "fixed-in-release"
versions: "error in 2.12.0; warning in later nightlies"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: file '.../.cmsis/project+target.dbgconf' not found; use --update-rte`

## Cause

csolution convert without RTE update treated a missing dbgconf like a missing component config and failed, although neither the build nor the debug session needs the file (defaults come from debug-vars).

## Fix

Run once with --update-rte to copy the file. Newer toolbox builds (nightly after 2.12.0) only warn and continue.

## Source

Resolution: fixed-in-release

Versions: error in 2.12.0; warning in later nightlies

From [Open-CMSIS-Pack/cmsis-toolbox #469](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/469), summarized in own words; confidence high, not reviewed yet.
