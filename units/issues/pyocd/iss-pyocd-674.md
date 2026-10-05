---
id: "iss-pyocd-674"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pip install pyocd 0.21.0 fails because cmsis-pack-manager has no build for the platform"
summary: "pyOCD 0.20 and later require cmsis-pack-manager, which contains compiled Rust code."
status: "draft"
tool: "pyocd"
symptoms: ["ERROR: Could not find a version that satisfies the requirement cmsis-pack-manager>=0.2.7 (from pyocd) (from versions: 0.1.0)", "ERROR: No matching distribution found for cmsis-pack-manager>=0.2.7 (from pyocd)"]
symptom_regex: "Could\\s+not\\s+find\\s+a\\s+version\\s+that\\s+satisfies\\s+the\\s+requirement\\s+cmsis\\-pack\\-manager>=\\S+\\s+\\(from\\s+pyocd\\)\\s+\\(from\\s+versions:\\s+\\S+\\)"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/674"
doc_source: "https://github.com/pyocd/pyOCD/issues/674"
resolution: "fixed-in-release"
versions: "pyocd 0.21.0 with cmsis-pack-manager below 0.2.8"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ERROR: Could not find a version that satisfies the requirement cmsis-pack-manager>=0.2.7 (from pyocd) (from versions: 0.1.0)`
`ERROR: No matching distribution found for cmsis-pack-manager>=0.2.7 (from pyocd)`

## Cause

pyOCD 0.20 and later require cmsis-pack-manager, which contains compiled Rust code. On platforms without a prebuilt wheel (FreeBSD, some ARM hosts) pip could only see an old source version and the install failed.

## Fix

Install an older pyOCD such as `pip install pyocd==0.19.0`, or wait for or upgrade to cmsis-pack-manager 0.2.8 or newer, which builds with stable Rust.

## Source

Resolution: fixed-in-release

Versions: pyocd 0.21.0 with cmsis-pack-manager below 0.2.8

From [pyocd/pyOCD #674](https://github.com/pyocd/pyOCD/issues/674), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
