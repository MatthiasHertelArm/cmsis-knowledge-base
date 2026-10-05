---
id: "iss-pyocd-634"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Loading an STM32F401RE pack under Python 2.7 crashes with unbound method error"
summary: "The pack-target code dynamically built methods in a way that works only on Python 3; on Python 2.7 the bound-method check fails."
status: "draft"
tool: "pyocd"
symptoms: ["uncaught exception: unbound method _pack_target__init__() must be called with _PackTargetMethods instance as first argument (got Session instance instead)"]
symptom_regex: "uncaught\\s+exception:\\s+unbound\\s+method\\s+_pack_target__init__\\(\\)\\s+must\\s+be\\s+called\\s+with\\s+_PackTargetMethods\\s+instance\\s+as\\s+first\\s+argument\\s+\\(got\\s+Session\\s+instance\\s+instead\\)"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/634"
doc_source: "https://github.com/pyocd/pyOCD/issues/634"
resolution: "fixed-in-release"
versions: "development build 0.19.1.dev"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["STM32F401RETx"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`uncaught exception: unbound method _pack_target__init__() must be called with _PackTargetMethods instance as first argument (got Session instance instead)`

## Cause

The pack-target code dynamically built methods in a way that works only on Python 3; on Python 2.7 the bound-method check fails. A typo (isinstane) was also found in the pack target module.

## Fix

Use Python 3 (the maintainer recommends 3.7) or a pyOCD build with the fix.

## Source

Resolution: fixed-in-release

Versions: development build 0.19.1.dev

From [pyocd/pyOCD #634](https://github.com/pyocd/pyOCD/issues/634), summarized in own words; confidence medium, not reviewed yet.
