---
id: "cc-overview"
type: "concept"
domain: "core"
title: "Overview"
summary: "Application code frequently uses standard C library functions, such as fopen, fwrite, printf(), scanf() and others to perform input/output operations. These functions may as well be used in a multithreaded environment."
status: "draft"
collection: "cmsis-compiler"
source: "ARM-software/CMSIS-Compiler@8cdaa0a:documentation/doxygen/src/mainpage.md"
doc_source: "https://github.com/ARM-software/CMSIS-Compiler/blob/8cdaa0a/documentation/doxygen/src/mainpage.md"
license: "Apache-2.0"
mode: "V"
---

**CMSIS-Compiler** provides software components that simplify retargeting of standard C run-time library functions.

Application code frequently uses standard C library functions, such as `fopen`, `fwrite`, `printf()`, `scanf()` and others to perform input/output operations. These functions may as well be used in a multithreaded environment.

The structure of these functions in the standard C run-time library together with the retarget interfaces is:

(figure: Software Structure Overview)

Standard C library functions are platform independent and can be easily ported, while the low-level interfaces needs to be tailored to the chosen platform. Generally low-level I/O functions serve to interact with the file system and a serial interface, i.e. terminal. Multithreading support is available for applications that run on top of an RTOS kernel.

CMSIS-Compiler enables platform specific retargeting by providing software components that break down into the following interfaces:

- File interface that enables reading and writing files
- STDIN interface that enables standard input stream redirection
- STDOUT interface that enables standard output stream redirection
- STDERR interface that enables standard error stream redirection
- OS interface that enables multithread safety using an arbitrary RTOS

The pages rt_io and rt_os explain the details about how retargeting is done using the provided components.

Using CMSIS-Compiler developers can retarget standard I/O streams and file operations to specific platform and enable thread safe operations using RTOS interface.

> **Note**
> - CMSIS-Compiler replaces and extends retargeting functionality previously provided as part of *Keil::ARM_Compiler* pack.
> - See [Migrating projects from CMSIS v5 to CMSIS v6](https://learn.arm.com/learning-paths/microcontrollers/project-migration-cmsis-v6) for a guidance on updating existing projects to CMSIS-Compiler.
