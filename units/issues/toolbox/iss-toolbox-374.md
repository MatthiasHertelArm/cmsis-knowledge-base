---
id: "iss-toolbox-374"
type: "troubleshooting"
domain: "project"
title: "cbuild: armclang compiler check fails in CI: no target architecture and later permission denied"
summary: "Old toolbox versions did not pass a target to the compiler test, and the compiler registration pointed at the wrong location."
status: "draft"
tool: "cbuild"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/374"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/374"
resolution: "configuration"
versions: "toolbox 2.4.0 initially"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild"], "toolchain": ["AC6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Old toolbox versions did not pass a target to the compiler test, and the compiler registration pointed at the wrong location. The ultimate cause was a functional-safety armclang variant that did not run without a MDK Professional licence.

## Fix

Update the toolbox, register the compiler with the toolchain environment variable pointing to the bin folder, verify with cbuild list environment and cbuild list toolchains -v, and use the regular armclang if the FuSa variant lacks a licence.

## Source

Resolution: configuration

Versions: toolbox 2.4.0 initially

From [Open-CMSIS-Pack/cmsis-toolbox #374](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/374), summarized in own words; confidence medium, not reviewed yet.
