---
id: "iss-devtools-1397"
type: "troubleshooting"
domain: "project"
title: "csolution: cbuild-idx.yml schema validation fails because cdefault node is missing in the schema"
summary: "The cbuild-idx.yml schema did not define the cdefault node that newer toolbox versions write, and additionalProperties is false, so validation of generated files failed."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1397"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1397"
resolution: "fixed-in-release"
versions: "2.3.0-dev"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The cbuild-idx.yml schema did not define the cdefault node that newer toolbox versions write, and additionalProperties is false, so validation of generated files failed.

## Fix

Schema corrected (cdefault added, tolerant of older keys); fixed with the schema updates of April 2024 (toolbox 2.3.0).

## Source

Resolution: fixed-in-release

Versions: 2.3.0-dev

From [Open-CMSIS-Pack/devtools #1397](https://github.com/Open-CMSIS-Pack/devtools/issues/1397), summarized in own words; confidence medium, not reviewed yet.
