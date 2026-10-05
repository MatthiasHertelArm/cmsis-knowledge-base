---
id: "iss-devtools-2335"
type: "troubleshooting"
domain: "project"
title: "csolution: Non-ASCII characters in user path become replacement characters in $G generator file"
summary: "Same encoding limitation as the non-ASCII project name problem: csolution does no UTF-8 conversion on Windows, so cbuild-gen.yml written under a profile path such as an accented user name contains the replacement character."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2335"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2335"
resolution: "workaround"
versions: "2.11.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Same encoding limitation as the non-ASCII project name problem: csolution does no UTF-8 conversion on Windows, so cbuild-gen.yml written under a profile path such as an accented user name contains the replacement character.

## Fix

Workaround: enable Windows Unicode UTF-8 worldwide language support, or work from a path with ASCII characters only.

## Source

Resolution: workaround

Versions: 2.11.0

From [Open-CMSIS-Pack/devtools #2335](https://github.com/Open-CMSIS-Pack/devtools/issues/2335), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
