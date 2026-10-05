---
id: "iss-devtools-2603"
type: "troubleshooting"
domain: "project"
title: "csolution: Paths of a CubeMX component duplicated and wrong when a setups: node is present"
summary: "With a Device:CubeMX component plus a setups: node in the cproject.yml, csolution emitted every path twice, the second copy resolved against the wrong base directory so it escaped the project."
status: "draft"
tool: "csolution"
symptoms: ["armclang: error: no such file or directory: '@<absolute_path>/../../../Core/compiler_args.txt'"]
symptom_regex: "armclang:\\s+error:\\s+no\\s+such\\s+file\\s+or\\s+directory:\\s+'.*?'"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2603"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2603"
resolution: "fixed-in-release"
versions: "seen in 2.14.1, fixed after"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["csolution", "cbuild"], "toolchain": ["AC6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`armclang: error: no such file or directory: '@<absolute_path>/../../../Core/compiler_args.txt'`

## Cause

With a Device:CubeMX component plus a setups: node in the cproject.yml, csolution emitted every path twice, the second copy resolved against the wrong base directory so it escaped the project.

## Fix

Fixed in a CMSIS-Toolbox nightly after 2.14.1 (build 2.14.1-68 confirmed); update the toolbox. Putting the options in a plain misc: node instead of setups: avoided the problem before.

## Source

Resolution: fixed-in-release

Versions: seen in 2.14.1, fixed after

From [Open-CMSIS-Pack/devtools #2603](https://github.com/Open-CMSIS-Pack/devtools/issues/2603), summarized in own words; confidence high, checked against the thread, not reviewed yet.
