---
id: "iss-pyocd-1958"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd pack install with a name prefix finds no devices on Python 3.14"
summary: "A change in how prefix matching worked broke under Python 3.14; the same command works on Python 3.13 and a full part name always works."
status: "draft"
tool: "pyocd"
symptoms: ["W No matching devices"]
symptom_regex: "W\\s+No\\s+matching\\s+devices"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1958"
doc_source: "https://github.com/pyocd/pyOCD/issues/1958"
resolution: "fixed-in-release"
versions: "seen on 0.44.0 with Python 3.14"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`W No matching devices`

## Cause

A change in how prefix matching worked broke under Python 3.14; the same command works on Python 3.13 and a full part name always works.

## Fix

Use Python 3.13 or earlier, install the full part number, or upgrade to a pyOCD release containing change #1993.

## Source

Resolution: fixed-in-release

Versions: seen on 0.44.0 with Python 3.14

From [pyocd/pyOCD #1958](https://github.com/pyocd/pyOCD/issues/1958), summarized in own words; confidence high, checked against the thread, not reviewed yet.
