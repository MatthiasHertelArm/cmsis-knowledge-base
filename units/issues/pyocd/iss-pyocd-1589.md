---
id: "iss-pyocd-1589"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: HC32L130 built-in target cannot write above 32 KB"
summary: "The built-in memory map for the part covered only the first 32 KB of flash."
status: "draft"
tool: "pyocd"
symptoms: ["W Failed to add data chunk: no memory region defined for address 0x00008000 [file_programmer]"]
symptom_regex: "W\\s+Failed\\s+to\\s+add\\s+data\\s+chunk:\\s+no\\s+memory\\s+region\\s+defined\\s+for\\s+address\\s+\\S+"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1589"
doc_source: "https://github.com/pyocd/pyOCD/issues/1589"
resolution: "fixed-in-release"
versions: "0.35.1"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["HC32L130F8UA"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`W Failed to add data chunk: no memory region defined for address 0x00008000 [file_programmer]`

## Cause

The built-in memory map for the part covered only the first 32 KB of flash.

## Fix

Fixed by change #1590; use a release containing it, or use the vendor pack with the specific part name.

## Source

Resolution: fixed-in-release

Versions: 0.35.1

From [pyocd/pyOCD #1589](https://github.com/pyocd/pyOCD/issues/1589), summarized in own words; confidence medium, not reviewed yet.
