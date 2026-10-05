---
id: "iss-devtools-1812"
type: "troubleshooting"
domain: "project"
title: "csolution: csolution run -g fails with missing component of an unselected sibling context"
summary: "All contexts that share the generator id, base-dir and cgen-file (and multi-core, secure/non-secure and map: siblings) are processed together, and a defect did not load packs additionally required by the unselected siblings, causing a false dependency failure."
status: "draft"
tool: "csolution"
symptoms: ["error csolution: no component was found with identifier 'Security:mbed TLS'"]
symptom_regex: "no\\s+component\\s+was\\s+found\\s+with\\s+identifier\\s+'.*?'"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1812"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1812"
resolution: "workaround"
versions: "csolution 2.6.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: no component was found with identifier 'Security:mbed TLS'`

## Cause

All contexts that share the generator id, base-dir and cgen-file (and multi-core, secure/non-secure and map: siblings) are processed together, and a defect did not load packs additionally required by the unselected siblings, causing a false dependency failure.

## Fix

Workaround: select all sibling contexts, here by leaving out -c, for example csolution run Network.csolution.yml -g CubeMX. csolution list generators <solution> -v shows the siblings.

## Source

Resolution: workaround

Versions: csolution 2.6.0

From [Open-CMSIS-Pack/devtools #1812](https://github.com/Open-CMSIS-Pack/devtools/issues/1812), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
