---
id: "zepb-nucleo-f429zi-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "nucleo_f429zi: Programming and Debugging"
summary: "The Nucleo F429ZI board includes an ST-LINK/V2-1 embedded debug tool interface."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/st/nucleo_f429zi/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/st/nucleo_f429zi/doc/index.html#programming-and-debugging"
license: "Apache-2.0"
mode: "V"
---

The Nucleo F429ZI board includes an ST-LINK/V2-1 embedded debug tool interface.


### Flashing


The board is configured to be flashed using west STM32CubeProgrammer runner,
so its installation is required.

Alternatively, OpenOCD or JLink can also be used to flash the board using
the `--runner` (or `-r`) option:

```console

$ west flash --runner openocd
$ west flash --runner jlink
```
