---
id: "mcuboot-building-and-using-mcuboot-with-ze"
type: "concept"
domain: "boot-update"
title: "Building and using MCUboot with Zephyr"
summary: "MCUboot began its life as the bootloader for Mynewt. It has since acquired the ability to be used as a bootloader for Zephyr as well."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@725d63c:docs/readme-zephyr.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/725d63c/docs/readme-zephyr.md"
license: "Apache-2.0"
mode: "V"
---

MCUboot began its life as the bootloader for Mynewt.  It has since
acquired the ability to be used as a bootloader for Zephyr as well.
There are some pretty significant differences in how apps are built
for Zephyr, and these are documented here.

Please see the [design document](https://github.com/mcu-tools/mcuboot/blob/725d63c/docs/design.md) for documentation on the design
and operation of the bootloader itself. This functionality should be the same
on all supported RTOSs.

The first step required for Zephyr is making sure your board has flash
partitions defined in its device tree. These partitions are:

- `boot_partition`: for MCUboot itself
- `slot0_partition`: the primary slot of Image 0
- `slot1_partition`: the secondary slot of Image 0

It is not recommended to use the swap-using-scratch algorithm of MCUboot, but
if this operating mode is desired then the following flash partition is also
needed (see end of this help file for details on creating a scratch partition
and how to use the swap-using-scratch algorithm):

- `scratch_partition`: the scratch slot

Currently, the two image slots must be contiguous. If you are running
MCUboot as your stage 1 bootloader, `boot_partition` must be configured
so your SoC runs it out of reset. If there are multiple updateable images
then the corresponding primary and secondary partitions must be defined for
the rest of the images too (for example, `slot2_partition` and
`slot3_partition` for Image 1).

The flash partitions are typically defined in the Zephyr boards folder, in a
file named `boards/<vendor>/<board>/<board>.dts`. An example `.dts` file with
flash partitions defined is the frdm_k64f's in
`boards/nxp/frdm_k64f/frdm_k64f.dts`. Make sure the DT node labels in your board's
`.dts` file match the ones used there.
