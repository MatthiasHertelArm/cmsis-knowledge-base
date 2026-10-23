---
id: "zep-board-porting-guide-board-terminology"
type: "concept"
domain: "bring-up"
title: "Board Porting Guide: Board terminology"
summary: "The previous section introduced the hierarchical manner in which Zephyr classifies and implements hardware support. This section focuses on the terminology used around hardware support, and in particular when defining and working with boards and SoCs."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/hardware/porting/board_porting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/hardware/porting/board_porting.rst"
license: "Apache-2.0"
mode: "V"
---

The previous section introduced the hierarchical manner in which Zephyr
classifies and implements hardware support.
This section focuses on the terminology used around hardware support, and in
particular when defining and working with boards and SoCs.

The overall set of terms used around the concept of board in Zephyr is depicted
in the image below, which uses the bl5340_dvk board as reference.

The diagram shows the different terms that are used to describe boards:

- The `board name`: `bl5340_dvk`
- The optional `board revision`: `1.2.0`
- The `board qualifiers`, that optionally describe the `SoC`,
  `CPU cluster` and `variant`: `nrf5340/cpuapp/ns`
- The `board target`, which uniquely identifies a combination of the above
  and can be used to specify the hardware to build for when using the tooling
  provided by Zephyr: `bl5340_dvk@1.2.0/nrf5340/cpuapp/ns`

Formally this can also be seen as
`{board name}[@{revision}][/{board qualifiers}]`, which can be extended to
`{board name}[@{revision}][/{SoC}[/{CPU cluster}][/{variant}]]`.

If a board contains only one single-core SoC, then the SoC can be omitted from
the board target. This implies that if the board does not define any board
qualifiers, the board name can be used as a board target. Conversely, if
board qualifiers are part of the board definition, then the SoC can be omitted
by leaving it out but including the corresponding forward-slashes: `//`.

Continuing with the example above, The board bl5340_dvk is a single SoC
board where the SoC defines two CPU clusters: `cpuapp` and `cpunet`. One of
the CPU clusters, `cpuapp`, additionally defines a non-secure board variant,
`ns`.

The board qualifiers `nrf5340/cpuapp/ns` can be read as:


- `nrf5340`: The SoC, which is a Nordic nRF5340 dual-core SoC
- `cpuapp`: The CPU cluster `cpuapp`, which consists of a single Cortex-M33
  CPU core. The number of cores in a CPU cluster cannot be determined from the
  board qualifiers.
- `ns`: a variant, in this case `ns` is a common variant name in
  Zephyr denoting a non-secure build for boards supporting tfm.

Not all SoCs define CPU clusters or variants. For example a simple board
like the thingy52 contains a single SoC with no CPU clusters and
no variants.
For `thingy52` the board target `thingy52/nrf52832` can be read as:

- `thingy52`: board name.
- `nrf52832`: The board qualifiers, in this case identical to the SoC, which
  is a Nordic nRF52832.
