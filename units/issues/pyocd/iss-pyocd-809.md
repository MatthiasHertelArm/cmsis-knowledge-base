---
id: "iss-pyocd-809"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pip install pyocd fails in a virtualenv while building cmsis-pack-manager"
summary: "pip 20.0/20.0.1 broke the build of the cmsis-pack-manager source package inside virtual environments."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/809"
doc_source: "https://github.com/pyocd/pyOCD/issues/809"
resolution: "fixed-in-release"
versions: "pip 20.0 and 20.0.1"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

pip 20.0/20.0.1 broke the build of the cmsis-pack-manager source package inside virtual environments.

## Fix

Use pip 20.0.2 or newer (downgrading to pip below 20 also worked).

## Source

Resolution: fixed-in-release

Versions: pip 20.0 and 20.0.1

From [pyocd/pyOCD #809](https://github.com/pyocd/pyOCD/issues/809), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
