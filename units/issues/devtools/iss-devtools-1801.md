---
id: "iss-devtools-1801"
type: "troubleshooting"
domain: "project"
title: "cbuild: cbuild --rebuild cannot remove tmp directory"
summary: "The tmp directory was in use (opened as working directory in a shell or an editor), so Windows could not delete it."
status: "draft"
tool: "cbuild"
symptoms: ["Error removing directory \"<project>/tmp\".", "error cbuild: error cleaning '<project>/<name>.cbuild-idx.yml'"]
symptom_regex: "Error\\s+removing\\s+directory\\s+\".*?\"\\."
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1801"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1801"
resolution: "fixed-in-release"
versions: "2.6.1"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Error removing directory "<project>/tmp".`
`error cbuild: error cleaning '<project>/<name>.cbuild-idx.yml'`

## Cause

The tmp directory was in use (opened as working directory in a shell or an editor), so Windows could not delete it.

## Fix

Close terminals and editors that sit in tmp; with the changed cleanup in CMSIS-Toolbox 2.7.0 the error no longer occurred.

## Source

Resolution: fixed-in-release

Versions: 2.6.1

From [Open-CMSIS-Pack/devtools #1801](https://github.com/Open-CMSIS-Pack/devtools/issues/1801), summarized in own words; confidence medium, not reviewed yet.
