---
id: "iss-devtools-914"
type: "troubleshooting"
domain: "project"
title: "cbuild: GCC link fails with undefined references between static libraries because of link order"
summary: "GNU ld scans an archive only once in command-line order, so libraries that reference each other circularly (many small component libraries) fail to link. cbuild passed the libraries without a rescan group."
status: "draft"
tool: "cbuild"
symptoms: ["undefined reference to"]
symptom_regex: "undefined\\s+reference\\s+to"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/914"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/914"
resolution: "fixed-in-release"
versions: "Reported with 1.7"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild"], "toolchain": ["GCC"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`undefined reference to`

## Cause

GNU ld scans an archive only once in command-line order, so libraries that reference each other circularly (many small component libraries) fail to link. cbuild passed the libraries without a rescan group.

## Fix

The GCC toolchain cmake file was changed to wrap the library list in -Wl,--start-group ... -Wl,--end-group (set(LIB_FILES -Wl,--start-group ${LIB_FILES} -Wl,--end-group)). The CMake LINK_GROUP genex is not usable because it needs CMake 3.24. Fixed in a CMSIS-Toolbox release after 1.7; as a local patch edit GCC.<version>.cmake.

## Source

Resolution: fixed-in-release

Versions: Reported with 1.7

From [Open-CMSIS-Pack/devtools #914](https://github.com/Open-CMSIS-Pack/devtools/issues/914), summarized in own words; confidence high, not reviewed yet.
