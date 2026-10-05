---
id: "lfs-design-the-problem"
type: "concept"
domain: "project"
title: "DESIGN: The problem"
summary: "The embedded systems littlefs targets are usually 32-bit microcontrollers with around 32 KiB of RAM and 512 KiB of ROM. These are often paired with SPI NOR flash chips with about 4 MiB of flash storage."
status: "draft"
collection: "littlefs"
source: "littlefs-project/littlefs@6cb4e86:DESIGN.md"
doc_source: "https://github.com/littlefs-project/littlefs/blob/6cb4e86/DESIGN.md#the-problem"
license: "BSD-3-Clause"
mode: "V"
---

The embedded systems littlefs targets are usually 32-bit microcontrollers with
around 32 KiB of RAM and 512 KiB of ROM. These are often paired with SPI NOR
flash chips with about 4 MiB of flash storage. These devices are too small for
Linux and most existing filesystems, requiring code written specifically with
size in mind.

Flash itself is an interesting piece of technology with its own quirks and
nuance. Unlike other forms of storage, writing to flash requires two
operations: erasing and programming. Programming (setting bits to 0) is
relatively cheap and can be very granular. Erasing however (setting bits to 1),
requires an expensive and destructive operation which gives flash its name.
[Wikipedia][wikipedia-flash] has more information on how exactly flash works.

To make the situation more annoying, it's very common for these embedded
systems to lose power at any time. Usually, microcontroller code is simple and
reactive, with no concept of a shutdown routine. This presents a big challenge
for persistent storage, where an unlucky power loss can corrupt the storage and
leave a device unrecoverable.

This leaves us with three major requirements for an embedded filesystem.

1. **Power-loss resilience** - On these systems, power can be lost at any time.
   If a power loss corrupts any persistent data structures, this can cause the
   device to become unrecoverable. An embedded filesystem must be designed to
   recover from a power loss during any write operation.

1. **Wear leveling** - Writing to flash is destructive. If a filesystem
   repeatedly writes to the same block, eventually that block will wear out.
   Filesystems that don't take wear into account can easily burn through blocks
   used to store frequently updated metadata and cause a device's early death.

1. **Bounded RAM/ROM** - If the above requirements weren't enough, these
   systems also have very limited amounts of memory. This prevents many
   existing filesystem designs, which can lean on relatively large amounts of
   RAM to temporarily store filesystem metadata.

   For ROM, this means we need to keep our design simple and reuse code paths
   where possible. For RAM we have a stronger requirement, all RAM usage is
   bounded. This means RAM usage does not grow as the filesystem changes in
   size or number of files. This creates a unique challenge as even presumably
   simple operations, such as traversing the filesystem, become surprisingly
   difficult.
