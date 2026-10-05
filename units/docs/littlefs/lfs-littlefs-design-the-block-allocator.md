---
id: "lfs-littlefs-design-the-block-allocator"
type: "concept"
domain: "project"
title: "littlefs DESIGN: The block allocator"
summary: "So we now have the framework for an atomic, wear leveling filesystem. Small two block metadata pairs provide atomic updates, while CTZ skip-lists provide compact storage of data in COW blocks."
status: "draft"
collection: "littlefs"
source: "littlefs-project/littlefs@6cb4e86:DESIGN.md"
doc_source: "https://github.com/littlefs-project/littlefs/blob/6cb4e86/DESIGN.md#the-block-allocator"
license: "BSD-3-Clause"
mode: "V"
---

So we now have the framework for an atomic, wear leveling filesystem. Small two
block metadata pairs provide atomic updates, while CTZ skip-lists provide
compact storage of data in COW blocks.

But now we need to look at the [elephant] in the room. Where do all these
blocks come from?

Deciding which block to use next is the responsibility of the block allocator.
In filesystem design, block allocation is often a second-class citizen, but in
a COW filesystem its role becomes much more important as it is needed for
nearly every write to the filesystem.

Normally, block allocation involves some sort of free list or bitmap stored on
the filesystem that is updated with free blocks. However, with power
resilience, keeping these structures consistent becomes difficult. It doesn't
help that any mistake in updating these structures can result in lost blocks
that are impossible to recover.

littlefs takes a cautious approach. Instead of trusting a free list on disk,
littlefs relies on the fact that the filesystem on disk is a mirror image of
the free blocks on the disk. The block allocator operates much like a garbage
collector in a scripting language, scanning for unused blocks on demand.

```
          .----.
          |root|
          |    |
          '----'
   v-------'  '-------v
.----.    .    .    .----.
| A  |    .    .    | B  |
|    |    .    .    |    |
'----'    .    .    '----'
.    .    .    .  v--'  '------------v---------v
.    .    .    .----.    .         .----.    .----.
.    .    .    | C  |    .         | D  |    | E  |
.    .    .    |    |    .         |    |    |    |
.    .    .    '----'    .         '----'    '----'
.    .    .    .    .    .         .    .    .    .
.----.----.----.----.----.----.----.----.----.----.----.----.
| A  |    |root| C  | B  |         | D  |    | E  |         |
|    |    |    |    |    |         |    |    |    |         |
'----'----'----'----'----'----'----'----'----'----'----'----'
        ^                   ^    ^                   ^    ^
         '-------------------'----'-------------------'----'-- free blocks
```

While this approach may sound complicated, the decision to not maintain a free
list greatly simplifies the overall design of littlefs. Unlike programming
languages, there are only a handful of data structures we need to traverse.
And block deallocation, which occurs nearly as often as block allocation,
is simply a noop. This "drop it on the floor" strategy greatly reduces the
complexity of managing on disk data structures, especially when handling
high-risk error conditions.

---

Our block allocator needs to find free blocks efficiently. You could traverse
through every block on storage and check each one against our filesystem tree;
however, the runtime would be abhorrent. We need to somehow collect multiple
blocks per traversal.

Looking at existing designs, some larger filesystems that use a similar "drop
it on the floor" strategy store a bitmap of the entire storage in [RAM]. This
works well because bitmaps are surprisingly compact. We can't use the same
strategy here, as it violates our constant RAM requirement, but we may be able
to modify the idea into a workable solution.

```
.----.----.----.----.----.----.----.----.----.----.----.----.
| A  |    |root| C  | B  |         | D  |    | E  |         |
|    |    |    |    |    |         |    |    |    |         |
'----'----'----'----'----'----'----'----'----'----'----'----'
  1    0    1    1    1    0    0    1    0    1    0    0
 \---------------------------+----------------------------/
                             v
               bitmap: 0xb94 (0b101110010100)
```

The block allocator in littlefs is a compromise between a disk-sized bitmap and
a brute force traversal. Instead of a bitmap the size of storage, we keep track
of a small, fixed-size bitmap called the lookahead buffer. During block
allocation, we take blocks from the lookahead buffer. If the lookahead buffer
is empty, we scan the filesystem for more free blocks, populating our lookahead
buffer. In each scan we use an increasing offset, circling the storage as
blocks are allocated.

Here's what it might look like to allocate 4 blocks on a decently busy
filesystem with a 32 bit lookahead and a total of 128 blocks (512 KiB
of storage if blocks are 4 KiB):
```
boot...         lookahead:
                fs blocks: fffff9fffffffffeffffffffffff0000
scanning...     lookahead: fffff9ff
                fs blocks: fffff9fffffffffeffffffffffff0000
alloc = 21      lookahead: fffffdff
                fs blocks: fffffdfffffffffeffffffffffff0000
alloc = 22      lookahead: ffffffff
                fs blocks: fffffffffffffffeffffffffffff0000
scanning...     lookahead:         fffffffe
                fs blocks: fffffffffffffffeffffffffffff0000
alloc = 63      lookahead:         ffffffff
                fs blocks: ffffffffffffffffffffffffffff0000
scanning...     lookahead:         ffffffff
                fs blocks: ffffffffffffffffffffffffffff0000
scanning...     lookahead:                 ffffffff
                fs blocks: ffffffffffffffffffffffffffff0000
scanning...     lookahead:                         ffff0000
                fs blocks: ffffffffffffffffffffffffffff0000
alloc = 112     lookahead:                         ffff8000
                fs blocks: ffffffffffffffffffffffffffff8000
```

This lookahead approach has a runtime complexity of _O(n²)_ to completely
scan storage; however, bitmaps are surprisingly compact, and in practice only
one or two passes are usually needed to find free blocks. Additionally, the
performance of the allocator can be optimized by adjusting the block size or
size of the lookahead buffer, trading either write granularity or RAM for
allocator performance.
