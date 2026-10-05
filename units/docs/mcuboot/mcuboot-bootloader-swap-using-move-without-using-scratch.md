---
id: "mcuboot-bootloader-swap-using-move-without-using-scratch"
type: "concept"
domain: "boot-update"
title: "Bootloader: Image slots / Swap using move (without using scratch)"
summary: "Please note that the swap-using-offset algorithm is preferred over swap-using-move except when building for existing products already using the latter."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/design.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/design.md#swap-using-move-without-using-scratch"
license: "Apache-2.0"
mode: "V"
---

_Part of: Image slots_

Please note that the swap-using-offset algorithm is preferred over swap-using-move
except when building for existing products already using the latter.

This algorithm is an alternative to the swap-using-scratch algorithm.
It uses an additional sector in the primary slot to make swap possible.
The algorithm works as follows:

  1.	Moves all sectors of the primary slot up by one sector.
    Beginning from N=0:
  2.	Copies the N-th sector from the secondary slot to the N-th sector of the
  primary slot.
  3.	Copies the (N+1)-th sector from the primary slot to the N-th sector of the
  secondary slot.
  4.	Repeats steps 2. and 3. until all the slots' sectors are swapped.

This algorithm is designed so that the higher sector of the primary slot is
used only for allowing sectors to move up. Therefore the most
memory-size-effective slot layout is when the primary slot is larger than
the secondary slot by exactly one sector plus the size of the swap status area,
rounded up to the total size of the sectors it occupies,
although same-sized slots are allowed as well.
The algorithm is limited to support sectors of the same
sector layout. All slot's sectors should be of the same size.

When using this algorithm the maximum image size available for the application
will be:
```
maximum-image-size = (N-1) * slot-sector-size - image-trailer-sectors-size
```

Where:
  `N` is the number of sectors in the primary slot.
  `image-trailer-sectors-size` is the size of the image trailer rounded up to
  the total size of sectors its occupied. For instance if the image-trailer-size
  is equal to 1056 B and the sector size is equal to 1024 B, then
  `image-trailer-sectors-size` will be equal to 2048 B.

This does imply, if there is any doubt, that the primary slot will be exactly
one sector larger than the secondary slot due to the swap sector alone. It is
the case that both the primary and secondary slots both have a trailer in
addition to the application payload and these trailers are identical in size
to one another.

The algorithm does two erase cycles on the primary slot and one on the secondary
slot during each swap. Assuming that receiving a new image by the DFU
application requires 1 erase cycle on the secondary slot, this should result in
leveling the flash wear between the slots.

The algorithm is enabled using the `MCUBOOT_SWAP_USING_MOVE` option.
