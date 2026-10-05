---
id: "threadx-chapter-2-installation-use-of-thre-product-distribution"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation & Use of ThreadX SMP: Product Distribution"
summary: "The exact content of the distribution disk depends on the target processor, development tools, and the ThreadX SMP package purchased. However, the following is a list of several important files that are common to most product distributions:"
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/threadx-smp/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/threadx-smp/chapter2.md#product-distribution"
license: "MIT"
mode: "V"
---

The exact content of the distribution disk depends on the target processor, development tools, and the ThreadX SMP package purchased. However, the following is a list of several important files that are common to most product distributions:

### ThreadX_Express_Startup.pdf

This PDF provides a simple, four-step procedure to get ThreadX SMP running on a specific target processor/board and specific development tools.

### readme_threadx.txt

Text file containing specific information about the ThreadX SMP port, including information about the target processor and the development tools.

| Tool | Description |
| -------------- | ------------------------------------------------------------------------------------------------- |
| **tx_api.h**  | C header file containing all system equates, data structures, and service prototypes.             |
| **tx_port.h** | C header file containing all development-tool and target specific data definitions and structures. |
|**demo_threadx.c**| C file containing a small demo application.|
|**tx.a (or tx.lib)**| Binary version of the ThreadX SMP C library that is distributed with the *standard* package.|

> **Important:** All file names are in lower-case. This naming convention makes it easier to convert the commands to Linux (Unix) development platforms.
