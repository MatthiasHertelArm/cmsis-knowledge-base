---
id: "iss-sol-360"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Layer selection omits the empty variable (Shield-Layer: ) for unused layers"
summary: "Layer variables of the cproject must be set, with an empty string when a layer is unused; the extension stopped writing the empty value, so the build failed and the dialog reopened."
status: "draft"
tool: "cmsis-solution"
symptoms: ["error csolution: undefined variables in Demo.csolution.yml:"]
symptom_regex: "undefined\\s+variables\\s+in\\s+Demo\\.csolution\\.yml:"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/360"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/360"
resolution: "fixed-in-release"
versions: "1.68.0 affected"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: undefined variables in Demo.csolution.yml:`

## Cause

Layer variables of the cproject must be set, with an empty string when a layer is unused; the extension stopped writing the empty value, so the build failed and the dialog reopened.

## Fix

Use CMSIS Solution nightly of 2026-07-13 or later; as a workaround add the variable with an empty string value to the csolution.yml.

## Source

Resolution: fixed-in-release

Versions: 1.68.0 affected

From [Open-CMSIS-Pack/vscode-cmsis-solution #360](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/360), summarized in own words; confidence high, not reviewed yet.
