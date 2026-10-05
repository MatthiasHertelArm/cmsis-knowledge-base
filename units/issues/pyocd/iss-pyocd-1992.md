---
id: "iss-pyocd-1992"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd pack install silently installs nothing when index and pdsc versions differ"
summary: "The pack index lists one version of the pack, but the vendor's pdsc file lists a newer release first. pyOCD builds its index from the newest release, then looks for a cached pdsc under that version name, which does …"
status: "draft"
tool: "pyocd"
symptoms: ["Target type mimxrt1171dvmab not recognized. Use 'pyocd list --targets' to see currently available target types."]
symptom_regex: "Target\\s+type\\s+mimxrt1171dvmab\\s+not\\s+recognized\\.\\s+Use\\s+'.*?'\\s+to\\s+see\\s+currently\\s+available\\s+target\\s+types\\."
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1992"
doc_source: "https://github.com/pyocd/pyOCD/issues/1992"
resolution: "workaround"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"], "device": ["MIMXRT1171DVMAB"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Target type mimxrt1171dvmab not recognized. Use 'pyocd list --targets' to see currently available target types.`

## Cause

The pack index lists one version of the pack, but the vendor's pdsc file lists a newer release first. pyOCD builds its index from the newest release, then looks for a cached pdsc under that version name, which does not exist, so the pack download never starts and no error is shown. Several NXP packs were non-compliant with the pack schema.

## Fix

Download the pack file yourself in the version the index really offers and pass it directly, for example: pyocd flash --target MIMXRT1171DVMAB --pack=NXP.MIMXRT1171_DFP.25.12.00.pack <image>. The vendor was fixing the metadata for its next pack release.

## Source

Resolution: workaround

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1992](https://github.com/pyocd/pyOCD/issues/1992), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
