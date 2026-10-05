---
id: "iss-pyocd-1396"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: GD32 flashing fails with Memory transfer fault and SVD load ParseError"
summary: "GigaDevice packs had SVD files with whitespace before the XML declaration, which pyOCD's strict parser rejects."
status: "draft"
tool: "pyocd"
symptoms: ["xml.etree.ElementTree.ParseError: XML or text declaration not at start of entity: line 1, column 2", "C Memory transfer fault @ 0x08000000-0x0800001f [__main__]"]
symptom_regex: "xml\\.etree\\.ElementTree\\.ParseError:\\s+XML\\s+or\\s+text\\s+declaration\\s+not\\s+at\\s+start\\s+of\\s+entity:\\s+line\\s+\\S+,\\s+column\\s+\\S+"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1396"
doc_source: "https://github.com/pyocd/pyOCD/issues/1396"
resolution: "workaround"
versions: "pyocd 0.33.1"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["GD32F350G8"], "core": ["Cortex-M4"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`xml.etree.ElementTree.ParseError: XML or text declaration not at start of entity: line 1, column 2`
`C Memory transfer fault @ 0x08000000-0x0800001f [__main__]`

## Cause

GigaDevice packs had SVD files with whitespace before the XML declaration, which pyOCD's strict parser rejects. A built-in target with a hand-built memory map showed the same fault, so this may not be the only cause.

## Fix

Unpack the pack, fix the SVD files (strip leading whitespace so the XML declaration starts the file), repack or pass the folder with --pack, and report the issue to the vendor.

## Source

Resolution: workaround

Versions: pyocd 0.33.1

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1396](https://github.com/pyocd/pyOCD/issues/1396), summarized in own words; confidence low, not reviewed yet.
