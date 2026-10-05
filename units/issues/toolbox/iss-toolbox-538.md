---
id: "iss-toolbox-538"
type: "troubleshooting"
domain: "project"
title: "cbuild: Whole AC6 map file is printed in the build terminal with CMake 4"
summary: "A bare --map linker option in cdefault.yml makes armlink print the map to stdout."
status: "draft"
tool: "cbuild"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/538"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/538"
resolution: "configuration"
versions: "CMake 4.2.1 vs 3.x"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cbuild"], "toolchain": ["AC6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

A bare --map linker option in cdefault.yml makes armlink print the map to stdout. CMake 3 silently added a --list file option, CMake 4 does not.

## Fix

Remove --map from misc and request the map through output: type: [map] in the *.cproject.yml. The output node is not allowed in *.csolution.yml.

## Source

Resolution: configuration

Versions: CMake 4.2.1 vs 3.x

From [Open-CMSIS-Pack/cmsis-toolbox #538](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/538), summarized in own words; confidence high, checked against the thread, not reviewed yet.
