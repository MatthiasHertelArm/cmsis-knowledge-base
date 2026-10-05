---
id: "iss-pyocd-1518"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Semihosting binary file write raises UnicodeDecodeError"
summary: "The semihosting layer decodes target data as UTF-8 text even when the file is opened as binary."
status: "draft"
tool: "pyocd"
symptoms: ["UnicodeDecodeError: 'utf-8' codec can't decode byte 0x81 in position 0: invalid start byte"]
symptom_regex: "UnicodeDecodeError:\\s+'.*?'\\s+codec\\s+can't\\s+decode\\s+byte\\s+\\S+\\s+in\\s+position\\s+\\S+:\\s+invalid\\s+start\\s+byte"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1518"
doc_source: "https://github.com/pyocd/pyOCD/issues/1518"
resolution: "workaround"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`UnicodeDecodeError: 'utf-8' codec can't decode byte 0x81 in position 0: invalid start byte`

## Cause

The semihosting layer decodes target data as UTF-8 text even when the file is opened as binary.

## Fix

Maintainers agreed the string helper must return bytes and only text-mode files should be encoded or decoded; also let the target open files in binary mode. Check for a release with the change.

## Source

Resolution: workaround

From [pyocd/pyOCD #1518](https://github.com/pyocd/pyOCD/issues/1518), summarized in own words; confidence low, not reviewed yet.
