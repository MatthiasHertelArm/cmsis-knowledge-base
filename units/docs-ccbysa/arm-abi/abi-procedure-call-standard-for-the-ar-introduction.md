---
id: "abi-procedure-call-standard-for-the-ar-introduction"
type: "concept"
domain: "core"
title: "Procedure Call Standard for the Arm® Architecture: Introduction"
summary: "The AAPCS embodies the fifth major revision of the APCS and third major revision of the TPCS. It forms part of the complete ABI specification for the Arm Architecture."
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:aapcs32/aapcs32.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/aapcs32/aapcs32.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

The AAPCS embodies the fifth major revision of the APCS and third major
revision of the TPCS. It forms part of the complete ABI specification for
the Arm Architecture.


### Design Goals


The goals of the AAPCS are to:

*  Support Thumb-state and Arm-state equally.

*  Support inter-working between Thumb-state and Arm-state.

*  Support efficient execution on high-performance implementations of the
   Arm Architecture.

*  Clearly distinguish between mandatory requirements and implementation
   discretion.

*  Minimize the binary incompatibility with the ATPCS.


### Conformance


The AAPCS defines how separately compiled and separately assembled routines
can work together. There is an **externally visible interface**
between such routines.  It is common that not all the externally visible
interfaces to software are intended to be **publicly visible** or
open to arbitrary use. In effect, there is a mismatch between the
machine-level concept of external visibility—defined rigorously by an object
code format—and a **higher level**, application-oriented concept of
external visibility—which is system-specific or application-specific.

Conformance to the AAPCS requires that\ [#aapcs32-f1]_:

*  At all times, stack limits and basic stack alignment are observed
   (Universal stack constraints).

*  At each call where the control transfer instruction is subject to a
   BL-type relocation at static link time, rules on the use of IP are
   observed (Use of IP by the linker).

*  The routines of each publicly visible interface conform to the relevant
   procedure call standard variant.

*  The data elements\ [#aapcs32-f2]_ of each publicly visible interface
   conform to the data layout rules.
