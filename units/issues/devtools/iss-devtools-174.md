---
id: "iss-devtools-174"
type: "troubleshooting"
domain: "project"
title: "cbuild: ERROR M800 / R817 Toolchain not supported by project when using --toolchain on a cprj"
summary: "A cprj describes one compiler; two compiler: keys in a cproject do not produce a multi-compiler project."
status: "draft"
tool: "cbuild"
symptoms: ["*** ERROR M800:\n  RTE Model reports: Error R817: Toolchain not supported by project: GCC: gpio-toggle+STM32U585I-IOT02A.cprj"]
symptom_regex: "RTE\\s+Model\\s+reports:\\s+Error\\s+R817:\\s+Toolchain\\s+not\\s+supported\\s+by\\s+project:\\s+GCC:\\s+gpio\\-toggle\\+STM32U585I\\-IOT02A\\.cprj"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/174"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/174"
resolution: "user-error"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cbuild", "csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`*** ERROR M800:
  RTE Model reports: Error R817: Toolchain not supported by project: GCC: gpio-toggle+STM32U585I-IOT02A.cprj`

## Cause

A cprj describes one compiler; two compiler: keys in a cproject do not produce a multi-compiler project.

## Fix

Declare one build-type per compiler (compiler: AC6, compiler: GCC) in csolution.yml so csolution generates one cprj per compiler.

## Source

Resolution: user-error

From [Open-CMSIS-Pack/devtools #174](https://github.com/Open-CMSIS-Pack/devtools/issues/174), summarized in own words; confidence high, checked against the thread, not reviewed yet.
