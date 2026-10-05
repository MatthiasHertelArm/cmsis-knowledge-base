---
id: "iss-cpackget-570"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add prints 'E: invalid dimensions' in a very small terminal window"
summary: "The license text is shown in a text window that needs a minimum terminal size."
status: "draft"
tool: "cpackget"
symptoms: ["E: invalid dimensions"]
symptom_regex: "E:\\s+invalid\\s+dimensions"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/570"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/570"
resolution: "fixed-in-release"
versions: "clearer message from 2.1.8 nightly 2025-09-10"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: invalid dimensions`

## Cause

The license text is shown in a text window that needs a minimum terminal size. If the terminal (for example a VS Code panel reduced to a few lines) is smaller, the UI library fails with this cryptic message.

## Fix

Enlarge the terminal (about 50 columns by 8 rows or more) and repeat the command; newer cpackget prints 'increase window size to display license information and obtain user response to at least 50x8'. Alternatively pass --agree-embedded-license.

## Source

Resolution: fixed-in-release

Versions: clearer message from 2.1.8 nightly 2025-09-10

From [Open-CMSIS-Pack/cpackget #570](https://github.com/Open-CMSIS-Pack/cpackget/issues/570), summarized in own words; confidence high, not reviewed yet.
