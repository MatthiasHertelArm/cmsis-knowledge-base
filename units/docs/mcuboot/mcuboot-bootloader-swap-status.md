---
id: "mcuboot-bootloader-swap-status"
type: "concept"
domain: "boot-update"
title: "Bootloader: Swap status"
summary: "The swap status region allows the bootloader to recover in case it restarts in the middle of an image swap operation. The swap status region consists of a series of single-byte records."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@725d63c:docs/design.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/725d63c/docs/design.md#swap-status"
license: "Apache-2.0"
mode: "V"
---

The swap status region allows the bootloader to recover in case it restarts in
the middle of an image swap operation.  The swap status region consists of a
series of single-byte records.  These records are written independently, and
therefore must be padded according to the minimum write size imposed by the
flash hardware.  The structure of the swap status region is illustrated below.
In this figure, a min-write-size of 1 is assumed for simplicity, this diagram
shows 3 states per sector which is applicable to swap using scratch and swap
using move, however in swap using offset mode there are only 2 states per
sector and the overall state size required is less.

```
     0                   1                   2                   3
     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |sec127,state 0 |sec127,state 1 |sec127,state 2 |sec126,state 0 |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |sec126,state 1 |sec126,state 2 |sec125,state 0 |sec125,state 1 |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |sec125,state 2 |                                               |
    +-+-+-+-+-+-+-+-+                                               +
    ~                                                               ~
    ~               [Records for indices 124 through 1              ~
    ~                                                               ~
    ~               +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    ~               |sec000,state 0 |sec000,state 1 |sec000,state 2 |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

The above is probably not helpful at all; here is a description in English.

Each image slot is partitioned into a sequence of flash sectors.  If we were to
enumerate the sectors in a single slot, starting at 0, we would have a list of
sector indices.  Since there are two image slots, each sector index would
correspond to a pair of sectors.  For example, sector index 0 corresponds to
the first sector in the primary slot and the first sector in the secondary slot.
Finally, reverse the list of indices such that the list starts with index
`BOOT_MAX_IMG_SECTORS - 1` and ends with 0.  The swap status region is a
representation of this reversed list.

During a swap operation, each sector index transitions through four separate
states:
```
0. primary slot: image 0,   secondary slot: image 1,   scratch: N/A
1. primary slot: image 0,   secondary slot: N/A,       scratch: image 1 (1->s, erase 1)
2. primary slot: N/A,       secondary slot: image 0,   scratch: image 1 (0->1, erase 0)
3. primary slot: image 1,   secondary slot: image 0,   scratch: N/A     (s->0)
```

Each time a sector index transitions to a new state, the bootloader writes a
record to the swap status region.  Logically, the bootloader only needs one
record per sector index to keep track of the current swap state.  However, due
to limitations imposed by flash hardware, a record cannot be overwritten when
an index's state changes.  To solve this problem, the bootloader uses three
records per sector index rather than just one.

Each sector-state pair is represented as a set of three records.  The record
values map to the above four states as follows

```
            | rec0 | rec1 | rec2
    --------+------+------+------
    state 0 | 0xff | 0xff | 0xff
    state 1 | 0x01 | 0xff | 0xff
    state 2 | 0x01 | 0x02 | 0xff
    state 3 | 0x01 | 0x02 | 0x03
```

The swap status region can accommodate `BOOT_MAX_IMG_SECTORS` sector indices.
Hence, the size of the region, in bytes, is
`BOOT_MAX_IMG_SECTORS * min-write-size * s` where `s` is 3 for swap using
scratch and swap using move modes, and is 2 for swap using offset mode. The
only requirement for the index count is that it is great enough to account
for a maximum-sized image (i.e., at least as great as the total sector count in
an image slot).  If a device's image slots have been configured with
`BOOT_MAX_IMG_SECTORS: 128` and use less than 128 sectors, the first record
that gets written will be somewhere in the middle of the region. For example,
if a slot uses 64 sectors, the first sector index that gets swapped is 63,
which corresponds to the exact halfway point within the region.

---
***Note***

*Since the scratch area only ever needs to record swapping of the last*
*sector, it uses at most min-write-size * 3 bytes for its own status area.*

---
