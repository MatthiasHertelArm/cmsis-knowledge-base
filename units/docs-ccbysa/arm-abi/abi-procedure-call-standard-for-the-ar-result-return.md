---
id: "abi-procedure-call-standard-for-the-ar-result-return"
type: "concept"
domain: "core"
title: "Procedure Call Standard for the Arm® Architecture: The Base Procedure Call Standard / Result Return"
summary: "Part of: The Base Procedure Call Standard"
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:aapcs32/aapcs32.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/aapcs32/aapcs32.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: The Base Procedure Call Standard_

The manner in which a result is returned from a function is determined by the
type of that result.

For the base standard:

*  A Half-precision Floating Point Type is returned in the least significant
   16 bits of r0.

*  A Fundamental Data Type that is smaller than 4 bytes is zero- or
   sign-extended to a word and returned in r0.

*  A word-sized Fundamental Data Type (e.g., `int`, `float`) is
   returned in r0.

*  A double-word sized Fundamental Data Type (e.g., `long long`,
   `double` and 64-bit containerized vectors) is returned in r0 and r1.

*  A 128-bit containerized vector is returned in r0-r3.

*  A Composite Type not larger than 4 bytes is returned in r0.  The format
   is as if the result had been stored in memory at a word-aligned address
   and then loaded into r0 with an LDR instruction.  Any bits in r0 that lie
   outside the bounds of the result have unspecified values.

*  A Composite Type larger than 4 bytes, or whose size cannot be determined
   statically by both caller and callee, is stored in memory at an address
   passed as an extra argument when the function was called
   (Parameter Passing (base PCS), Rule A.4). The
   memory to be used for the result may be modified at any point during the
   function call.

.. _Parameter Passing (base PCS):
