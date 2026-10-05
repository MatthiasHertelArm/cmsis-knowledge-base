---
id: "lfs-design-files"
type: "concept"
domain: "project"
title: "DESIGN: Files"
summary: "Now that we have our building blocks out of the way, we can start looking at our filesystem as a whole."
status: "draft"
collection: "littlefs"
source: "littlefs-project/littlefs@6cb4e86:DESIGN.md"
doc_source: "https://github.com/littlefs-project/littlefs/blob/6cb4e86/DESIGN.md#files"
license: "BSD-3-Clause"
mode: "V"
---

Now that we have our building blocks out of the way, we can start looking at
our filesystem as a whole.

The first step: How do we actually store our files?

We've determined that CTZ skip-lists are pretty good at storing data compactly,
so following the precedent found in other filesystems we could give each file
a skip-list stored in a metadata pair that acts as an inode for the file.


```
                                    .--------.
                                   .|metadata|
                                   ||        |
                                   ||        |
                                   |'--------'
                                   '----|---'
                                        v
.--------.  .--------.  .--------.  .--------.
| data 0 |<-| data 1 |<-| data 2 |<-| data 3 |
|        |<-|        |--|        |  |        |
|        |  |        |  |        |  |        |
'--------'  '--------'  '--------'  '--------'
```

However, this doesn't work well when files are small, which is common for
embedded systems. Compared to PCs, _all_ data in an embedded system is small.

Consider a small 4-byte file. With a two block metadata-pair and one block for
the CTZ skip-list, we find ourselves using a full 3 blocks. On most NOR flash
with 4 KiB blocks, this is 12 KiB of overhead. A ridiculous 3072x increase.

```
file stored as inode, 4 bytes costs ~12 KiB

 .----------------.                  \
.|    revision    |                  |
||----------------|    \             |
||    skiplist   ---.  +- metadata   |
||----------------| |  /  4x8 bytes  |
||    checksum    | |     32 bytes   |
||----------------| |                |
||       |        | |                +- metadata pair
||       v        | |                |  2x4 KiB
||                | |                |  8 KiB
||                | |                |
||                | |                |
||                | |                |
|'----------------' |                |
'----------------'  |                /
          .--------'
         v
 .----------------.    \             \
 |      data      |    +- data       |
 |----------------|    /  4 bytes    |
 |                |                  |
 |                |                  |
 |                |                  |
 |                |                  +- data block
 |                |                  |  4 KiB
 |                |                  |
 |                |                  |
 |                |                  |
 |                |                  |
 |                |                  |
 '----------------'                  /
```

We can make several improvements. First, instead of giving each file its own
metadata pair, we can store multiple files in a single metadata pair. One way
to do this is to directly associate a directory with a metadata pair (or a
linked list of metadata pairs). This makes it easy for multiple files to share
the directory's metadata pair for logging and reduces the collective storage
overhead.

The strict binding of metadata pairs and directories also gives users
direct control over storage utilization depending on how they organize their
directories.

```
multiple files stored in metadata pair, 4 bytes costs ~4 KiB

       .----------------.
      .|    revision    |
      ||----------------|
      ||    A name      |
      ||   A skiplist  -----.
      ||----------------|   |  \
      ||    B name      |   |  +- metadata
      ||   B skiplist  ---. |  |  4x8 bytes
      ||----------------| | |  /  32 bytes
      ||    checksum    | | |
      ||----------------| | |
      ||       |        | | |
      ||       v        | | |
      |'----------------' | |
      '----------------'  | |
         .----------------' |
        v                   v
.----------------.  .----------------.  \           \
|     A data     |  |     B data     |  +- data     |
|                |  |----------------|  /  4 bytes  |
|                |  |                |              |
|                |  |                |              |
|                |  |                |              |
|                |  |                |              + data block
|                |  |                |              | 4 KiB
|                |  |                |              |
|----------------|  |                |              |
|                |  |                |              |
|                |  |                |              |
|                |  |                |              |
'----------------'  '----------------'              /
```

The second improvement we can make is noticing that for very small files, our
attempts to use CTZ skip-lists for compact storage backfires. Metadata pairs
have a ~4x storage cost, so if our file is smaller than 1/4 the block size,
there's actually no benefit in storing our file outside of our metadata pair.

In this case, we can store the file directly in our directory's metadata pair.
We call this an inline file, and it allows a directory to store many small
files quite efficiently. Our previous 4 byte file now only takes up a
theoretical 16 bytes on disk.

```
inline files stored in metadata pair, 4 bytes costs ~16 bytes

 .----------------.
.|    revision    |
||----------------|
||    A name      |
||   A skiplist  ---.
||----------------| |  \
||    B name      | |  +- data
||    B data      | |  |  4x4 bytes
||----------------| |  /  16 bytes
||    checksum    | |
||----------------| |
||       |        | |
||       v        | |
|'----------------' |
'----------------'  |
          .---------'
         v
 .----------------.
 |     A data     |
 |                |
 |                |
 |                |
 |                |
 |                |
 |                |
 |                |
 |----------------|
 |                |
 |                |
 |                |
 '----------------'
```

Once the file exceeds 1/4 the block size, we switch to a CTZ skip-list. This
means that our files never use more than 4x storage overhead, decreasing as
the file grows in size.

![File storage cost graph][file-cost-graph]
