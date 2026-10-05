---
id: "txmw-chapter-3-functional-components-of-local-default-path"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional components of FileX: **FAT12/16/32 Directory Description** / Local Default Path"
summary: "Part of: FAT12/16/32 Directory Description"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/filex/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/filex/chapter3.md#local-default-path"
license: "MIT"
mode: "V"
---

_Part of: **FAT12/16/32 Directory Description**_

FileX also provides a thread-specific default path that allows different threads to have unique paths without conflict. The **FX_LOCAL_PATH** structure is supplied  by the application during calls to ***fx_directory_local_path_set*** and ***fx_directory_local_path_restore*** to modify the local path for the calling thread.

If a local path is present, the local path takes precedence over the global default media path. If the local path is not setup or if it is cleared with the ***fx_directory_local_path_clear*** service, the media's global default path is used once again.
