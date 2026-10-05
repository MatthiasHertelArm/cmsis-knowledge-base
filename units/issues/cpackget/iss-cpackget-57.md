---
id: "iss-cpackget-57"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add of an older pack version fails with 'URL for the pack cannot be determined'"
summary: "cpackget looked up the pdsc entry in index.pidx by vendor, name and the requested version, but the index lists only the latest version of each pack, so an older version cannot be found while its pdsc is not yet …"
status: "draft"
tool: "cpackget"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/57"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/57"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

cpackget looked up the pdsc entry in index.pidx by vendor, name and the requested version, but the index lists only the latest version of each pack, so an older version cannot be found while its pdsc is not yet in .Web. It should look up vendor and name only.

## Fix

Install the latest version of the pack first, so that its pdsc lands in .Web; the older version then installs. PR #60 changes the lookup to vendor and name.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/cpackget #57](https://github.com/Open-CMSIS-Pack/cpackget/issues/57), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
