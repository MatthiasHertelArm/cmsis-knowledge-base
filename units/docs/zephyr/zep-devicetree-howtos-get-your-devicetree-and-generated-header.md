---
id: "zep-devicetree-howtos-get-your-devicetree-and-generated-header"
type: "concept"
domain: "project"
title: "Devicetree HOWTOs: Get your devicetree and generated header"
summary: "A board's devicetree (BOARD.dts) pulls in common node definitions via #include preprocessor directives. This at least includes the SoC's .dtsi. One way to figure out the devicetree's contents is by opening these files, e.g."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/howtos.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/howtos.rst"
license: "Apache-2.0"
mode: "V"
---

A board's devicetree (BOARD.dts) pulls in
common node definitions via `#include` preprocessor directives. This at least
includes the SoC's `.dtsi`. One way to figure out the devicetree's contents
is by opening these files, e.g. by looking in
`dts/<ARCH>/<vendor>/<soc>.dtsi`, but this can be time consuming.

If you just want to see the "final" devicetree for your board, build an
application and open the `zephyr.dts` file in the build directory.


**Tip:** You can build hello_world to see the "base" devicetree for your board without any additional changes from overlay files.

For example, using the qemu_cortex_m3 board to build
hello_world:

```sh

# --cmake-only here just forces CMake to run, skipping the
# build process to save time.
west build -b qemu_cortex_m3 samples/hello_world --cmake-only
```
You can change `qemu_cortex_m3` to match your board.

CMake prints the input and output file locations like this:

```none

-- Found BOARD.dts: .../zephyr/boards/arm/qemu_cortex_m3/qemu_cortex_m3.dts
-- Generated zephyr.dts: .../zephyr/build/zephyr/zephyr.dts
-- Generated devicetree_generated.h: .../zephyr/build/zephyr/include/generated/zephyr/devicetree_generated.h
```
The `zephyr.dts` file is the final devicetree in DTS format.

The `devicetree_generated.h` file is the corresponding generated header.

See devicetree-in-out-files for details about these files.
