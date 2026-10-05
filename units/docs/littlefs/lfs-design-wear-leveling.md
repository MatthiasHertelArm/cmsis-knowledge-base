---
id: "lfs-design-wear-leveling"
type: "concept"
domain: "project"
title: "DESIGN: Wear leveling"
summary: "The block allocator has a secondary role: wear leveling."
status: "draft"
collection: "littlefs"
source: "littlefs-project/littlefs@6cb4e86:DESIGN.md"
doc_source: "https://github.com/littlefs-project/littlefs/blob/6cb4e86/DESIGN.md#wear-leveling"
license: "BSD-3-Clause"
mode: "V"
---

The block allocator has a secondary role: wear leveling.

Wear leveling is the process of distributing wear across all blocks in the
storage to prevent the filesystem from experiencing an early death due to
wear on a single block in the storage.

littlefs has two methods of protecting against wear:
1. Detection and recovery from bad blocks
2. Evenly distributing wear across dynamic blocks

---

Recovery from bad blocks doesn't actually have anything to do with the block
allocator itself. Instead, it relies on the ability of the filesystem to detect
and evict bad blocks when they occur.

In littlefs, it is fairly straightforward to detect bad blocks at write time.
All writes must be sourced by some form of data in RAM, so immediately after we
write to a block, we can read the data back and verify that it was written
correctly. If we find that the data on disk does not match the copy we have in
RAM, a write error has occurred and we most likely have a bad block.

Once we detect a bad block, we need to recover from it. In the case of write
errors, we have a copy of the corrupted data in RAM, so all we need to do is
evict the bad block, allocate a new, hopefully good block, and repeat the write
that previously failed.

The actual act of evicting the bad block and replacing it with a new block is
left up to the filesystem's copy-on-bounded-writes (CObW) data structures. One
property of CObW data structures is that any block can be replaced during a
COW operation. The bounded-writes part is normally triggered by a counter, but
nothing prevents us from triggering a COW operation as soon as we find a bad
block.

