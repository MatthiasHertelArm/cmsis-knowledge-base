---
id: "iss-pyocd-1547"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: i.MX RT685 pack: debug sequence parse error on 'U' integer suffix and no cores discovered"
summary: "The NXP pack uses C-style 'U' suffixes on integer literals in a debug sequence, which pyOCD's parser rejected."
status: "draft"
tool: "pyocd"
symptoms: ["Unexpected token Token('IDENT', 'U') at line 3, column 34.", "C No cores were discovered! [__main__]"]
symptom_regex: "Unexpected\\s+token\\s+Token\\('.*?',\\s+'.*?'\\)\\s+at\\s+line\\s+\\S+,\\s+column\\s+\\S+\\."
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1547"
doc_source: "https://github.com/pyocd/pyOCD/issues/1547"
resolution: "workaround"
versions: "NXP.MIMXRT685S_DFP 16.0.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["MIMXRT685S"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Unexpected token Token('IDENT', 'U') at line 3, column 34.`
`C No cores were discovered! [__main__]`

## Cause

The NXP pack uses C-style 'U' suffixes on integer literals in a debug sequence, which pyOCD's parser rejected. After that, DebugPortStart was assigned to the named core cm33; pyOCD did not support core-specific DebugPort* sequences, so the debug unlock sequence did not run and the CM33 access port stayed disabled.

## Fix

Parser fix in pull request #1548 (installable from the branch). For the second problem remove Pname="cm33" from the DebugPortStart sequence in the pdsc and pass the expanded pack directory to --pack, until core-specific port sequences are supported. Use the .FLM extracted from the pack, not NXP's .cfx.

## Source

Resolution: workaround

Versions: NXP.MIMXRT685S_DFP 16.0.0

From [pyocd/pyOCD #1547](https://github.com/pyocd/pyOCD/issues/1547), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
