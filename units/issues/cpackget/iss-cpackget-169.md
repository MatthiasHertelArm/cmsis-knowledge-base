---
id: "iss-cpackget-169"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add -f packs.txt downloads required packs that are already installed"
summary: "The check for already satisfied requirement packs did not handle the internal unbounded upper version marker, so installed dependencies were not recognised."
status: "draft"
tool: "cpackget"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/169"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/169"
resolution: "fixed-in-release"
versions: "fixed in 0.9.4"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The check for already satisfied requirement packs did not handle the internal unbounded upper version marker, so installed dependencies were not recognised.

## Fix

Use cpackget 0.9.4 or later.

## Source

Resolution: fixed-in-release

Versions: fixed in 0.9.4

From [Open-CMSIS-Pack/cpackget #169](https://github.com/Open-CMSIS-Pack/cpackget/issues/169), summarized in own words; confidence high, checked against the thread, not reviewed yet.
