---
id: "cc-low-level-i-o-retarget"
type: "concept"
domain: "core"
title: "Low-Level I/O Retarget"
summary: "CMSIS-Compiler splits low-level I/O retargeting into standard I/O stream related components and file stream related components."
status: "draft"
collection: "cmsis-compiler"
source: "ARM-software/CMSIS-Compiler@8cdaa0a:documentation/doxygen/src/rt_io.md"
doc_source: "https://github.com/ARM-software/CMSIS-Compiler/blob/8cdaa0a/documentation/doxygen/src/rt_io.md"
license: "Apache-2.0"
mode: "V"
---

CMSIS-Compiler splits low-level I/O retargeting into **standard I/O stream** related components and **file stream** related components.

The low-level I/O retarget decision tree is shown below:

(figure: Low-Level I/O Retarget Decision Tree)

Low-Level I/O retargeting implementation checks whether the incoming stream is a standard stream (i.e. stderr, stdin, stdout) or a file system related stream and redirects incoming request to the appropriate software component. Chapters rt_io_components and rt_file_interface explain these software components in detail.
