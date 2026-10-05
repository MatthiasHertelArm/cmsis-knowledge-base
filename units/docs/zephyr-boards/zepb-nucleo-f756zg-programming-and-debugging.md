---
id: "zepb-nucleo-f756zg-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "nucleo_f756zg: Programming and Debugging"
summary: "Nucleo F756ZG board includes an ST-LINK/V2-1 embedded debug tool interface."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/st/nucleo_f756zg/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/st/nucleo_f756zg/doc/index.html#programming-and-debugging"
license: "Apache-2.0"
mode: "V"
---

Nucleo F756ZG board includes an ST-LINK/V2-1 embedded debug tool interface.

Applications for the `nucleo_f756zg` board configuration can be built and
flashed in the usual way (see build_an_application and
application_run for more details).


### Flashing


The board is configured to be flashed using west STM32CubeProgrammer runner,
so its installation is required.

Alternatively, OpenOCD or JLink can also be used to flash the board using
the `--runner` (or `-r`) option:

```console

$ west flash --runner openocd
$ west flash --runner jlink
```

#### Flashing an application to Nucleo F756ZG


Here is an example for the hello_world application.

Run a serial host program to connect with your Nucleo board.

```console

$ minicom -b 115200 -D /dev/ttyACM0
```
Build and flash the application:

You should see the following message on the console:

```console

$ Hello World! nucleo_f756zg
```

### Debugging


You can debug an application in the usual way.  Here is an example for the
hello_world application.

.. _STM32F756ZG on www.st.com:
   https://www.st.com/content/st_com/en/products/microcontrollers/stm32-32-bit-arm-cortex-mcus/stm32-high-performance-mcus/stm32f7-series/stm32f7x6/stm32f756zg.html
