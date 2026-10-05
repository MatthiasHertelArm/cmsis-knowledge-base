---
id: "iss-toolbox-374"
type: "troubleshooting"
domain: "project"
title: "cbuild: armclang compiler check fails in CI: no target architecture and later permission denied"
summary: "With CMSIS-Toolbox 2.4.0 the compiler check ran armclang without a target; with 2.9.0 the target was passed but the check still failed."
status: "draft"
tool: "cbuild"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/374"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/374"
resolution: "configuration"
versions: "CMSIS-Toolbox 2.4.0 and 2.9.0; Arm Compiler 6.22.1"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild"], "toolchain": ["AC6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

With CMSIS-Toolbox 2.4.0 the compiler check ran armclang without a target; with 2.9.0 the target was passed but the check still failed. The ultimate cause was the functional-safety variant of Arm Compiler 6, which needs an MDK Professional licence, while the reporter used a community licence.

## Fix

Update the toolbox, check the setup with `cbuild list environment` and `cbuild list toolchains -v`, and use the regular Arm Compiler 6.22 instead of the FuSa variant unless an MDK Professional licence is available.

## Source

Resolution: configuration

Versions: CMSIS-Toolbox 2.4.0 and 2.9.0; Arm Compiler 6.22.1

From [Open-CMSIS-Pack/cmsis-toolbox #374](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/374), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
