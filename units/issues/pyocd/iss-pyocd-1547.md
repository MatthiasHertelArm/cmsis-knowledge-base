---
id: "iss-pyocd-1547"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: i.MX RT685 pack: debug sequence parse error on 'U' integer suffix and no cores discovered"
summary: "The NXP pack uses C-style 'U' suffixes in debug sequence literals, which pyOCD's parser rejected."
status: "draft"
tool: "pyocd"
symptoms: ["Unexpected token Token('IDENT', 'U') at line 3, column 34.", "C No cores were discovered! [__main__]"]
symptom_regex: "Unexpected\\s+token\\s+Token\\('.*?',\\s+'.*?'\\)\\s+at\\s+line\\s+\\S+,\\s+column\\s+\\S+\\."
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1547"
doc_source: "https://github.com/pyocd/pyOCD/issues/1547"
resolution: "fixed-in-release"
versions: "0.35"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["MIMXRT685S"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Unexpected token Token('IDENT', 'U') at line 3, column 34.`
`C No cores were discovered! [__main__]`

## Cause

The NXP pack uses C-style 'U' suffixes in debug sequence literals, which pyOCD's parser rejected. Later, DebugPortStart was bound to a named core, so pyOCD did not run it and the debug AP stayed locked.

## Fix

Parser fix in change #1548. For the second problem remove Pname="cm33" from the DebugPortStart sequence in the pdsc (use an expanded pack directory) until core-specific port sequences are supported. Use the .FLM from the pack, not the .cfx.

## Source

Resolution: fixed-in-release

Versions: 0.35

From [pyocd/pyOCD #1547](https://github.com/pyocd/pyOCD/issues/1547), summarized in own words; confidence high, not reviewed yet.
