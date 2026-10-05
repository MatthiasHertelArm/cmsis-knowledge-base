---
id: "iss-cpackget-272"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add ARM::CMSIS@>=6.0.0 exits with code 255 and prints nothing"
summary: "The unquoted > is interpreted by the shell as redirection, so the real error (bad pack name) is written to a file named after the version."
status: "draft"
tool: "cpackget"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/272"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/272"
resolution: "user-error"
versions: "cpackget 2.0.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The unquoted > is interpreted by the shell as redirection, so the real error (bad pack name) is written to a file named after the version.

## Fix

Quote the argument (cpackget add "ARM::CMSIS@>=6.0.0") or check for a stray file named 6.0.0 in the working directory.

## Source

Resolution: user-error

Versions: cpackget 2.0.0

From [Open-CMSIS-Pack/cpackget #272](https://github.com/Open-CMSIS-Pack/cpackget/issues/272), summarized in own words; confidence high, not reviewed yet.
