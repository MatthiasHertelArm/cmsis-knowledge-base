---
id: "lfs-littlefs-spec-directories-metadata-pairs"
type: "concept"
domain: "project"
title: "littlefs SPEC: Directories / Metadata pairs"
summary: "Metadata pairs form the backbone of littlefs and provide a system for distributed atomic updates. Even the superblock is stored in a metadata pair."
status: "draft"
collection: "littlefs"
source: "littlefs-project/littlefs@6cb4e86:SPEC.md"
doc_source: "https://github.com/littlefs-project/littlefs/blob/6cb4e86/SPEC.md#directories-metadata-pairs"
license: "BSD-3-Clause"
mode: "V"
---

Metadata pairs form the backbone of littlefs and provide a system for
distributed atomic updates. Even the superblock is stored in a metadata pair.

As their name suggests, a metadata pair is stored in two blocks, with one block
providing a backup during erase cycles in case power is lost. These two blocks
are not necessarily sequential and may be anywhere on disk, so a "pointer" to a
metadata pair is stored as two block pointers.

On top of this, each metadata block behaves as an appendable log, containing a
variable number of commits. Commits can be appended to the metadata log in
order to update the metadata without requiring an erase cycles. Note that
successive commits may supersede the metadata in previous commits. Only the
most recent metadata should be considered valid.

The high-level layout of a metadata block is fairly simple:

```
  .---------------------------------------.
.-|  revision count   |      entries      |  \
| |-------------------+                   |  |
| |                                       |  |
| |                                       |  +-- 1st commit
| |                                       |  |
| |                   +-------------------|  |
| |                   |        CRC        |  /
| |-------------------+-------------------|
| |                entries                |  \
| |                                       |  |
| |                                       |  +-- 2nd commit
| |    +-------------------+--------------|  |
| |    |        CRC        |    padding   |  /
| |----+-------------------+--------------|
| |                entries                |  \
| |                                       |  |
| |                                       |  +-- 3rd commit
| |         +-------------------+---------|  |
| |         |        CRC        |         |  /
| |---------+-------------------+         |
| |           unwritten storage           |  more commits
| |                                       |       |
| |                                       |       v
| |                                       |
| |                                       |
| '---------------------------------------'
'---------------------------------------'
```

Each metadata block contains a 32-bit revision count followed by a number of
commits. Each commit contains a variable number of metadata entries followed
by a 32-bit CRC.

Note also that entries aren't necessarily word-aligned. This allows us to
store metadata more compactly, however we can only write to addresses that are
aligned to our program block size. This means each commit may have padding for
alignment.

Metadata block fields:

1. **Revision count (32-bits)** - Incremented every erase cycle. If both blocks
   contain valid commits, only the block with the most recent revision count
   should be used. Sequence comparison must be used to avoid issues with
   integer overflow.

2. **CRC (32-bits)** - Detects corruption from power-loss or other write
   issues.  Uses a CRC-32 with a polynomial of `0x04c11db7` initialized
   with `0xffffffff`.

Entries themselves are stored as a 32-bit tag followed by a variable length
blob of data. But exactly how these tags are stored is a little bit tricky.

Metadata blocks support both forward and backward iteration. In order to do
this without duplicating the space for each tag, neighboring entries have their
tags XORed together, starting with `0xffffffff`.

```
 Forward iteration                        Backward iteration

.-------------------.  0xffffffff        .-------------------.
|  revision count   |      |             |  revision count   |
|-------------------|      v             |-------------------|
|      tag ~A       |---> xor -> tag A   |      tag ~A       |---> xor -> 0xffffffff
|-------------------|      |             |-------------------|      ^
|       data A      |      |             |       data A      |      |
|                   |      |             |                   |      |
|                   |      |             |                   |      |
|-------------------|      v             |-------------------|      |
|      tag AxB      |---> xor -> tag B   |      tag AxB      |---> xor -> tag A
|-------------------|      |             |-------------------|      ^
|       data B      |      |             |       data B      |      |
|                   |      |             |                   |      |
|                   |      |             |                   |      |
|-------------------|      v             |-------------------|      |
|      tag BxC      |---> xor -> tag C   |      tag BxC      |---> xor -> tag B
|-------------------|                    |-------------------|      ^
|       data C      |                    |       data C      |      |
|                   |                    |                   |    tag C
|                   |                    |                   |
|                   |                    |                   |
'-------------------'                    '-------------------'
```

