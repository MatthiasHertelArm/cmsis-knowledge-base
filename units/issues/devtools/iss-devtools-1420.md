---
id: "iss-devtools-1420"
type: "troubleshooting"
domain: "project"
title: "csolution: Redefinition of optimize level from project and solution is rejected"
summary: "Translation controls such as optimize may only be set once across project, solution, target-type and build-type; redefining them is deliberately an error, regardless of order."
status: "draft"
tool: "csolution"
symptoms: ["error csolution: redefinition from 'balanced' into 'none' is not allowed"]
symptom_regex: "redefinition\\s+from\\s+'.*?'\\s+into\\s+'.*?'\\s+is\\s+not\\s+allowed"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1420"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1420"
resolution: "not-a-bug"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: redefinition from 'balanced' into 'none' is not allowed`

## Cause

Translation controls such as optimize may only be set once across project, solution, target-type and build-type; redefining them is deliberately an error, regardless of order.

## Fix

Set optimize: at only one level, for example only in the build-type of the solution.

## Source

Resolution: not-a-bug

From [Open-CMSIS-Pack/devtools #1420](https://github.com/Open-CMSIS-Pack/devtools/issues/1420), summarized in own words; confidence high, not reviewed yet.
