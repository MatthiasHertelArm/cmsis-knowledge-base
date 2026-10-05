---
id: "iss-pyocd-1396"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: GD32 flashing fails with Memory transfer fault and SVD load ParseError"
summary: "The pack's SVD file failed to parse (the XML declaration was not at the start of the file); another user found that all SVDs of GigaDevice.GD32F30x_DFP 2.2.0 had whitespace before the XML declaration."
status: "draft"
tool: "pyocd"
symptoms: ["xml.etree.ElementTree.ParseError: XML or text declaration not at start of entity: line 1, column 2", "C Memory transfer fault @ 0x08000000-0x0800001f [__main__]"]
symptom_regex: "xml\\.etree\\.ElementTree\\.ParseError:\\s+XML\\s+or\\s+text\\s+declaration\\s+not\\s+at\\s+start\\s+of\\s+entity:\\s+line\\s+\\S+,\\s+column\\s+\\S+"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1396"
doc_source: "https://github.com/pyocd/pyOCD/issues/1396"
resolution: "workaround"
versions: "pyocd 0.33.1; GigaDevice GD32F3x0_DFP 2.0.0"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["GD32F350G8"], "core": ["Cortex-M4"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`xml.etree.ElementTree.ParseError: XML or text declaration not at start of entity: line 1, column 2`
`C Memory transfer fault @ 0x08000000-0x0800001f [__main__]`

## Cause

The pack's SVD file failed to parse (the XML declaration was not at the start of the file); another user found that all SVDs of GigaDevice.GD32F30x_DFP 2.2.0 had whitespace before the XML declaration. The memory transfer fault at 0x08000000 was not explained: a built-in target with a hand-built memory map showed the same fault.

## Fix

Unpack the pack, fix the SVD files (strip the leading whitespace so the XML declaration starts the file), repack or pass the expanded folder with --pack, and report the issue to the vendor. This fixed the other user's pack; the reporter did not confirm it.

## Source

Resolution: workaround

Versions: pyocd 0.33.1; GigaDevice GD32F3x0_DFP 2.0.0

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1396](https://github.com/pyocd/pyOCD/issues/1396), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
