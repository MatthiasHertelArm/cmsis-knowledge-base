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
resolution: "fixed-in-release"
versions: "fixed in packchk 1.3.9x"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["packchk"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Not Semantic Versioning: '2.0.0-alpha.0.5'`

## Cause

packchk's own version parser did not accept dot-separated pre-release identifiers, which SemVer allows; error M394 cannot be suppressed with -x.

## Fix

Fixed by checking versions with the regular expression of PACK.xsd (PackVersionType); use a packchk release containing it.

## Source

Resolution: fixed-in-release

Versions: fixed in packchk 1.3.9x

From [Open-CMSIS-Pack/devtools #329](https://github.com/Open-CMSIS-Pack/devtools/issues/329), summarized in own words; confidence medium, not reviewed yet.
