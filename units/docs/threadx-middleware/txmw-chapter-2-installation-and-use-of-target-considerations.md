---
id: "txmw-chapter-2-installation-and-use-of-target-considerations"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and use of FileX: Target Considerations"
summary: "FileX requires between 6 KBytes and 30 KBytes of Read-Only Memory (ROM) on the target. Another 100 bytes of the target's Random Access Memory (RAM) are required for FileX global data structures."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/filex/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/filex/chapter2.md#target-considerations"
license: "MIT"
mode: "V"
---

FileX requires between 6 KBytes and 30 KBytes of  Read-Only Memory (ROM) on the target. Another  100 bytes of the target's Random Access Memory (RAM) are required for FileX global data structures. Each opened media also requires 1.5 KBytes of RAM for the control block in addition to RAM for storing data for one sector (typically 512 bytes).

For date/time stamping to function properly, FileX relies on ThreadX timer facilities. This is implemented by creating a FileX-specific timer during FileX initialization. FileX also relies on ThreadX semaphores for multiple thread protection and I/O suspension.
