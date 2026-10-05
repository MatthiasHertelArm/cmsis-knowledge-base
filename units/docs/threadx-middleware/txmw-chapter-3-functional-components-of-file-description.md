---
id: "txmw-chapter-3-functional-components-of-file-description"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional components of FileX: File Description"
summary: "FileX supports standard 8.3 character and long file names with three-character extensions."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/filex/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/filex/chapter3.md#file-description"
license: "MIT"
mode: "V"
---

FileX supports standard 8.3 character and long file names with three-character extensions. In addition to the ASCII name, each file entry contains the entry's attributes, the last modified time and date, the starting cluster index, and the size in bytes of the entry.

### File Allocation

FileX supports the standard cluster allocation scheme of the FAT format. In addition, FileX supports pre-cluster allocation of contiguous clusters. To accommodate this, each FileX file is created with no allocated clusters. Clusters are allocated on subsequent write requests or on ***fx_file_allocate*** requests to pre-allocate contiguous clusters.

Figure 4, "FileX FAT-16 File Example," shows a file named ***FILE.TXT*** with two sequential clusters allocated starting at cluster 101, a size of 26, and the alphabet as the data in the file's first data cluster number 101.

### File Access

A FileX file may be opened multiple times simultaneously for read access. However, a file can only be opened once for writing. The information used to support the file access is contained in the ***FX_FILE*** file control block.

> **Note:** *Note that the media driver can dynamically set write protection. If this happens all write requests are rejected as well as attempts to open a file for writing.*
