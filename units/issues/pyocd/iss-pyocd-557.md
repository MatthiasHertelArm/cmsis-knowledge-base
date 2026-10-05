---
id: "iss-pyocd-557"
type: "troubleshooting"
domain: "general"
title: "other: objcopy 8-2018-q4 on Windows: address out of range for Intel Hex"
summary: "A bug in the Windows build of the GNU Arm Embedded 8-2018-q4-major toolchain breaks binary to ihex conversion; Mac and Linux builds were fine."
status: "draft"
tool: "other"
symptoms: ["arm-none-eabi-objcopy: c:\\Temp\\<elfFile> 64-bit address 0x4b4fa300000000 out of range for Intel Hex file"]
symptom_regex: "arm\\-none\\-eabi\\-objcopy:\\s+c:\\\\Temp\\\\<elfFile>\\s+\\S+\\-bit\\s+address\\s+\\S+\\s+out\\s+of\\s+range\\s+for\\s+Intel\\s+Hex\\s+file"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/557"
doc_source: "https://github.com/pyocd/pyOCD/issues/557"
resolution: "workaround"
versions: "GNU Arm Embedded 8-2018-q4-major, Windows"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd", "gdb"], "toolchain": ["GCC"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`arm-none-eabi-objcopy: c:\Temp\<elfFile> 64-bit address 0x4b4fa300000000 out of range for Intel Hex file`

## Cause

A bug in the Windows build of the GNU Arm Embedded 8-2018-q4-major toolchain breaks binary to ihex conversion; Mac and Linux builds were fine.

## Fix

Use an earlier release (7-2018-q2-update or 7-2017-q4-major) or a toolchain build that contains the fix (GNU MCU Eclipse 8.2.1-1.2).

## Source

Resolution: workaround

Versions: GNU Arm Embedded 8-2018-q4-major, Windows

From [pyocd/pyOCD #557](https://github.com/pyocd/pyOCD/issues/557), summarized in own words; confidence high, checked against the thread, not reviewed yet.
