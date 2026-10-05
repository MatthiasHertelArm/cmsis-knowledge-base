---
id: "txmw-chapter-3-functional-components-of-root-directory"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional components of FileX: **FAT12/16/32 Directory Description** / Root Directory"
summary: "Part of: FAT12/16/32 Directory Description"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/filex/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/filex/chapter3.md#root-directory"
license: "MIT"
mode: "V"
---

_Part of: **FAT12/16/32 Directory Description**_

In FAT 12- and 16-bit formats, the *root directory* is located immediately after all the FAT sectors in the media and can be located by examining the ***fx_media_root_sector_start*** in an opened **FX_MEDIA** control block. The size of the root directory, in terms of number of directory entries (each 32 bytes in size), is determined by the corresponding entry in the media's boot record.

The root directory in FAT-32 can be located anywhere in the available clusters. Its location and size are determined from the boot record when the media is opened. After the media is opened, the ***fx_media_root_sector_start*** field can be used to find the starting cluster of the FAT-32 root directory.
