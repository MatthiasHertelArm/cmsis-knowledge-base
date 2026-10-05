---
id: "iss-toolbox-99"
type: "troubleshooting"
domain: "project"
title: "cbuild: Database generation fails because the RTE folder does not exist yet"
summary: "The compile_commands.json generation ran before the RTE folder was populated."
status: "draft"
tool: "cbuild"
symptoms: ["*** WARNING M634:", "error cbuild: error executing 'cbuildgen cmake'"]
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/99"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/99"
resolution: "workaround"
versions: "toolbox 2.2.1"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`*** WARNING M634:`
`error cbuild: error executing 'cbuildgen cmake'`

## Cause

The compile_commands.json generation ran before the RTE folder was populated. The warning itself says to use --update-rte; the extension must update RTE first.

## Fix

Run a build or touch the csolution.yml so cbuild runs with --update-rte (or csolution update-rte).

## Source

Resolution: workaround

Versions: toolbox 2.2.1

From [Open-CMSIS-Pack/cmsis-toolbox #99](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/99), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
