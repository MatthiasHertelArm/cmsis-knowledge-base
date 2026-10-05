---
id: "iss-toolbox-559"
type: "troubleshooting"
domain: "project"
title: "cbuild: Adding a symdefs/ROM symbol file to an AC6 project gives a format error"
summary: "Files are classified by extension."
status: "draft"
tool: "cbuild"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/559"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/559"
resolution: "configuration"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"], "toolchain": ["AC6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Files are classified by extension. A symbol file with .icf is taken as an IAR linker script, and one without a known extension is not passed to armlink as an object.

## Fix

Declare the file with category: object in the group (file: <name>, category: object) or give it the .o extension so it appears on the armlink command line.

## Source

Resolution: configuration

From [Open-CMSIS-Pack/cmsis-toolbox #559](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/559), summarized in own words; confidence high, not reviewed yet.
