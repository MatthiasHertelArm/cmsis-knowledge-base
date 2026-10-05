---
id: "iss-toolbox-128"
type: "troubleshooting"
domain: "project"
title: "cbuild: Function-like macro in define: is split into many -D options"
summary: "Unescaped parentheses and dots are tokenised by the generator, so macros like NAME(...)=value become several defines."
status: "draft"
tool: "cbuild"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/128"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/128"
resolution: "workaround"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Unescaped parentheses and dots are tokenised by the generator, so macros like NAME(...)=value become several defines.

## Fix

Escape the characters or use YAML quoting that preserves inner quotes, e.g. - '"NAME(...)=((void)0)"'. Reporter later found a newer CMake accepts the form.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/cmsis-toolbox #128](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/128), summarized in own words; confidence low, not reviewed yet.
