---
id: "mcuboot-building-and-using-mcuboot-with-ze-building-the-bootloader-itself-manually"
type: "concept"
domain: "boot-update"
title: "Building and using MCUboot with Zephyr: Building the bootloader itself (manually)"
summary: "The bootloader is an ordinary Zephyr application, at least from Zephyr's point of view. There is a bit of configuration that needs to be made before building it."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@725d63c:docs/readme-zephyr.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/725d63c/docs/readme-zephyr.md#building-the-bootloader-itself-manually"
license: "Apache-2.0"
mode: "V"
---

The bootloader is an ordinary Zephyr application, at least from
Zephyr's point of view.  There is a bit of configuration that needs to
be made before building it.  Most of this can be done as documented in
the `CMakeLists.txt` file in boot/zephyr.  There are comments there for
guidance.  It is important to select a signature algorithm, and decide
if the primary slot should be validated on every boot.

To build MCUboot, use west:

```
  cd boot/zephyr
  west build -b <board>
```

In addition to the partitions defined in DTS, some additional
information about the flash layout is currently required to build
MCUboot itself. All the needed configuration is collected in
`boot/zephyr/include/target.h`. Depending on the board, this information
may come from board-specific headers, Device Tree, or be configured by
MCUboot on a per-SoC family basis.

After building the bootloader, the binaries should reside in
`build/zephyr/zephyr.{bin,hex,elf}`, where `build` is the build
directory you chose when running `west build`. Use `west flash`
to flash these binaries from the build directory. Depending
on the target and flash tool used, this might erase the whole of the flash
memory (mass erase) or only the sectors where the bootloader resides prior to
programming the bootloader image itself.
