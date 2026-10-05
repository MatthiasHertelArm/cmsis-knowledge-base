---
id: "iss-pyocd-1023"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd on Raspberry Pi: DistributionNotFound for cmsis-pack-manager after --no-deps install"
summary: "pyocd's entry-point loading still requires cmsis-pack-manager, which has no prebuilt wheel for ARM and needs Rust to build, so the documented --no-deps route no longer works."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1023"
doc_source: "https://github.com/pyocd/pyOCD/issues/1023"
resolution: "workaround"
versions: "pyOCD 0.29, ARM Linux (Raspberry Pi, aarch64)"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

pyocd's entry-point loading still requires cmsis-pack-manager, which has no prebuilt wheel for ARM and needs Rust to build, so the documented --no-deps route no longer works.

## Fix

Build and install cmsis-pack-manager from source on the device first (Rust toolchain and system packages needed), then install pyocd. Expect Rust-version build breakage; the non-x86 install document was outdated.

## Source

Resolution: workaround

Versions: pyOCD 0.29, ARM Linux (Raspberry Pi, aarch64)

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1023](https://github.com/pyocd/pyOCD/issues/1023), summarized in own words; confidence low, not reviewed yet.
