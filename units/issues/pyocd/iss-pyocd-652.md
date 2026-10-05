---
id: "iss-pyocd-652"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd list --targets fails with BadZipFile after a broken pack index download"
summary: "cmsis-pack-manager constructed a wrong download URL for packs whose URL lacked a trailing slash (ARMmbed/cmsis-pack-manager#95), so the downloaded pack was garbage and reading it ended in the BadZipFile AttributeError, which the maintainer still had to investigate."
status: "draft"
tool: "pyocd"
symptoms: ["uncaught exception: 'module' object has no attribute 'BadZipFile'"]
symptom_regex: "uncaught\\s+exception:\\s+'.*?'\\s+object\\s+has\\s+no\\s+attribute\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/652"
doc_source: "https://github.com/pyocd/pyOCD/issues/652"
resolution: "workaround"
versions: "Python 2.7.15rc1; Keil.STM32L4xx_DFP 2.2.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`uncaught exception: 'module' object has no attribute 'BadZipFile'`

## Cause

cmsis-pack-manager constructed a wrong download URL for packs whose URL lacked a trailing slash (ARMmbed/cmsis-pack-manager#95), so the downloaded pack was garbage and reading it ended in the BadZipFile AttributeError, which the maintainer still had to investigate.

## Fix

Update cmsis-pack-manager once the release with the fix is out; pyocd pack --clean removes the error but also the pack. Meanwhile download the pack manually and pass it with --pack (e.g. pyocd gdbserver --pack <file>) or list it under pack: in pyocd.yaml.

## Source

Resolution: workaround

Versions: Python 2.7.15rc1; Keil.STM32L4xx_DFP 2.2.0

From [pyocd/pyOCD #652](https://github.com/pyocd/pyOCD/issues/652), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
