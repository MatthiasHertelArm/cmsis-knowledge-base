---
id: "iss-cpackget-197"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget update-index -a leaves some pdsc files missing in .Web"
summary: "The concurrent download scheduler spawned more workers than configured and did not wait for the last ones, so some downloaded files were cut off or never moved to .Web."
status: "draft"
tool: "cpackget"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/197"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/197"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The concurrent download scheduler spawned more workers than configured and did not wait for the last ones, so some downloaded files were cut off or never moved to .Web.

## Fix

Use a cpackget with the semaphore-based scheduler (fixed September 2023); as a workaround run update-index -a -C 0 to disable concurrency.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/cpackget #197](https://github.com/Open-CMSIS-Pack/cpackget/issues/197), summarized in own words; confidence high, not reviewed yet.
