---
id: "iss-pyocd-505"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pip install pyocd fails on Windows with a gbk UnicodeDecodeError in setup.py"
summary: "On a system whose default code page is gbk, setup.py opened README.md, which contains non-ASCII characters, without specifying an encoding."
status: "draft"
tool: "pyocd"
symptoms: ["UnicodeDecodeError: 'gbk' codec can't decode byte 0xa6 in position 6075: illegal multibyte sequence"]
symptom_regex: "UnicodeDecodeError:\\s+'.*?'\\s+codec\\s+can't\\s+decode\\s+byte\\s+\\S+\\s+in\\s+position\\s+\\S+:\\s+illegal\\s+multibyte\\s+sequence"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/505"
doc_source: "https://github.com/pyocd/pyOCD/issues/505"
resolution: "fixed-in-release"
versions: "0.14.3 affected"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`UnicodeDecodeError: 'gbk' codec can't decode byte 0xa6 in position 6075: illegal multibyte sequence`

## Cause

On a system whose default code page is gbk, setup.py opened README.md, which contains non-ASCII characters, without specifying an encoding.

## Fix

Use a pyOCD version that contains PR #495, which fixed reading the file in setup.py.

## Source

Resolution: fixed-in-release

Versions: 0.14.3 affected

From [pyocd/pyOCD #505](https://github.com/pyocd/pyOCD/issues/505), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
