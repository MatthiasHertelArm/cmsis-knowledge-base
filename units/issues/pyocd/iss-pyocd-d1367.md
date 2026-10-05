---
id: "iss-pyocd-d1367"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Adding an external RTOS or probe driver to pyOCD without editing its sources"
summary: "pyOCD loads its probe drivers and RTOS awareness modules as setuptools entry points, so out-of-tree packages can register themselves."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/discussions/1367"
doc_source: "https://github.com/pyocd/pyOCD/discussions/1367"
resolution: "configuration"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

pyOCD loads its probe drivers and RTOS awareness modules as setuptools entry points, so out-of-tree packages can register themselves.

## Fix

Create a Python package that exports an entry point in the group pyocd.rtos or pyocd.probe. The entry point must reference a subclass of pyocd.core.plugin.Plugin whose load() returns the implementation (a ThreadProvider subclass for an RTOS). The built-in FreeRTOS plugin and the entry_points section of pyOCD's setup.cfg are the reference.

## Source

Resolution: configuration

From [pyocd/pyOCD discussion 1367](https://github.com/pyocd/pyOCD/discussions/1367), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
