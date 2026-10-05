---
id: "txmw-chapter-6-filex-fault-tolerant-mod-use-of-the-fault-tolerant-module"
type: "concept"
domain: "rtos"
title: "Chapter 6 - FileX fault tolerant module: Use of the Fault Tolerant Module"
summary: "The FileX Fault Tolerant feature is available to all FAT file systems supported by FileX, including FAT12, FAT16, and FAT32. To enable the fault tolerant feature, FileX must be built with the symbol FX_ENABLE_FAULT_TOLERANT defined."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/filex/chapter6.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/filex/chapter6.md#use-of-the-fault-tolerant-module"
license: "MIT"
mode: "V"
---

The FileX Fault Tolerant feature is available to all FAT file systems supported by FileX, including FAT12, FAT16, and FAT32. To enable the fault tolerant feature, FileX must be built with the symbol **FX_ENABLE_FAULT_TOLERANT** defined. At run time, application starts fault tolerant service by calling ***fx_fault_tolerant_enable*** immediately after the call to ***fx_media_open***. After fault tolerant is enabled, all file write operations to the designated media are protected. By default the fault tolerant module is not enabled.

> **Important:** *Application needs to make sure the file system is not being accessed prior to ***fx_fault_tolerant_enable*** being called. If application writes data to the file system prior to fault tolerant enable, the write operation could corrupt the media if prior write operations were not completed, and the file system was not restored using fault tolerant log entries.*
