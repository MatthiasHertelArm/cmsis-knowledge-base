---
id: "lfs-readme-other-notes"
type: "concept"
domain: "project"
title: "README: Other notes"
summary: "Littlefs is written in C, and specifically should compile with any compiler that conforms to the C99 standard."
status: "draft"
collection: "littlefs"
source: "littlefs-project/littlefs@6cb4e86:README.md"
doc_source: "https://github.com/littlefs-project/littlefs/blob/6cb4e86/README.md#other-notes"
license: "BSD-3-Clause"
mode: "V"
---

Littlefs is written in C, and specifically should compile with any compiler
that conforms to the `C99` standard.

All littlefs calls have the potential to return a negative error code. The
errors can be either one of those found in the `enum lfs_error` in
[lfs.h](https://github.com/littlefs-project/littlefs/blob/6cb4e86/lfs.h), or an error returned by the user's block device operations.

In the configuration struct, the `prog` and `erase` function provided by the
user may return a `LFS_ERR_CORRUPT` error if the implementation already can
detect corrupt blocks. However, the wear leveling does not depend on the return
code of these functions, instead all data is read back and checked for
integrity.

If your storage caches writes, make sure that the provided `sync` function
flushes all the data to memory and ensures that the next read fetches the data
from memory, otherwise data integrity can not be guaranteed. If the `write`
function does not perform caching, and therefore each `read` or `write` call
hits the memory, the `sync` function can simply return 0.
