---
id: "iss-cpackget-499"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add fails because pack IDs were matched case-sensitively"
summary: "cpackget looked up pack IDs case-sensitively, so cpackget add ARM::ethos-u-core-driver@1.24.8, the pack ID a project referenced, did not find the pack."
status: "draft"
tool: "cpackget"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/499"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/499"
resolution: "workaround"
versions: "cpackget 2.1.6 affected; fixed in CMSIS-Toolbox nightly builds from 2025-04-10"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

cpackget looked up pack IDs case-sensitively, so cpackget add ARM::ethos-u-core-driver@1.24.8, the pack ID a project referenced, did not find the pack.

## Fix

Use a CMSIS-Toolbox nightly build from 2025-04-10 or later, whose cpackget looks up pack IDs case-insensitively; no release is named.

## Source

Resolution: workaround

Versions: cpackget 2.1.6 affected; fixed in CMSIS-Toolbox nightly builds from 2025-04-10

From [Open-CMSIS-Pack/cpackget #499](https://github.com/Open-CMSIS-Pack/cpackget/issues/499), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
