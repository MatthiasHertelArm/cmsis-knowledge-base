---
id: "iss-sol-330"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Switching solutions reports 'pack ... is duplicated' for solution-local packs"
summary: "Local packs of the previously loaded solution stayed in the pack cache when another solution was loaded."
status: "draft"
tool: "cmsis-solution"
symptoms: ["csolution error: component 'CMSIS:NN Lib' not found in included packs", "warning #500: pack 'ARM::CMSIS-NN@4.1.0' is duplicated:"]
symptom_regex: "csolution\\s+error:\\s+component\\s+'.*?'\\s+not\\s+found\\s+in\\s+included\\s+packs"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/330"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/330"
resolution: "fixed-in-release"
versions: "1.68.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`csolution error: component 'CMSIS:NN Lib' not found in included packs`
`warning #500: pack 'ARM::CMSIS-NN@4.1.0' is duplicated:`

## Cause

Local packs of the previously loaded solution stayed in the pack cache when another solution was loaded.

## Fix

Fixed in CMSIS Solution nightly of 2026-06-29; solution-local packs are removed on reload.

## Source

Resolution: fixed-in-release

Versions: 1.68.0

From [Open-CMSIS-Pack/vscode-cmsis-solution #330](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/330), summarized in own words; confidence high, not reviewed yet.
