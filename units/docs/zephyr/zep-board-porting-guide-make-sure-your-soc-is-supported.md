---
id: "zep-board-porting-guide-make-sure-your-soc-is-supported"
type: "concept"
domain: "bring-up"
title: "Board Porting Guide: Make sure your SoC is supported"
summary: "Start by making sure your SoC is supported by Zephyr. If it is, it's time to create-your-board-directory. If you don't know, try:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/hardware/porting/board_porting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/hardware/porting/board_porting.rst"
license: "Apache-2.0"
mode: "V"
---

Start by making sure your SoC is supported by Zephyr. If it is, it's time to
create-your-board-directory. If you don't know, try:

- checking boards for names that look relevant, and reading individual
  board documentation to find out for sure.
- asking your SoC vendor

If you need to add a SoC, CPU cluster, or even architecture support, this is the
wrong page, but here is some general advice.


### Architecture


See architecture_porting_guide.


### CPU Core


CPU core support files go in `core` subdirectories under `arch`,
e.g. `arch/x86/core`.

See gs_toolchain for information about toolchains (compiler, linker,
etc.) supported by Zephyr. If you need to support a new toolchain,
build_overview is a good place to start learning about the build system.
Please reach out to the community if you are looking for advice or want to
collaborate on toolchain support.


### SoC


Zephyr SoC support files are in architecture-specific subdirectories of
`soc`. They are generally grouped by SoC family.

When adding a new SoC family or series for a vendor that already has SoC
support within Zephyr, please try to extract common functionality into shared
files to avoid duplication. If there is no support for your vendor yet, you can
add it in a new directory `zephyr/soc/<VENDOR>/<YOUR-SOC>`; please use
self-explanatory directory names.
