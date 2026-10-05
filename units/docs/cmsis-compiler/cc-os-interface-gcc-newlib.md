---
id: "cc-os-interface-gcc-newlib"
type: "concept"
domain: "core"
title: "OS Interface: GCC Newlib"
summary: "\\include /osinterface/gcc/retargetlock.c"
status: "draft"
collection: "cmsis-compiler"
source: "ARM-software/CMSIS-Compiler@8cdaa0a:documentation/doxygen/src/templates_os.md"
doc_source: "https://github.com/ARM-software/CMSIS-Compiler/blob/8cdaa0a/documentation/doxygen/src/templates_os.md#gcc-newlib"
license: "Apache-2.0"
mode: "V"
---

**Code template used to retarget locking routines**

\include /os_interface/gcc/retarget_lock.c

**Code template used to retarget system calls**

> **Note**
> - All system call functions are provided in this template although there may not be necessary to reimplement them all. Functions that are not necessary may be removed or kept depending on the linker settings.
> - Reimplementing functions like `_open`, `_close`,` _write`, etc. breaks compatibility with the CMSIS-Compiler:IO component. Make sure to remove them from custom implementation when application does not require to reimplement them.

\include /os_interface/gcc/retarget_syscalls.c
