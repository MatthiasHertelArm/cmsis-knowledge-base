---
id: "lfs-design-metadata-pairs"
type: "concept"
domain: "project"
title: "DESIGN: Metadata pairs"
summary: "Metadata pairs are the backbone of littlefs. These are small, two block logs that allow atomic updates anywhere in the filesystem."
status: "draft"
collection: "littlefs"
source: "littlefs-project/littlefs@6cb4e86:DESIGN.md"
doc_source: "https://github.com/littlefs-project/littlefs/blob/6cb4e86/DESIGN.md#metadata-pairs"
license: "BSD-3-Clause"
mode: "V"
---

Metadata pairs are the backbone of littlefs. These are small, two block logs
that allow atomic updates anywhere in the filesystem.

Why two blocks? Well, logs work by appending entries to a circular buffer
stored on disk. But remember that flash has limited write granularity. We can
incrementally program new data onto erased blocks, but we need to erase a full
block at a time. This means that in order for our circular buffer to work, we
need more than one block.

We could make our logs larger than two blocks, but the next challenge is how
do we store references to these logs? Because the blocks themselves are erased
during writes, using a data structure to track these blocks is complicated.
The simple solution here is to store a two block addresses for every metadata
pair. This has the added advantage that we can change out blocks in the
metadata pair independently, and we don't reduce our block granularity for
other operations.

In order to determine which metadata block is the most recent, we store a
revision count that we compare using [sequence arithmetic][wikipedia-sna]
(very handy for avoiding problems with integer overflow). Conveniently, this
revision count also gives us a rough idea of how many erases have occurred on
the block.

```
metadata pair pointer: {block 0, block 1}
                           |        '--------------------.
                            '-.                           |
disk                           v                          v
.--------.--------.--------.--------.--------.--------.--------.--------.
|                 |        |metadata|                 |metadata|        |
|                 |        |block 0 |                 |block 1 |        |
|                 |        |        |                 |        |        |
'--------'--------'--------'--------'--------'--------'--------'--------'
                               '--.                  .----'
                                   v                v
             metadata pair .----------------.----------------.
                           |   revision 11  |   revision 12  |
             block 1 is    |----------------|----------------|
             most recent   |       A        |       A''      |
                           |----------------|----------------|
                           |    checksum    |    checksum    |
                           |----------------|----------------|
                           |       B        |       A'''     | <- most recent A
                           |----------------|----------------|
                           |       A''      |    checksum    |
                           |----------------|----------------|
                           |    checksum    |       |        |
                           |----------------|       v        |
                           '----------------'----------------'
```

So how do we atomically update our metadata pairs? Atomicity (a type of
power-loss resilience) requires two parts: redundancy and error detection.
Error detection can be provided with a checksum, and in littlefs's case we
use a 32-bit [CRC][wikipedia-crc]. Maintaining redundancy, on the other hand,
requires multiple stages.

1. If our block is not full and the program size is small enough to let us
   append more entries, we can simply append the entries to the log. Because
   we don't overwrite the original entries (remember rewriting flash requires
   an erase), we still have the original entries if we lose power during the
   append.

   ```
                                    commit A
   .----------------.----------------.    .----------------.----------------.
   |   revision 1   |   revision 0   | => |   revision 1   |   revision 0   |
   |----------------|----------------|    |----------------|----------------|
   |       |        |                |    |       A        |                |
   |       v        |                |    |----------------|                |
   |                |                |    |    checksum    |                |
   |                |                |    |----------------|                |
   |                |                |    |       |        |                |
   |                |                |    |       v        |                |
   |                |                |    |                |                |
   |                |                |    |                |                |
   |                |                |    |                |                |
   |                |                |    |                |                |
   '----------------'----------------'    '----------------'----------------'
   ```

   Note that littlefs doesn't maintain a checksum for each entry. Many logging
   filesystems do this, but it limits what you can update in a single atomic
   operation. What we can do instead is group multiple entries into a commit
   that shares a single checksum. This lets us update multiple unrelated pieces
   of metadata as long as they reside on the same metadata pair.

   ```
                                 commit B and A'
   .----------------.----------------.    .----------------.----------------.
   |   revision 1   |   revision 0   | => |   revision 1   |   revision 0   |
   |----------------|----------------|    |----------------|----------------|
   |       A        |                |    |       A        |                |
   |----------------|                |    |----------------|                |
   |    checksum    |                |    |    checksum    |                |
   |----------------|                |    |----------------|                |
   |       |        |                |    |       B        |                |
   |       v        |                |    |----------------|                |
   |                |                |    |       A'       |                |
   |                |                |    |----------------|                |
   |                |                |    |    checksum    |                |
   |                |                |    |----------------|                |
   '----------------'----------------'    '----------------'----------------'
   ```

