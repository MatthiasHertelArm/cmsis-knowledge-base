---
id: "abi-procedure-call-standard-for-the-ar-the-base-procedure-call-standard"
type: "concept"
domain: "core"
title: "Procedure Call Standard for the Arm® Architecture: The Base Procedure Call Standard"
summary: "The base standard defines a machine-level, core-registers-only calling standard common to the Arm and Thumb instruction sets."
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:aapcs32/aapcs32.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/aapcs32/aapcs32.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

The base standard defines a machine-level, core-registers-only calling
standard common to the Arm and Thumb instruction sets.  It should be used
for systems where there is no floating-point hardware, or where a high
degree of inter-working with Thumb code is required.
