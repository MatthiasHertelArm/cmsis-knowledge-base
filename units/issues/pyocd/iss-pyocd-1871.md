---
id: "iss-pyocd-1871"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: CMSIS-DAP v2 bulk: stray zero byte after transfers sized as multiple of endpoint size"
summary: "pyOCD's USB backend appends a dummy zero byte to bulk writes whose length is a multiple of wMaxPacketSize but shorter than the DAP packet size, to terminate the transfer."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1871"
doc_source: "https://github.com/pyocd/pyOCD/issues/1871"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

pyOCD's USB backend appends a dummy zero byte to bulk writes whose length is a multiple of wMaxPacketSize but shorter than the DAP packet size, to terminate the transfer. Probe firmware that treats every byte as data sees a bogus one-byte packet.

## Fix

The extra byte was introduced on purpose to end the USB transfer; a later change (#1882) altered it so it no longer shows up in the command stream. Update pyOCD or make probe firmware tolerate it.

## Source

Resolution: fixed-in-release

From [pyocd/pyOCD #1871](https://github.com/pyocd/pyOCD/issues/1871), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
