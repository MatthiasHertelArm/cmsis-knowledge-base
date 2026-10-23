---
id: "iss-pyocd-2025"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Sparse HEX holes filled with 0xFF when FLM valEmpty is 0x00 on single-sector flash"
summary: "When the FLM describes one uniform sector range covering the whole flash region, pyOCD creates no subregions and never copies the FLM valEmpty value to the parent flash region."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/2025"
doc_source: "https://github.com/pyocd/pyOCD/issues/2025"
resolution: "workaround"
versions: "Reported on pyOCD 0.44.1; 0.45.1 was also inspected, and the related logic appears unchanged there. No release containing the PR is named."
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

When the FLM describes one uniform sector range covering the whole flash region, pyOCD creates no subregions and never copies the FLM valEmpty value to the parent flash region. The region keeps its default erased byte of 0xFF, so the page buffers used for sparse image programming fill gaps with 0xFF instead of the chip's real erased value.

## Fix

Set erased_byte_value to the FLM valEmpty value (0x00 for this target) on the affected region and its subregions, using a project-local pyocd_user.py hook as the reporter did. The thread says the issue was fixed by PR #2032, which propagates valEmpty to the parent region's erased_byte_value, but it does not name a release containing that change.

## Source

Resolution: workaround

Versions: Reported on pyOCD 0.44.1; 0.45.1 was also inspected, and the related logic appears unchanged there. No release containing the PR is named.

From [pyocd/pyOCD #2025](https://github.com/pyocd/pyOCD/issues/2025), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
