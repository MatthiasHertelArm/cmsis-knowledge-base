---
id: "iss-pyocd-444"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd-flashtool / pyocd-gdbserver ImportError after installing pyOCD 0.13.0"
summary: "The released 0.13.0 sdist contained the package directory with the wrong letter case, so Python could not import pyocd on case-sensitive or case-aware setups."
status: "draft"
tool: "pyocd"
symptoms: ["ImportError: No module named pyocd.tools.flash_tool"]
symptom_regex: "ImportError:\\s+No\\s+module\\s+named\\s+pyocd\\.tools\\.flash_tool"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/444"
doc_source: "https://github.com/pyocd/pyOCD/issues/444"
resolution: "fixed-in-release"
versions: "0.13.0 affected; 0.13.1 fixed"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ImportError: No module named pyocd.tools.flash_tool`

## Cause

The released 0.13.0 sdist contained the package directory with the wrong letter case, so Python could not import pyocd on case-sensitive or case-aware setups.

## Fix

Upgrade to pyOCD 0.13.1 or later; temporary workaround was renaming the installed folder to lowercase pyocd.

## Source

Resolution: fixed-in-release

Versions: 0.13.0 affected; 0.13.1 fixed

From [pyocd/pyOCD #444](https://github.com/pyocd/pyOCD/issues/444), summarized in own words; confidence high, not reviewed yet.
