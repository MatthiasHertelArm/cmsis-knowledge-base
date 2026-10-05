---
id: "iss-pyocd-189"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: External nRF51 board cannot be flashed through an nRF51-DK running mbed interface firmware"
summary: "The CMSIS-DAP firmware only drives the SWD pins to the on-board chip; the Debug Out header is not selected."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/189"
doc_source: "https://github.com/pyocd/pyOCD/issues/189"
resolution: "not-a-bug"
versions: "2015"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "family": ["nRF51 Series"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The CMSIS-DAP firmware only drives the SWD pins to the on-board chip; the Debug Out header is not selected.

## Fix

Use an interface firmware that supports Debug Out switching, or a separate probe wired to the external target.

## Source

Resolution: not-a-bug

Versions: 2015

From [pyocd/pyOCD #189](https://github.com/pyocd/pyOCD/issues/189), summarized in own words; confidence medium, not reviewed yet.
