---
id: "iss-pyocd-1518"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Semihosting binary file write raises UnicodeDecodeError"
summary: "SemihostAgent._get_string() decodes target data as UTF-8 regardless of whether the file was opened as binary, so non-UTF-8 binary data written via semihosting raises an exception."
status: "draft"
tool: "pyocd"
symptoms: ["UnicodeDecodeError: 'utf-8' codec can't decode byte 0x81 in position 0: invalid start byte"]
symptom_regex: "UnicodeDecodeError:\\s+'.*?'\\s+codec\\s+can't\\s+decode\\s+byte\\s+\\S+\\s+in\\s+position\\s+\\S+:\\s+invalid\\s+start\\s+byte"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1518"
doc_source: "https://github.com/pyocd/pyOCD/issues/1518"
resolution: "unresolved"
confidence: "low"
cause_origin: "issue-digest"
checked: "unsupported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`UnicodeDecodeError: 'utf-8' codec can't decode byte 0x81 in position 0: invalid start byte`

## Cause

SemihostAgent._get_string() decodes target data as UTF-8 regardless of whether the file was opened as binary, so non-UTF-8 binary data written via semihosting raises an exception.

## Fix

No fix in the thread. Maintainer and reporter agreed that _get_string() should return bytes and only text-mode files be encoded/decoded, and that target libraries (picolibc) should open files in binary mode by default.

## Source

Resolution: unresolved

From [pyocd/pyOCD #1518](https://github.com/pyocd/pyOCD/issues/1518), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
