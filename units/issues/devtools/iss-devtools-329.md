---
id: "iss-devtools-329"
type: "troubleshooting"
domain: "pack"
title: "packchk: M394 Not Semantic Versioning for pre-release versions with dots (2.0.0-alpha.0.5)"
summary: "packchk's own version parser did not accept dot-separated pre-release identifiers, which SemVer allows; error M394 cannot be suppressed with -x."
status: "draft"
tool: "packchk"
symptoms: ["Not Semantic Versioning: '2.0.0-alpha.0.5'"]
symptom_regex: "Not\\s+Semantic\\s+Versioning:\\s+'.*?'"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/329"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/329"
resolution: "unresolved"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["packchk"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Not Semantic Versioning: '2.0.0-alpha.0.5'`

## Cause

packchk's own version parser did not accept dot-separated pre-release identifiers, which SemVer allows; error M394 cannot be suppressed with -x.

## Fix

The maintainer was changing packchk to check versions with the PackVersionType regular expression of PACK.xsd; the thread does not confirm a merged fix or a release.

## Source

Resolution: unresolved

From [Open-CMSIS-Pack/devtools #329](https://github.com/Open-CMSIS-Pack/devtools/issues/329), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
