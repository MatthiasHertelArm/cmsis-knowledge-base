---
id: "lfs-readme-usage"
type: "concept"
domain: "project"
title: "README: Usage"
summary: "Detailed documentation (or at least as much detail as is currently available) can be found in the comments in lfs.h."
status: "draft"
collection: "littlefs"
source: "littlefs-project/littlefs@6cb4e86:README.md"
doc_source: "https://github.com/littlefs-project/littlefs/blob/6cb4e86/README.md#usage"
license: "BSD-3-Clause"
mode: "V"
---

Detailed documentation (or at least as much detail as is currently available)
can be found in the comments in [lfs.h](https://github.com/littlefs-project/littlefs/blob/6cb4e86/lfs.h).

littlefs takes in a configuration structure that defines how the filesystem
operates. The configuration struct provides the filesystem with the block
device operations and dimensions, tweakable parameters that tradeoff memory
usage for performance, and optional static buffers if the user wants to avoid
dynamic memory.

The state of the littlefs is stored in the `lfs_t` type which is left up
to the user to allocate, allowing multiple filesystems to be in use
simultaneously. With the `lfs_t` and configuration struct, a user can
format a block device or mount the filesystem.

Once mounted, the littlefs provides a full set of POSIX-like file and
directory functions, with the deviation that the allocation of filesystem
structures must be provided by the user.

All POSIX operations, such as remove and rename, are atomic, even in event
of power-loss. Additionally, file updates are not actually committed to
the filesystem until sync or close is called on the file.
