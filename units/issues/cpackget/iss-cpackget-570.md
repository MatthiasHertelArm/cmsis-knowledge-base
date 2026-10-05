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
resolution: "workaround"
versions: "clearer message in cpackget nightly 2.1.8-45-g83198e5 (2025-09-10)"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: invalid dimensions`

## Cause

The license text is shown in a text window that needs a minimum terminal size. If the terminal (for example a VS Code panel reduced to a few lines) is smaller, the UI library fails with this cryptic message.

## Fix

Enlarge the terminal to at least 50 columns by 8 rows and repeat the command. The cpackget nightly 2.1.8-45-g83198e5 (2025-09-10) checks the size first and prints 'increase window size to display license information and obtain user response to at least 50x8'.

## Source

Resolution: workaround

Versions: clearer message in cpackget nightly 2.1.8-45-g83198e5 (2025-09-10)

From [Open-CMSIS-Pack/cpackget #570](https://github.com/Open-CMSIS-Pack/cpackget/issues/570), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
