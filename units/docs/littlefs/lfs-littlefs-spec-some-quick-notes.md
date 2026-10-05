---
id: "lfs-littlefs-spec-some-quick-notes"
type: "concept"
domain: "project"
title: "littlefs SPEC: Some quick notes"
summary: "littlefs SPEC: Some quick notes"
status: "draft"
collection: "littlefs"
source: "littlefs-project/littlefs@6cb4e86:SPEC.md"
doc_source: "https://github.com/littlefs-project/littlefs/blob/6cb4e86/SPEC.md#some-quick-notes"
license: "BSD-3-Clause"
mode: "V"
---

- littlefs is a block-based filesystem. The disk is divided into an array of
  evenly sized blocks that are used as the logical unit of storage.

- Block pointers are stored in 32 bits, with the special value `0xffffffff`
  representing a null block address.

- In addition to the logical block size (which usually matches the erase
  block size), littlefs also uses a program block size and read block size.
  These determine the alignment of block device operations, but don't need
  to be consistent for portability.

- By default, all values in littlefs are stored in little-endian byte order.
