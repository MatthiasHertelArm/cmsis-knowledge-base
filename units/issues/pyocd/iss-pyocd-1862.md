---
id: "iss-pyocd-1862"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pip install pyocd fails building hidapi on Python 3.14"
summary: "hidapi had no wheel for Python 3.14 so pip compiled it and needed a C++ build toolchain; libusb-package also lacked a 3.14 wheel at first."
status: "draft"
tool: "pyocd"
symptoms: ["Building wheel for hidapi (pyproject.toml) ... error"]
symptom_regex: "Building\\s+wheel\\s+for\\s+hidapi\\s+\\(pyproject\\.toml\\)\\s+\\.\\.\\.\\s+error"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1862"
doc_source: "https://github.com/pyocd/pyOCD/issues/1862"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Building wheel for hidapi (pyproject.toml) ... error`

## Cause

hidapi had no wheel for Python 3.14 so pip compiled it and needed a C++ build toolchain; libusb-package also lacked a 3.14 wheel at first.

## Fix

Use a recent pyOCD: hidapi 0.15.0 and a newer libusb-package ship Python 3.14 wheels, so install works without a compiler. Otherwise use an older Python.

## Source

Resolution: fixed-in-release

From [pyocd/pyOCD #1862](https://github.com/pyocd/pyOCD/issues/1862), summarized in own words; confidence high, not reviewed yet.
