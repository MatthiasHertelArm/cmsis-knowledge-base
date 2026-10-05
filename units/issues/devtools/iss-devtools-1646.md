---
id: "iss-devtools-1646"
type: "troubleshooting"
domain: "project"
title: "csolution: csolution convert aborts when no toolchain environment variable is registered"
summary: "csolution 2.5.0 enforced a registered toolchain (GCC_TOOLCHAIN_<major>_<minor>_<patch> environment variable) even for csolution convert, which before did not need one; the agreed behaviour is to check it only when cbuild invokes the toolchain."
status: "draft"
tool: "csolution"
symptoms: ["error csolution: cmake configuration file and compiler registration environment variable missing, format: GCC_TOOLCHAIN_<major>_<minor>_<patch>"]
symptom_regex: "cmake\\s+configuration\\s+file\\s+and\\s+compiler\\s+registration\\s+environment\\s+variable\\s+missing,\\s+format:\\s+GCC_TOOLCHAIN_<major>_<minor>_<patch>"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1646"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1646"
resolution: "fixed-in-release"
versions: "2.5.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"], "toolchain": ["GCC"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: cmake configuration file and compiler registration environment variable missing, format: GCC_TOOLCHAIN_<major>_<minor>_<patch>`

## Cause

csolution 2.5.0 enforced a registered toolchain (GCC_TOOLCHAIN_<major>_<minor>_<patch> environment variable) even for csolution convert, which before did not need one; the agreed behaviour is to check it only when cbuild invokes the toolchain.

## Fix

Fixed (confirmed in the thread, no version named); update csolution. Otherwise register the toolchain via the GCC_TOOLCHAIN_<major>_<minor>_<patch> environment variable.

## Source

Resolution: fixed-in-release

Versions: 2.5.0

From [Open-CMSIS-Pack/devtools #1646](https://github.com/Open-CMSIS-Pack/devtools/issues/1646), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
