---
id: "iss-pyocd-634"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Loading an STM32F401RE pack under Python 2.7 crashes with unbound method error"
summary: "The pack-target code fails on Python 2.7 only: the generated target __init__ is treated as an unbound method of _PackTargetMethods."
status: "draft"
tool: "pyocd"
symptoms: ["uncaught exception: unbound method _pack_target__init__() must be called with _PackTargetMethods instance as first argument (got Session instance instead)"]
symptom_regex: "uncaught\\s+exception:\\s+unbound\\s+method\\s+_pack_target__init__\\(\\)\\s+must\\s+be\\s+called\\s+with\\s+_PackTargetMethods\\s+instance\\s+as\\s+first\\s+argument\\s+\\(got\\s+Session\\s+instance\\s+instead\\)"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/634"
doc_source: "https://github.com/pyocd/pyOCD/issues/634"
resolution: "workaround"
versions: "0.19.1.dev61"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["STM32F401RETx"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`uncaught exception: unbound method _pack_target__init__() must be called with _PackTargetMethods instance as first argument (got Session instance instead)`

## Cause

The pack-target code fails on Python 2.7 only: the generated target __init__ is treated as an unbound method of _PackTargetMethods. A typo (isinstane) was also found in pack_target.py.

## Fix

Use Python 3, where the error does not occur (the maintainer recommends 3.7), and correct the isinstane typo in pack_target.py by hand; the maintainer said he would fix it quickly.

## Source

Resolution: workaround

Versions: 0.19.1.dev61

From [pyocd/pyOCD #634](https://github.com/pyocd/pyOCD/issues/634), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
