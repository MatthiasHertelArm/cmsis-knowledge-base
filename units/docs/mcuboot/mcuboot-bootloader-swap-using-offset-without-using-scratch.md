---
id: "mcuboot-bootloader-swap-using-offset-without-using-scratch"
type: "concept"
domain: "boot-update"
title: "Bootloader: Image slots / Swap using offset (without using scratch)"
summary: "This algorithm is an alternative to the swap-using-scratch algorithm and an enhancement of the swap using move algorithm. It uses an additional sector in the secondary slot to make swap possible. The algorithm works as follows:"
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/design.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/design.md#swap-using-offset-without-using-scratch"
license: "Apache-2.0"
mode: "V"
---

_Part of: Image slots_

This algorithm is an alternative to the swap-using-scratch algorithm and an
enhancement of the swap using move algorithm.
It uses an additional sector in the secondary slot to make swap possible.
The algorithm works as follows:

  1.	Update image must be placed starting at the second sector in the secondary slot
  2.	Copies the N-th sector from the primary slot to the N-th sector of the
  secondary slot.
  3.	Copies the (N+1)-th sector from the secondary slot to the N-th sector of the
  primary slot.
  4.	Repeats steps 2. and 3. until all the slots' sectors are swapped.

This algorithm is designed so that the lower sector of the secondary slot is
used only for allowing sectors to move down during a swap. Therefore the most
memory-size-effective slot layout is when the secondary slot is larger than
the primary slot by exactly one sector, although same-sized slots are allowed
as well. The algorithm is limited to support sectors of the same sector layout.
All slot's sectors should be of the same size. This algorithm uses 2 flags per
sector update rather than the 3 flags used by swap using move, which requires
a smaller swap status area size.

When using this algorithm the maximum image size available for the application
will be:
```
maximum-image-size1 = N * slot-sector-size - image-trailer-sectors-size
```

Where:
  `N` is the number of sectors in the primary slot.
  `image-trailer-sectors-size` is the size of the image trailer rounded up to
  the total size of sectors its occupied. For instance if the image-trailer-size
  is equal to 1056 B and the sector size is equal to 1024 B, then
  `image-trailer-sectors-size` will be equal to 2048 B.

The algorithm does one erase cycle on both the primary and secondary slots
during each swap.

The algorithm is enabled using the `MCUBOOT_SWAP_USING_OFFSET` option.
