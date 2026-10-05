---
id: "iss-devtools-1646"
type: "troubleshooting"
domain: "project"
title: "csolution: csolution convert aborts when no toolchain environment variable is registered"
summary: "2.5.0 enforced a registered toolchain even for csolution convert, which before did not need one."
status: "draft"
tool: "csolution"
symptoms: ["error csolution: cmake configuration file and compiler registration environment variable missing, format: GCC_TOOLCHAIN_<major>_<minor>_<patch>"]
symptom_regex: "cmake\\s+configuration\\s+file\\s+and\\s+compiler\\s+registration\\s+environment\\s+variable\\s+missing,\\s+format:\\s+GCC_TOOLCHAIN_<major>_<minor>_<patch>"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1646"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1646"
resolution: "fixed-in-release"
versions: "2.5.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"], "toolchain": ["GCC"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: cmake configuration file and compiler registration environment variable missing, format: GCC_TOOLCHAIN_<major>_<minor>_<patch>`

## Cause

2.5.0 enforced a registered toolchain even for csolution convert, which before did not need one.

## Fix

Fixed in a later 2.5.x build; update. Otherwise register a toolchain via the GCC_TOOLCHAIN_<major>_<minor>_<patch> environment variable.

## Source

Resolution: fixed-in-release

Versions: 2.5.0

From [Open-CMSIS-Pack/devtools #1646](https://github.com/Open-CMSIS-Pack/devtools/issues/1646), summarized in own words; confidence high, not reviewed yet.
