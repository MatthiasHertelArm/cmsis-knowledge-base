---
id: "iss-devtools-1826"
type: "troubleshooting"
domain: "project"
title: "cbuild: Build with an old pack fails on Linux and macOS because of backslashes in paths"
summary: "Older packs have backslashes in path names, which csolution passed unchanged into the generated CMake file; on Linux and macOS this breaks the CMake syntax."
status: "draft"
tool: "cbuild"
symptoms: ["CMake Error at CMakeLists.txt:43:\n  Parse error.  Function missing ending \")\".  Instead found bad character\n  with text \"\\\"."]
symptom_regex: "CMake\\s+Error\\s+at\\s+CMakeLists\\.txt:\\S+:\\\\s+Parse\\s+error\\.\\s+Function\\s+missing\\s+ending\\s+\".*?\"\\.\\s+Instead\\s+found\\s+bad\\s+character\\\\s+with\\s+text\\s+\".*?\"\\."
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1826"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1826"
resolution: "fixed-in-release"
versions: "CMSIS-Toolbox 2.6.1 affected"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild", "csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`CMake Error at CMakeLists.txt:43:
  Parse error.  Function missing ending ")".  Instead found bad character
  with text "\".`

## Cause

Older packs have backslashes in path names, which csolution passed unchanged into the generated CMake file; on Linux and macOS this breaks the CMake syntax.

## Fix

Use a CMSIS-Toolbox nightly from 2024-12-10 or later, with which the example builds on Linux; the request was that csolution converts backslashes to forward slashes.

## Source

Resolution: fixed-in-release

Versions: CMSIS-Toolbox 2.6.1 affected

From [Open-CMSIS-Pack/devtools #1826](https://github.com/Open-CMSIS-Pack/devtools/issues/1826), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
