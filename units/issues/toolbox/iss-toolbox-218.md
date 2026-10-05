---
id: "iss-toolbox-218"
type: "troubleshooting"
domain: "project"
title: "cbuild: No program size printed at the end of a GCC build"
summary: "The size line comes from linker options in cdefault.yml (armlink summary), and a local cdefault without them prints nothing; GCC needs its own option."
status: "draft"
tool: "cbuild"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/218"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/218"
resolution: "configuration"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild"], "toolchain": ["GCC"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The size line comes from linker options in cdefault.yml (armlink summary), and a local cdefault without them prints nothing; GCC needs its own option.

## Fix

Use the cdefault.yml shipped with toolbox 2.7 or newer, which adds -Wl,-print-memory-usage for GCC, or add that option yourself.

## Source

Resolution: configuration

From [Open-CMSIS-Pack/cmsis-toolbox #218](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/218), summarized in own words; confidence medium, not reviewed yet.
