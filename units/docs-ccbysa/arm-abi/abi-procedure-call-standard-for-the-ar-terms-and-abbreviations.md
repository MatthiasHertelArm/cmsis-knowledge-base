---
id: "abi-procedure-call-standard-for-the-ar-terms-and-abbreviations"
type: "concept"
domain: "core"
title: "Procedure Call Standard for the Arm® Architecture: About This Document / Terms and Abbreviations"
summary: "This document uses the following terms and abbreviations."
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:aapcs32/aapcs32.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/aapcs32/aapcs32.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: About This Document_

This document uses the following terms and abbreviations.

ABI
   Application Binary Interface:

   1. The specifications to which an executable must conform in order to
      execute in a specific execution environment. For example, the
      `Linux ABI for the Arm Architecture`.

   2. A particular aspect of the specifications to which independently
      produced relocatable files must conform in order to be statically
      linkable and executable. For example, the C++ ABI for the Arm
      Architecture [CPPABI32_], the Run-time ABI for the Arm Architecture
      [RTABI32_], the C Library ABI for the Arm Architecture [CLIBABI32_].

Arm-based
   based on the Arm architecture

EABI
   An ABI suited to the needs of embedded (sometimes called
   **free standing**) applications.

PCS
   Procedure Call Standard.

AAPCS
   Procedure Call Standard for the Arm Architecture (this standard).

APCS
   Arm Procedure Call Standard (obsolete).

TPCS
   Thumb Procedure Call Standard (obsolete).

ATPCS
   Arm-Thumb Procedure Call Standard (precursor to this standard).

PIC / PID
   Position-independent code, position-independent data.

Routine / subroutine
   A fragment of program to which control can be transferred that, on
   completing its task, returns control to its caller at an instruction
   following the call.  **Routine** is used for clarity where
   there are nested calls: a routine is the **caller** and a
   subroutine is the **callee**.

Procedure
   A routine that returns no result value.

Function
   A routine that returns a result value.

Activation stack / call-frame stack
   The stack of routine activation records (call frames).

Activation record / call frame
   The memory used by a routine for saving registers and holding local
   variables (usually allocated on a stack, once per activation of the
   routine).

Argument / Parameter
   The terms **argument** and **parameter** are used
   interchangeably. They may denote a formal parameter of a routine given
   the value of the actual parameter when the routine is called, or an
   actual parameter, according to context.

Externally visible [interface]
   [An interface] between separately compiled or separately assembled
   routines.

Variadic routine
   A routine is variadic if the number of arguments it takes, and their
   type, is determined by the caller instead of the callee.

Global register
   A register whose value is neither saved nor destroyed by a subroutine.
   The value may be updated, but only in a manner defined by the
   execution environment.

Program state
   The state of the program’s memory, including values in machine
   registers.

Scratch register / temporary register
   A register used to hold an intermediate value during a calculation
   (usually, such values are not named in the program source and have a
   limited lifetime).

Thumb-1
   The variant of the Thumb instruction set introduced in Arm v4T
   and used in Arm v6-M and the Arm v8-M.Baseline variants of the
   architecture.  It consists of instructions that are
   predominantly encoded with 16-bit opcodes.

Thumb-2
   The variant of the Thumb instruction set introduced in Arm v6T2.
   It consists of a mix of instructions encoded with 16- and 32-bit
   opcodes.

Variable register / v-register
   A register used to hold the value of a variable, usually one local to
   a routine, and often named in the source code.

More specific terminology is defined when it is first used.