```
     .----.
     |root|
     |    |
     '----'
   v--'  '----------------------v
.----.                        .----.
| A  |                        | B  |
|    |                        |    |
'----'                        '----'
.    .                      v---'  .
.    .                   .----.    .
.    .                   | C  |    .
.    .                   |    |    .
.    .                   '----'    .
.    .                   .    .    .
.----.----.----.----.----.----.----.----.----.----.
| A  |root|              | C  | B  |              |
|    |    |              |    |    |              |
'----'----'----'----'----'----'----'----'----'----'

update C
=>
     .----.
     |root|
     |    |
     '----'
   v--'  '----------------------v
.----.                        .----.
| A  |                        | B  |
|    |                        |    |
'----'                        '----'
.    .                      v---'  .
.    .                   .----.    .
.    .                   |bad |    .
.    .                   |blck|    .
.    .                   '----'    .
.    .                   .    .    .
.----.----.----.----.----.----.----.----.----.----.
| A  |root|              |bad | B  |              |
|    |    |              |blck|    |              |
'----'----'----'----'----'----'----'----'----'----'

oh no! bad block! relocate C
=>
     .----.
     |root|
     |    |
     '----'
   v--'  '----------------------v
.----.                        .----.
| A  |                        | B  |
|    |                        |    |
'----'                        '----'
.    .                      v---'  .
.    .                   .----.    .
.    .                   |bad |    .
.    .                   |blck|    .
.    .                   '----'    .
.    .                   .    .    .
.----.----.----.----.----.----.----.----.----.----.
| A  |root|              |bad | B  |bad |         |
|    |    |              |blck|    |blck|         |
'----'----'----'----'----'----'----'----'----'----'
                            --------->
oh no! bad block! relocate C
=>
     .----.
     |root|
     |    |
     '----'
   v--'  '----------------------v
.----.                        .----.
| A  |                        | B  |
|    |                        |    |
'----'                        '----'
.    .                      v---'  .
.    .                   .----.    .    .----.
.    .                   |bad |    .    | C' |
.    .                   |blck|    .    |    |
.    .                   '----'    .    '----'
.    .                   .    .    .    .    .
.----.----.----.----.----.----.----.----.----.----.
| A  |root|              |bad | B  |bad | C' |    |
|    |    |              |blck|    |blck|    |    |
'----'----'----'----'----'----'----'----'----'----'
                            -------------->
successfully relocated C, update B
=>
     .----.
     |root|
     |    |
     '----'
   v--'  '----------------------v
.----.                        .----.
| A  |                        |bad |
|    |                        |blck|
'----'                        '----'
.    .                      v---'  .
.    .                   .----.    .    .----.
.    .                   |bad |    .    | C' |
.    .                   |blck|    .    |    |
.    .                   '----'    .    '----'
.    .                   .    .    .    .    .
.----.----.----.----.----.----.----.----.----.----.
| A  |root|              |bad |bad |bad | C' |    |
|    |    |              |blck|blck|blck|    |    |
'----'----'----'----'----'----'----'----'----'----'

oh no! bad block! relocate B
=>
     .----.
     |root|
     |    |
     '----'
   v--'  '----------------------v
.----.                        .----.         .----.
| A  |                        |bad |         |bad |
|    |                        |blck|         |blck|
'----'                        '----'         '----'
.    .                      v---'  .         .    .
.    .                   .----.    .    .----.    .
.    .                   |bad |    .    | C' |    .
.    .                   |blck|    .    |    |    .
.    .                   '----'    .    '----'    .
.    .                   .    .    .    .    .    .
.----.----.----.----.----.----.----.----.----.----.
| A  |root|              |bad |bad |bad | C' |bad |
|    |    |              |blck|blck|blck|    |blck|
'----'----'----'----'----'----'----'----'----'----'
                                 -------------->
oh no! bad block! relocate B
=>
     .----.
     |root|
     |    |
     '----'
   v--'  '----------------------v
.----.    .----.              .----.
| A  |    | B' |              |bad |
|    |    |    |              |blck|
'----'    '----'              '----'
.    .    .  | .            .---'  .
.    .    .  '--------------v-------------v
.    .    .    .         .----.    .    .----.
.    .    .    .         |bad |    .    | C' |
.    .    .    .         |blck|    .    |    |
.    .    .    .         '----'    .    '----'
.    .    .    .         .    .    .    .    .
.----.----.----.----.----.----.----.----.----.----.
| A  |root| B' |         |bad |bad |bad | C' |bad |
|    |    |    |         |blck|blck|blck|    |blck|
'----'----'----'----'----'----'----'----'----'----'
------------>                    ------------------
successfully relocated B, update root
=>
     .----.
     |root|
     |    |
     '----'
   v--'  '--v
.----.    .----.
| A  |    | B' |
|    |    |    |
'----'    '----'
.    .    .   '---------------------------v
.    .    .    .                        .----.
.    .    .    .                        | C' |
.    .    .    .                        |    |
.    .    .    .                        '----'
.    .    .    .                        .    .
.----.----.----.----.----.----.----.----.----.----.
| A  |root| B' |         |bad |bad |bad | C' |bad |
|    |    |    |         |blck|blck|blck|    |blck|
'----'----'----'----'----'----'----'----'----'----'
```

We may find that the new block is also bad, but hopefully after repeating this
cycle we'll eventually find a new block where a write succeeds. If we don't,
that means that all blocks in our storage are bad, and we've reached the end of
our device's usable life. At this point, littlefs will return an "out of space"
error. This is technically true, as there are no more good blocks, but as an
added benefit it also matches the error condition expected by users of
dynamically sized data.

---

Read errors, on the other hand, are quite a bit more complicated. We don't have
a copy of the data lingering around in RAM, so we need a way to reconstruct the
original data even after it has been corrupted. One such mechanism for this is
[error-correction-codes (ECC)][wikipedia-ecc].

ECC is an extension to the idea of a checksum. Where a checksum such as CRC can
detect that an error has occurred in the data, ECC can detect and actually
correct some amount of errors. However, there is a limit to how many errors ECC
can detect: the [Hamming bound][wikipedia-hamming-bound]. As the number of
errors approaches the Hamming bound, we may still be able to detect errors, but
can no longer fix the data. If we've reached this point the block is
unrecoverable.

littlefs by itself does **not** provide ECC. The block nature and relatively
large footprint of ECC does not work well with the dynamically sized data of
filesystems, correcting errors without RAM is complicated, and ECC fits better
with the geometry of block devices. In fact, several NOR flash chips have extra
storage intended for ECC, and many NAND chips can even calculate ECC on the
chip itself.

