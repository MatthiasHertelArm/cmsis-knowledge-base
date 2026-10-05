---
id: "iss-devtools-1826"
type: "troubleshooting"
domain: "project"
title: "cbuild: Build with an old pack fails on Linux and macOS because of backslashes in paths"
summary: "Older packs have backslashes in file paths of the pdsc, which csolution passed unchanged into the generated CMake file; on Windows this works, elsewhere it breaks the CMake syntax."
status: "draft"
tool: "cbuild"
symptoms: ["CMake Error at CMakeLists.txt:43:\n  Parse error.  Function missing ending \")\".  Instead found bad character\n  with text \"\\\"."]
symptom_regex: "CMake\\s+Error\\s+at\\s+CMakeLists\\.txt:\\S+:\\\\s+Parse\\s+error\\.\\s+Function\\s+missing\\s+ending\\s+\".*?\"\\.\\s+Instead\\s+found\\s+bad\\s+character\\\\s+with\\s+text\\s+\".*?\"\\."
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1826"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1826"
resolution: "fixed-in-release"
versions: "2.6.1, fixed in 2.7.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild", "csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`CMake Error at CMakeLists.txt:43:
  Parse error.  Function missing ending ")".  Instead found bad character
  with text "\".`

## Cause

Older packs have backslashes in file paths of the pdsc, which csolution passed unchanged into the generated CMake file; on Windows this works, elsewhere it breaks the CMake syntax.

## Fix

Fixed in CMSIS-Toolbox 2.7.0 (backslashes converted to forward slashes). On older versions use a newer version of the pack or correct the path in the pack.

## Source

Resolution: fixed-in-release

Versions: 2.6.1, fixed in 2.7.0

From [Open-CMSIS-Pack/devtools #1826](https://github.com/Open-CMSIS-Pack/devtools/issues/1826), summarized in own words; confidence high, not reviewed yet.
