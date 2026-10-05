---
id: "txmw-chapter-1-introduction-to-filex-powerful-services-of-filex"
type: "concept"
domain: "rtos"
title: "Chapter 1 - Introduction to FileX: Powerful Services of FileX"
summary: "FileX can support an unlimited number of physical media. Each media instance has its own distinct memory area and associated driver specified on the fx_media_open call."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/filex/chapter1.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/filex/chapter1.md#powerful-services-of-filex"
license: "MIT"
mode: "V"
---

### Multiple Media Management

FileX can support an unlimited number of physical media. Each media instance has its own distinct memory area and associated driver specified on the **_fx_media_open_** call. The default distribution of FileX comes with a simple RAM media driver and a demonstration system that uses this RAM disk.

### Logical Sector Cache

By reducing the number of whole sector transfers, both to and from the media, the FileX logical sector cache significantly improves performance. FileX maintains a logical sector cache for each opened media. The depth of the logical sector cache is determined by the amount of memory supplied to FileX with the **_fx_media_open_** API call.

### Contiguous File Support

FileX offers contiguous file support through the API service **_fx_file_allocate_** to improve and make file access time deterministic. This routine takes the amount of memory requested and looks for a series of adjacent clusters to satisfy the request. If such clusters are found, they are pre-allocated by making them part of the file's chain of allocated clusters. On moving physical media, the FileX contiguous file support results in a significant performance improvement and makes the access time deterministic.

### Dynamic Creation

FileX allows you to create system resources dynamically. This is especially important if your application has
multiple or dynamic configuration requirements. In addition, there are no predetermined limits on the number of FileX resources you can use (media or files). Also, the number of system objects does not have any
impact on performance.
