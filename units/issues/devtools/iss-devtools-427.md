---
id: "iss-devtools-427"
type: "troubleshooting"
domain: "project"
title: "csolution: $Output(...)$ access sequences stay unresolved in output-dirs for inter-project references"
summary: "Access sequences inside output-dirs were not evaluated when another project referenced the output of a sibling project; also output-dirs is only accepted in csolution.yml, a key in cproject.yml triggers a warning that it was not recognized."
status: "draft"
tool: "csolution"
symptoms: ["Path not found: /trustzone_examples/hello_world/cm33_core0/hello_world_ns/..\\hello_world_s\\$Project$\\$Compiler$\\$BuildType$hello_world_s.debug+Board_CMSE_Lib.o"]
symptom_regex: "Path\\s+not\\s+found:\\s+\\S+\\$Project\\$\\\\\\$Compiler\\$\\\\\\$BuildType\\$hello_world_s\\.debug\\+Board_CMSE_Lib\\.o"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/427"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/427"
resolution: "fixed-in-release"
versions: "fixed in 1.1.0"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Path not found: /trustzone_examples/hello_world/cm33_core0/hello_world_ns/..\hello_world_s\$Project$\$Compiler$\$BuildType$hello_world_s.debug+Board_CMSE_Lib.o`

## Cause

Access sequences inside output-dirs were not evaluated when another project referenced the output of a sibling project; also output-dirs is only accepted in csolution.yml, a key in cproject.yml triggers a warning that it was not recognized.

## Fix

Fixed in CMSIS-Toolbox 1.1.0. Put output-dirs into csolution.yml, not into cproject.yml.

## Source

Resolution: fixed-in-release

Versions: fixed in 1.1.0

From [Open-CMSIS-Pack/devtools #427](https://github.com/Open-CMSIS-Pack/devtools/issues/427), summarized in own words; confidence high, checked against the thread, not reviewed yet.
