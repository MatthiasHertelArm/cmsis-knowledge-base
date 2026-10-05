---
id: "txmw-chapter-2-installation-and-use-of-filex-version-id"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and use of FileX: FileX Version ID"
summary: "The current version of FileX is available both to the user and the application software during run-time. The programmer can obtain the FileX version from examination of the fx_port.h file."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/filex/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/filex/chapter2.md#filex-version-id"
license: "MIT"
mode: "V"
---

The current version of FileX is available both to the user and the application software during run-time. The programmer can obtain the FileX version from examination of the **fx_port.h** file. In addition, this file also contains a version history of the corresponding port. Application software can obtain the FileX version by examining the global string ***_fx_version_id***.
