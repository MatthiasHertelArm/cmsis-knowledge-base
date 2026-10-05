---
id: "iss-devtools-1801"
type: "troubleshooting"
domain: "project"
title: "cbuild: cbuild --rebuild cannot remove tmp directory"
summary: "The tmp directory was open as the working directory of a Bash shell, so with CMSIS-Toolbox 2.6.1 the rebuild could not delete it on Windows."
status: "draft"
tool: "cbuild"
symptoms: ["Error removing directory \"<project>/tmp\".", "error cbuild: error cleaning '<project>/<name>.cbuild-idx.yml'"]
symptom_regex: "Error\\s+removing\\s+directory\\s+\".*?\"\\."
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1801"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1801"
resolution: "fixed-in-release"
versions: "2.6.1 affected; 2.7.0 works"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Error removing directory "<project>/tmp".`
`error cbuild: error cleaning '<project>/<name>.cbuild-idx.yml'`

## Cause

The tmp directory was open as the working directory of a Bash shell, so with CMSIS-Toolbox 2.6.1 the rebuild could not delete it on Windows.

## Fix

Leave the tmp directory in the shell before rebuilding; with the changed cleanup strategy of CMSIS-Toolbox 2.7.0 (cbuild PR #343) the same steps no longer give an error.

## Source

Resolution: fixed-in-release

Versions: 2.6.1 affected; 2.7.0 works

From [Open-CMSIS-Pack/devtools #1801](https://github.com/Open-CMSIS-Pack/devtools/issues/1801), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
