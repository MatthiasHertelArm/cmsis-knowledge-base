---
id: "mcuboot-building-and-using-mcuboot-with-ze-using-swap-using-scratch-flash-algorithm"
type: "concept"
domain: "boot-update"
title: "Building and using MCUboot with Zephyr: Using swap-using-scratch flash algorithm"
summary: "Note: This mode is not recommended for use and swap-using-offset or swap-using-move are recommended instead."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/readme-zephyr.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/readme-zephyr.md#using-swap-using-scratch-flash-algorithm"
license: "Apache-2.0"
mode: "V"
---

Note: This mode is not recommended for use and swap-using-offset or
swap-using-move are recommended instead. Swap-using-scratch is required to be
used if the primary and secondary slots have different sector sizes, or if
either slot's sector sizes are not uniform over the whole NVM area.

To use the swap-using-scratch flash algorithm, a scratch partition needs to be
present for the target board which is used for holding the data being swapped
from both slots, this section must be at least as big as the largest sector
size of the 2 partitions (e.g. if a device has a primary slot in main flash
with a sector size of 512 bytes and secondar slot in external off-chip flash
with a sector size of 4KB then the scratch area must be at least 4KB in size).
The number of sectors must also be evenly divisable by this sector size, e.g.
4KB, 8KB, 12KB, 16KB are allowed, 7KB, 7.5KB are not. This scratch partition
needs adding to the .dts file for the board, e.g. for the nrf52dk_nrf52832
board thus would involve updating
`<zephyr>/boards/nordic/nrf52dk/nrf52dk_nrf52832.dts` with:

```
    boot_partition: partition@0 {
            compatible = "zephyr,mapped-partition";
            label = "mcuboot";
            reg = <0x00000000 0xc000>;
    };

    slot0_partition: partition@c000 {
            compatible = "zephyr,mapped-partition";
            label = "image-0";
            reg = <0x0000C000 0x37000>;
    };

    slot1_partition: partition@43000 {
            compatible = "zephyr,mapped-partition";
            label = "image-1";
            reg = <0x00043000 0x37000>;
    };

    scratch_partition: partition@7a000 {
            compatible = "zephyr,mapped-partition";
            label = "image-scratch";
            reg = <0x0007a000 0x00006000>;
    };
```

Which would make the application size 220KB and scratch size 24KB (the nRF52832
has a 4KB sector size so the size of the scratch partition can be reduced at
the cost of vastly reducing flash lifespan, e.g. for a 32KB firmware update
with an 8KB scratch area, the scratch area would be erased and programmed 8
times per image upgrade/revert). To configure MCUboot to work in
swap-using-scratch mode, the Kconfig value must be set when building it:
`CONFIG_BOOT_SWAP_USING_SCRATCH=y`.

Note that it is possible for an application to get into a stuck state when
swap-using-scratch is used whereby an application has loaded a firmware update
and marked it as test/confirmed but MCUboot will not swap the images and
erasing the secondary slot from the zephyr application returns an error
because the slot is marked for upgrade.