Here's a more complete example of metadata block containing 4 entries:

```
  .---------------------------------------.
.-|  revision count   |      tag ~A       |        \
| |-------------------+-------------------|        |
| |                 data A                |        |
| |                                       |        |
| |-------------------+-------------------|        |
| |      tag AxB      |       data B      | <--.   |
| |-------------------+                   |    |   |
| |                                       |    |   +-- 1st commit
| |         +-------------------+---------|    |   |
| |         |      tag BxC      |         | <-.|   |
| |---------+-------------------+         |   ||   |
| |                 data C                |   ||   |
| |                                       |   ||   |
| |-------------------+-------------------|   ||   |
| |     tag CxCRC     |        CRC        |   ||   /
| |-------------------+-------------------|   ||
| |     tag CRCxA'    |      data A'      |   ||   \
| |-------------------+                   |   ||   |
| |                                       |   ||   |
| |              +-------------------+----|   ||   +-- 2nd commit
| |              |     tag CRCxA'    |    |   ||   |
| |--------------+-------------------+----|   ||   |
| | CRC          |        padding         |   ||   /
| |--------------+----+-------------------|   ||
| |     tag CRCxA''   |      data A''     | <---.  \
| |-------------------+                   |   |||  |
| |                                       |   |||  |
| |         +-------------------+---------|   |||  |
| |         |     tag A''xD     |         | < |||  |
| |---------+-------------------+         |  ||||  +-- 3rd commit
| |                data D                 |  ||||  |
| |                             +---------|  ||||  |
| |                             |   tag Dx|  ||||  |
| |---------+-------------------+---------|  ||||  |
| |CRC      |        CRC        |         |  ||||  /
| |---------+-------------------+         |  ||||
| |           unwritten storage           |  ||||  more commits
| |                                       |  ||||       |
| |                                       |  ||||       v
| |                                       |  ||||
| |                                       |  ||||
| '---------------------------------------'  ||||
'---------------------------------------'    |||'- most recent A
                                             ||'-- most recent B
                                             |'--- most recent C
                                             '---- most recent D
```

Two things to note before we get into the details around tag encoding:

1. Each tag contains a valid bit used to indicate if the tag and containing
   commit is valid. After XORing, this bit should always be zero.

   At the end of each commit, the valid bit of the previous tag is XORed
   with the lowest bit in the type field of the CRC tag. This allows
   the CRC tag to force the next commit to fail the valid bit test if it
   has not yet been written to.

2. The valid bit alone is not enough info to know if the next commit has been
   erased. We don't know the order bits will be programmed in a program block,
   so it's possible that the next commit had an attempted program that left the
   valid bit unchanged.

   To ensure we only ever program erased bytes, each commit can contain an
   optional forward-CRC (FCRC). An FCRC contains a checksum of some amount of
   bytes in the next commit at the time it was erased.

   ```
   .-------------------. \      \
   |  revision count   | |      |
   |-------------------| |      |
   |     metadata      | |      |
   |                   | +---.  +-- current commit
   |                   | |   |  |
   |-------------------| |   |  |
   |       FCRC       ---|-. |  |
   |-------------------| / | |  |
   |        CRC       -----|-'  /
   |-------------------|   |
   |      padding      |   |        padding (does't need CRC)
   |                   |   |
   |-------------------| \ |    \
   |      erased?      | +-'    |
   |         |         | |      +-- next commit
   |         v         | /      |
   |                   |        /
   |                   |
   '-------------------'
   ```

   If the FCRC is missing or the checksum does not match, we must assume a
   commit was attempted but failed due to power-loss.

   Note that end-of-block commits do not need an FCRC.
