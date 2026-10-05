---
id: "iss-devtools-1553"
type: "troubleshooting"
domain: "project"
title: "csolution: Schema 2.3 rejects cbuild.yml files written by toolbox 2.1/2.2 (from-pack missing)"
summary: "Schema version 2.3 made from-pack required for generators, but files from older toolbox versions do not contain it, so validating them with that schema fails."
status: "draft"
tool: "csolution"
symptoms: ["missing properties: 'from-pack'"]
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1553"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1553"
resolution: "fixed-in-release"
versions: "schema 2.3"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution", "cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`missing properties: 'from-pack'`

## Cause

Schema version 2.3 made from-pack required for generators, but files from older toolbox versions do not contain it, so validating them with that schema fails.

## Fix

The schema was changed so from-pack is optional again; use a newer schema, or regenerate the files with a current toolbox.

## Source

Resolution: fixed-in-release

Versions: schema 2.3

From [Open-CMSIS-Pack/devtools #1553](https://github.com/Open-CMSIS-Pack/devtools/issues/1553), summarized in own words; confidence high, not reviewed yet.
