---
id: "iss-devtools-1952"
type: "troubleshooting"
domain: "project"
title: "csolution: Misleading ninja error when the linker script named in the project does not exist"
summary: "csolution did not check linker: script: files, so a typo only surfaced as a ninja error late in the build."
status: "draft"
tool: "csolution"
symptoms: ["ninja: error: '<project>/RTE/Device/<device>/ac6_linker_script.sct.srcx', needed by '<out>/CubeMX.axf', missing and no known rule to make it"]
symptom_regex: "ninja:\\s+error:\\s+'.*?',\\s+needed\\s+by\\s+'.*?',\\s+missing\\s+and\\s+no\\s+known\\s+rule\\s+to\\s+make\\s+it"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1952"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1952"
resolution: "fixed-in-release"
versions: "2.7.0, fixed in later nightly"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["csolution", "cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ninja: error: '<project>/RTE/Device/<device>/ac6_linker_script.sct.srcx', needed by '<out>/CubeMX.axf', missing and no known rule to make it`

## Cause

csolution did not check linker: script: files, so a typo only surfaced as a ninja error late in the build.

## Fix

Check the file name under linker: script: in the cproject.yml. Toolbox builds after 2.7.0 report error csolution: file '...' was not found at setup time.

## Source

Resolution: fixed-in-release

Versions: 2.7.0, fixed in later nightly

From [Open-CMSIS-Pack/devtools #1952](https://github.com/Open-CMSIS-Pack/devtools/issues/1952), summarized in own words; confidence high, checked against the thread, not reviewed yet.
