---
id: "mcuboot-bootloader-swap-using-scratch-image-swap-using-scra"
type: "concept"
domain: "boot-update"
title: "Bootloader: [Image slots](#image-slots) / [Swap using scratch](#image-swap-using-scratch)"
summary: "Please note that the swap-using-scratch algorithm may be removed in the coming future."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/design.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/design.md#swap-using-scratch-image-swap-using-scratch"
license: "Apache-2.0"
mode: "V"
---

_Part of: [Image slots](#image-slots)_

Please note that the swap-using-scratch algorithm may be removed in the coming
future.

When swap-using-scratch algorithm is used, in addition to the slots of
image areas, the bootloader requires a scratch area to allow for reliable
image swapping. The scratch area must have a size
that is enough to store at least the largest sector that is going to be swapped.
Many devices have small equally sized flash sectors, eg 4K, while others have
variable sized sectors where the largest sectors might be 128K or 256K, so the
scratch must be big enough to store that. The scratch is only ever used when
swapping firmware, which means only when doing an upgrade. Given that, the main
reason for using a larger size for the scratch is that flash wear will be more
evenly distributed, because a single sector would be written twice the number of
times than using two sectors, for example. To evaluate the ideal size of the
scratch for your use case the following parameters are relevant:

* the ratio of image size / scratch size
* the number of erase cycles supported by the flash hardware

The image size is used (instead of slot size) because only the slot's sectors
that are actually used for storing the image are copied. The image/scratch ratio
is the number of times the scratch will be erased on every upgrade. The number
of erase cycles divided by the image/scratch ratio will give you the number of
times an upgrade can be performed before the device goes out of spec.

```
num_upgrades = number_of_erase_cycles / (image_size / scratch_size)
```

Let's assume, for example, a device with 10000 erase cycles, an image size of
150K and a scratch of 4K (usual minimum size of 4K sector devices). This would
result in a total of:

`10000 / (150 / 4) ~ 267`

Increasing the scratch to 16K would give us:

`10000 / (150 / 16) ~ 1067`

There is no *best* ratio, as the right size is use-case dependent. Factors to
consider include the number of times a device will be upgraded both in the field
and during development, as well as any desired safety margin on the
manufacturer's specified number of erase cycles. In general, using a ratio that
allows hundreds to thousands of field upgrades in production is recommended.

swap-using scratch algorithm assumes that the primary and the secondary image
slot areas sizes are equal.
The maximum image size available for the application
will be:
```
maximum-image-size = image-slot-size - image-trailer-size
```

Where:
  `image-slot-size` is the size of the image slot.
  `image-trailer-size` is the size of the image trailer.
