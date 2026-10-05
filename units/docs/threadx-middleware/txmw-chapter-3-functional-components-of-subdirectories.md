---
id: "txmw-chapter-3-functional-components-of-subdirectories"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional components of FileX: **FAT12/16/32 Directory Description** / Subdirectories"
summary: "Part of: FAT12/16/32 Directory Description"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/filex/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/filex/chapter3.md#subdirectories"
license: "MIT"
mode: "V"
---

_Part of: **FAT12/16/32 Directory Description**_

There is any number of subdirectories in an FAT system. The name of the subdirectory resides in a directory entry just like a file name. However, the directory attribute specification (0x10) is set to indicate the entry is a subdirectory and the file size is always zero.
Figure 3 shows what a typical subdirectory structure looks like for a new singlecluster subdirectory named ***SAMPLE.DIR*** with one file called ***FILE.TXT***.
In most ways, subdirectories are very similar to file entries. The first cluster field points to the first cluster of a linked list of clusters. When a subdirectory is created, the first two directory entries contain default directories, namely the "." directory and the ".." directory. The "." directory points to the subdirectory itself, while the ".." directory points to the previous or parent directory.
