---
id: "iss-cpackget-387"
type: "troubleshooting"
domain: "pack"
title: "cpackget: Stale pdsc files remain in .Web after a vendor withdraws packs from the index"
summary: "cpackget init only downloads the new index.pidx and does not clean .Web; removing pdsc files that are no longer listed is done by update-index -a."
status: "draft"
tool: "cpackget"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/387"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/387"
resolution: "user-error"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

cpackget init only downloads the new index.pidx and does not clean .Web; removing pdsc files that are no longer listed is done by update-index -a.

## Fix

Run cpackget update-index -a; it prints a warning per pdsc no longer present in the index and deletes the file. Make sure copies of pdsc files keep file name and the name element consistent.

## Source

Resolution: user-error

From [Open-CMSIS-Pack/cpackget #387](https://github.com/Open-CMSIS-Pack/cpackget/issues/387), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