2. If our block _is_ full of entries, we need to somehow remove outdated
   entries to make space for new ones. This process is called garbage
   collection, but because littlefs has multiple garbage collectors, we
   also call this specific case compaction.

   Compared to other filesystems, littlefs's garbage collector is relatively
   simple. We want to avoid RAM consumption, so we use a sort of brute force
   solution where for each entry we check to see if a newer entry has been
   written. If the entry is the most recent we append it to our new block. This
   is where having two blocks becomes important, if we lose power we still have
   everything in our original block.

   During this compaction step we also erase the metadata block and increment
   the revision count. Because we can commit multiple entries at once, we can
   write all of these changes to the second block without worrying about power
   loss. It's only when the commit's checksum is written that the compacted
   entries and revision count become committed and readable.

   ```
                           commit B', need to compact
   .----------------.----------------.    .----------------.----------------.
   |   revision 1   |   revision 0   | => |   revision 1   |   revision 2   |
   |----------------|----------------|    |----------------|----------------|
   |       A        |                |    |       A        |       A'       |
   |----------------|                |    |----------------|----------------|
   |    checksum    |                |    |    checksum    |       B'       |
   |----------------|                |    |----------------|----------------|
   |       B        |                |    |       B        |    checksum    |
   |----------------|                |    |----------------|----------------|
   |       A'       |                |    |       A'       |       |        |
   |----------------|                |    |----------------|       v        |
   |    checksum    |                |    |    checksum    |                |
   |----------------|                |    |----------------|                |
   '----------------'----------------'    '----------------'----------------'
   ```

3. If our block is full of entries _and_ we can't find any garbage, then what?
   At this point, most logging filesystems would return an error indicating no
   more space is available, but because we have small logs, overflowing a log
   isn't really an error condition.

   Instead, we split our original metadata pair into two metadata pairs, each
   containing half of the entries, connected by a tail pointer. Instead of
   increasing the size of the log and dealing with the scalability issues
   associated with larger logs, we form a linked list of small bounded logs.
   This is a tradeoff as this approach does use more storage space, but at the
   benefit of improved scalability.

   Despite writing to two metadata pairs, we can still maintain power
   resilience during this split step by first preparing the new metadata pair,
   and then inserting the tail pointer during the commit to the original
   metadata pair.

   ```
                         commit C and D, need to split
   .----------------.----------------.    .----------------.----------------.
   |   revision 1   |   revision 2   | => |   revision 3   |   revision 2   |
   |----------------|----------------|    |----------------|----------------|
   |       A        |       A'       |    |       A'       |       A'       |
   |----------------|----------------|    |----------------|----------------|
   |    checksum    |       B'       |    |       B'       |       B'       |
   |----------------|----------------|    |----------------|----------------|
   |       B        |    checksum    |    |      tail    ---------------------.
   |----------------|----------------|    |----------------|----------------| |
   |       A'       |       |        |    |    checksum    |                | |
   |----------------|       v        |    |----------------|                | |
   |    checksum    |                |    |       |        |                | |
   |----------------|                |    |       v        |                | |
   '----------------'----------------'    '----------------'----------------' |
                                                   .----------------.---------'
                                                  v                v
                                          .----------------.----------------.
                                          |   revision 1   |   revision 0   |
                                          |----------------|----------------|
                                          |       C        |                |
                                          |----------------|                |
                                          |       D        |                |
                                          |----------------|                |
                                          |    checksum    |                |
                                          |----------------|                |
                                          |       |        |                |
                                          |       v        |                |
                                          |                |                |
                                          |                |                |
                                          '----------------'----------------'
   ```

There is another complexity the crops up when dealing with small logs. The
amortized runtime cost of garbage collection is not only dependent on its
one time cost (_O(n²)_ for littlefs), but also depends on how often
garbage collection occurs.

Consider two extremes:

1. Log is empty, garbage collection occurs once every _n_ updates
2. Log is full, garbage collection occurs **every** update

Clearly we need to be more aggressive than waiting for our metadata pair to
be full. As the metadata pair approaches fullness the frequency of compactions
grows very rapidly.

Looking at the problem generically, consider a log with ![n] bytes for each
entry, ![d] dynamic entries (entries that are outdated during garbage
collection), and ![s] static entries (entries that need to be copied during
garbage collection). If we look at the amortized runtime complexity of updating
this log we get this formula:

![cost = n + n (s / d+1)][metadata-formula1]

If we let ![r] be the ratio of static space to the size of our log in bytes, we
find an alternative representation of the number of static and dynamic entries:

![s = r (size/n)][metadata-formula2]

![d = (1 - r) (size/n)][metadata-formula3]

Substituting these in for ![d] and ![s] gives us a nice formula for the cost of
updating an entry given how full the log is:

![cost = n + n (r (size/n) / ((1-r) (size/n) + 1))][metadata-formula4]

Assuming 100 byte entries in a 4 KiB log, we can graph this using the entry
size to find a multiplicative cost:

![Metadata pair update cost graph][metadata-cost-graph]

So at 50% usage, we're seeing an average of 2x cost per update, and at 75%
usage, we're already at an average of 4x cost per update.

To avoid this exponential growth, instead of waiting for our metadata pair
to be full, we split the metadata pair once we exceed 50% capacity. We do this
lazily, waiting until we need to compact before checking if we fit in our 50%
limit. This limits the overhead of garbage collection to 2x the runtime cost,
giving us an amortized runtime complexity of _O(1)_.

---

If we look at metadata pairs and linked-lists of metadata pairs at a high
level, they have fairly nice runtime costs. Assuming _n_ metadata pairs,
each containing _m_ metadata entries, the _lookup_ cost for a specific
entry has a worst case runtime complexity of _O(nm)_. For _updating_ a specific
entry, the worst case complexity is _O(nm²)_, with an amortized complexity
of only _O(nm)_.

However, splitting at 50% capacity does mean that in the best case our
metadata pairs will only be 1/2 full. If we include the overhead of the second
block in our metadata pair, each metadata entry has an effective storage cost
of 4x the original size. I imagine users would not be happy if they found
that they can only use a quarter of their original storage. Metadata pairs
provide a mechanism for performing atomic updates, but we need a separate
mechanism for storing the bulk of our data.