In littlefs, ECC is entirely optional. Read errors can instead be prevented
proactively by wear leveling. But it's important to note that ECC can be used
at the block device level to modestly extend the life of a device. littlefs
respects any errors reported by the block device, allowing a block device to
provide additional aggressive error detection.

---

To avoid read errors, we need to be proactive, as opposed to reactive as we
were with write errors.

One way to do this is to detect when the number of errors in a block exceeds
some threshold, but is still recoverable. With ECC we can do this at write
time, and treat the error as a write error, evicting the block before fatal
read errors have a chance to develop.

A different, more generic strategy, is to proactively distribute wear across
all blocks in the storage, with the hope that no single block fails before the
rest of storage is approaching the end of its usable life. This is called
wear leveling.

Generally, wear leveling algorithms fall into one of two categories:

1. [Dynamic wear leveling][wikipedia-dynamic-wear-leveling], where we
   distribute wear over "dynamic" blocks. The can be accomplished by
   only considering unused blocks.

2. [Static wear leveling][wikipedia-static-wear-leveling], where we
   distribute wear over both "dynamic" and "static" blocks. To make this work,
   we need to consider all blocks, including blocks that already contain data.

As a tradeoff for code size and complexity, littlefs (currently) only provides
dynamic wear leveling. This is a best effort solution. Wear is not distributed
perfectly, but it is distributed among the free blocks and greatly extends the
life of a device.

On top of this, littlefs uses a statistical wear leveling algorithm. What this
means is that we don’t actively track wear, instead we rely on a uniform
distribution of wear across storage to approximate a dynamic wear leveling
algorithm. Despite the long name, this is actually a simplification of dynamic
wear leveling.

The uniform distribution of wear is left up to the block allocator, which
creates a uniform distribution in two parts. The easy part is when the device
is powered, in which case we allocate the blocks linearly, circling the device.
The harder part is what to do when the device loses power. We can't just
restart the allocator at the beginning of storage, as this would bias the wear.
Instead, we start the allocator as a random offset every time we mount the
filesystem. As long as this random offset is uniform, the combined allocation
pattern is also a uniform distribution.

![Cumulative wear distribution graph][wear-distribution-graph]

Initially, this approach to wear leveling looks like it creates a difficult
dependency on a power-independent random number generator, which must return
different random numbers on each boot. However, the filesystem is in a
relatively unique situation in that it is sitting on top of a large of amount
of entropy that persists across power loss.

We can actually use the data on disk to directly drive our random number
generator. In practice, this is implemented by xoring the checksums of each
metadata pair, which is already calculated to fetch and mount the filesystem.

```
            .--------. \                         probably random
           .|metadata| |                                ^
           ||        | +-> crc ----------------------> xor
           ||        | |                                ^
           |'--------' /                                |
           '---|--|-'                                   |
            .-'    '-------------------------.          |
           |                                  |         |
           |        .--------------> xor ------------> xor
           |        |                 ^       |         ^
           v       crc               crc      v        crc
      .--------. \  ^   .--------. \  ^   .--------. \  ^
     .|metadata|-|--|-->|metadata| |  |  .|metadata| |  |
     ||        | +--'  ||        | +--'  ||        | +--'
     ||        | |     ||        | |     ||        | |
     |'--------' /     |'--------' /     |'--------' /
     '---|--|-'        '----|---'        '---|--|-'
      .-'    '-.            |             .-'    '-.
     v          v           v            v          v
.--------.  .--------.  .--------.  .--------.  .--------.
|  data  |  |  data  |  |  data  |  |  data  |  |  data  |
|        |  |        |  |        |  |        |  |        |
|        |  |        |  |        |  |        |  |        |
'--------'  '--------'  '--------'  '--------'  '--------'
```

Note that this random number generator is not perfect. It only returns unique
random numbers when the filesystem is modified. This is exactly what we want
for distributing wear in the allocator, but means this random number generator
is not useful for general use.

---

Together, bad block detection and dynamic wear leveling provide a best effort
solution for avoiding the early death of a filesystem due to wear. Importantly,
littlefs's wear leveling algorithm provides a key feature: You can increase the
life of a device simply by increasing the size of storage. And if more
aggressive wear leveling is desired, you can always combine littlefs with a
[flash translation layer (FTL)][wikipedia-ftl] to get a small power resilient
filesystem with static wear leveling.
