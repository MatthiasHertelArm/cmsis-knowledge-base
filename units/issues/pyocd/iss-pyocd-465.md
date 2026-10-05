---
id: "iss-pyocd-465"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: ImportError for pyocd.tools.gdb_server after upgrading to 0.13"
summary: "pyOCD 0.13 renamed the package from pyOCD to pyocd; the maintainer suspected that on a case-insensitive filesystem an upgrade may leave the installed folder with the old name, so the import of pyocd fails."
status: "draft"
tool: "pyocd"
symptoms: ["ImportError: No module named pyocd.tools.gdb_server"]
symptom_regex: "ImportError:\\s+No\\s+module\\s+named\\s+pyocd\\.tools\\.gdb_server"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/465"
doc_source: "https://github.com/pyocd/pyOCD/issues/465"
resolution: "fixed-in-release"
versions: "0.13.2 affected; 0.12.x works"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ImportError: No module named pyocd.tools.gdb_server`

## Cause

pyOCD 0.13 renamed the package from pyOCD to pyocd; the maintainer suspected that on a case-insensitive filesystem an upgrade may leave the installed folder with the old name, so the import of pyocd fails. He could not reproduce it.

## Fix

Upgrade to the latest pyOCD with `pip install -U pyocd`, which resolved it for the reporter. Other suggestions in the thread: uninstall and reinstall in a virtualenv, or rename the installed package folder to pyocd by hand (needed by another user on Windows).

## Source

Resolution: fixed-in-release

Versions: 0.13.2 affected; 0.12.x works

From [pyocd/pyOCD #465](https://github.com/pyocd/pyOCD/issues/465), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
