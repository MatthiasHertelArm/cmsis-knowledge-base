---
id: "iss-toolbox-132"
type: "troubleshooting"
domain: "project"
title: "cbuild: Working directory of executes commands is the tmp folder"
summary: "The working directory of an execute run command is intentionally unspecified (it was the intermediate directory), so relative script paths break."
status: "draft"
tool: "cbuild"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/132"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/132"
resolution: "not-a-bug"
versions: "toolbox 2.4.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The working directory of an execute run command is intentionally unspecified (it was the intermediate directory), so relative script paths break.

## Fix

List scripts as input and refer to them with access sequences: run: python $input(0)$ with input: $ProjectDir()$/scripts/script.py.

## Source

Resolution: not-a-bug

Versions: toolbox 2.4.0

From [Open-CMSIS-Pack/cmsis-toolbox #132](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/132), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
