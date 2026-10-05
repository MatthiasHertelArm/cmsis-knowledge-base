---
id: "abi-procedure-call-standard-for-the-ar-argument-passing-conventions"
type: "concept"
domain: "core"
title: "Procedure Call Standard for the Arm® Architecture: Arm C and C++ Language Mappings / Argument Passing Conventions"
summary: "Part of: Arm C and C++ Language Mappings"
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:aapcs32/aapcs32.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/aapcs32/aapcs32.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Arm C and C++ Language Mappings_

The argument list for a subroutine call is formed by taking the user
arguments in the order in which they are specified.

*  For C, each argument is formed from the value specified in the source
   code, except that an array is passed by passing the address of its first
   element.

*  For C++, an implicit `this` parameter is passed as an extra argument
   that immediately precedes the first user argument. Other rules for
   marshalling C++ arguments are described in CPPABI32_.

*  For variadic functions, `float` arguments that match the ellipsis
   (...) are converted to type `double`.

The argument list is then processed according to the standard rules for
procedure calls (see Parameter Passing (base PCS)) or the appropriate
variant.
