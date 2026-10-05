---
id: "iss-devtools-1397"
type: "troubleshooting"
domain: "project"
title: "csolution: cbuild-idx.yml schema validation fails because cdefault node is missing in the schema"
summary: "The cbuild-idx.yml schema did not define the cdefault node that the toolbox writes, and additionalProperties is false, so validation of generated files failed."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1397"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1397"
resolution: "unresolved"
versions: "csolution 2.2.1 (schema 2.2.1)"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The cbuild-idx.yml schema did not define the cdefault node that the toolbox writes, and additionalProperties is false, so validation of generated files failed.

## Fix

Add cdefault to the schema so it matches the current output and stays tolerant of keys from previous versions; agreed as PRs #1416 and #1419 in the 2024-04-02 meeting, no release named.

## Source

Resolution: unresolved

Versions: csolution 2.2.1 (schema 2.2.1)

From [Open-CMSIS-Pack/devtools #1397](https://github.com/Open-CMSIS-Pack/devtools/issues/1397), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
