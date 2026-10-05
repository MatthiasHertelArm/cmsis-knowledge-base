---
id: "lfs-littlefs-design-existing-designs"
type: "concept"
domain: "project"
title: "littlefs DESIGN: Existing designs?"
summary: "So, what's already out there? There are, of course, many different filesystems, however they often share and borrow feature from each other."
status: "draft"
collection: "littlefs"
source: "littlefs-project/littlefs@6cb4e86:DESIGN.md"
doc_source: "https://github.com/littlefs-project/littlefs/blob/6cb4e86/DESIGN.md#existing-designs"
license: "BSD-3-Clause"
mode: "V"
---

So, what's already out there? There are, of course, many different filesystems,
however they often share and borrow feature from each other. If we look at
power-loss resilience and wear leveling, we can narrow these down to a handful
of designs.

1. First we have the non-resilient, block based filesystems, such as [FAT] and
   [ext2]. These are the earliest filesystem designs and often the most simple.
   Here storage is divided into blocks, with each file being stored in a
   collection of blocks. Without modifications, these filesystems are not
   power-loss resilient, so updating a file is a simple as rewriting the blocks
   in place.

   ```
               .--------.
               |  root  |
               |        |
               |        |
               '--------'
               .-'    '-.
              v          v
         .--------.  .--------.
         |   A    |  |   B    |
         |        |  |        |
         |        |  |        |
         '--------'  '--------'
         .-'         .-'    '-.
        v           v          v
   .--------.  .--------.  .--------.
   |   C    |  |   D    |  |   E    |
   |        |  |        |  |        |
   |        |  |        |  |        |
   '--------'  '--------'  '--------'
   ```

   Because of their simplicity, these filesystems are usually both the fastest
   and smallest. However the lack of power resilience is not great, and the
   binding relationship of storage location and data removes the filesystem's
   ability to manage wear.

2. In a completely different direction, we have logging filesystems, such as
   [JFFS], [YAFFS], and [SPIFFS], storage location is not bound to a piece of
   data, instead the entire storage is used for a circular log which is
   appended with every change made to the filesystem. Writing appends new
   changes, while reading requires traversing the log to reconstruct a file.
   Some logging filesystems cache files to avoid the read cost, but this comes
   at a tradeoff of RAM.

   ```
                                                             v
   .--------.--------.--------.--------.--------.--------.--------.--------.
   |        C        | new B  | new A  |                 |   A    |   B    |
   |                 |        |        |->               |        |        |
   |                 |        |        |                 |        |        |
   '--------'--------'--------'--------'--------'--------'--------'--------'
   ```

   Logging filesystem are beautifully elegant. With a checksum, we can easily
   detect power-loss and fall back to the previous state by ignoring failed
   appends. And if that wasn't good enough, their cyclic nature means that
   logging filesystems distribute wear across storage perfectly.

   The main downside is performance. If we look at garbage collection, the
   process of cleaning up outdated data from the end of the log, I've yet to
   see a pure logging filesystem that does not have one of these two costs:

   1. _O(n²)_ runtime
   2. _O(n)_ RAM

   SPIFFS is a very interesting case here, as it uses the fact that repeated
   programs to NOR flash is both atomic and masking. This is a very neat
   solution, however it limits the type of storage you can support.

3. Perhaps the most common type of filesystem, a journaling filesystem is the
   offspring that happens when you mate a block based filesystem with a logging
   filesystem. [ext4] and [NTFS] are good examples. Here, we take a normal
   block based filesystem and add a bounded log where we note every change
   before it occurs.

   ```
                             journal
                            .--------.--------.
               .--------.   | C'| D'|     | E'|
               |  root  |-->|   |   |->   |   |
               |        |   |   |   |     |   |
               |        |   '--------'--------'
               '--------'
               .-'    '-.
              v          v
         .--------.  .--------.
         |   A    |  |   B    |
         |        |  |        |
         |        |  |        |
         '--------'  '--------'
         .-'         .-'    '-.
        v           v          v
   .--------.  .--------.  .--------.
   |   C    |  |   D    |  |   E    |
   |        |  |        |  |        |
   |        |  |        |  |        |
   '--------'  '--------'  '--------'
   ```


   This sort of filesystem takes the best from both worlds. Performance can be
   as fast as a block based filesystem (though updating the journal does have
   a small cost), and atomic updates to the journal allow the filesystem to
   recover in the event of a power loss.

   Unfortunately, journaling filesystems have a couple of problems. They are
   fairly complex, since there are effectively two filesystems running in
   parallel, which comes with a code size cost. They also offer no protection
   against wear because of the strong relationship between storage location
   and data.

4. Last but not least we have copy-on-write (COW) filesystems, such as
   [btrfs] and [ZFS]. These are very similar to other block based filesystems,
   but instead of updating block inplace, all updates are performed by creating
   a copy with the changes and replacing any references to the old block with
   our new block. This recursively pushes all of our problems upwards until we
   reach the root of our filesystem, which is often stored in a very small log.

   ```
               .--------.                  .--------.
               |  root  |       write      |new root|
               |        |        ==>       |        |
               |        |                  |        |
               '--------'                  '--------'
               .-'    '-.                    |    '-.
              |  .-------|------------------'        v
              v v        v                       .--------.
         .--------.  .--------.                  | new B  |
         |   A    |  |   B    |                  |        |
         |        |  |        |                  |        |
         |        |  |        |                  '--------'
         '--------'  '--------'                  .-'    |
         .-'         .-'    '-.    .------------|------'
        |           |          |  |             v
        v           v          v  v        .--------.
   .--------.  .--------.  .--------.      | new D  |
   |   C    |  |   D    |  |   E    |      |        |
   |        |  |        |  |        |      |        |
   |        |  |        |  |        |      '--------'
   '--------'  '--------'  '--------'
   ```

   COW filesystems are interesting. They offer very similar performance to
   block based filesystems while managing to pull off atomic updates without
   storing data changes directly in a log. They even disassociate the storage
   location of data, which creates an opportunity for wear leveling.

   Well, almost. The unbounded upwards movement of updates causes some
   problems. Because updates to a COW filesystem don't stop until they've
   reached the root, an update can cascade into a larger set of writes than
   would be needed for the original data. On top of this, the upward motion
   focuses these writes into the block, which can wear out much earlier than
   the rest of the filesystem.
