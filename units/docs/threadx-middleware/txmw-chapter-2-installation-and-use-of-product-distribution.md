---
id: "txmw-chapter-2-installation-and-use-of-product-distribution"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and use of FileX: Product Distribution"
summary: "FileX can be obtained from our public source code repository at <https://github.com/eclipse-threadx/filex/>."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/filex/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/filex/chapter2.md#product-distribution"
license: "MIT"
mode: "V"
---

FileX can be obtained from our public source code repository at <https://github.com/eclipse-threadx/filex/>.

The following is a list of several important files in the repository:

- ***fx_api.h*** : This C header file contains all system equates, data structures, and service prototypes.
- ***fx_port.h*** : This C header file contains all development-tool-specific data definitions and structures.
- ***demo_filex.c*** : This C file contains a small demo application.
- ***fx.a (or fx.lib)*** : This is the binary version of the FileX C library. It is distributed with the standard package.

> **Important:** *All file names are in lower-case. This naming convention makes it easier to convert the commands to Linux (Unix) development platforms.*
