---
id: "txmw-chapter-3-functional-components-of-global-default-path"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional components of FileX: **FAT12/16/32 Directory Description** / Global Default Path"
summary: "Part of: FAT12/16/32 Directory Description"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/filex/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/filex/chapter3.md#global-default-path"
license: "MIT"
mode: "V"
---

_Part of: **FAT12/16/32 Directory Description**_

FileX provides a global default path for the media. The default path is used in any file or directory service that does not explicitly specify a full path.

Initially, the global default directory is set to the media's root directory. This may be changed by the application by calling ***fx_directory_default_set***.

The current default path for the media may be examined by calling ***fx_directory_default_get***. This routine provides a string pointer to the default path string maintained inside of the **FX_MEDIA** control block.
