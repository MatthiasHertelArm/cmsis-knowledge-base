---
id: "zepb-nucleo-h743zi-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "nucleo_h743zi: Programming and Debugging"
summary: "Nucleo H743ZI board includes an ST-LINK/V2-1 embedded debug tool interface."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/st/nucleo_h743zi/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/st/nucleo_h743zi/doc/index.html#programming-and-debugging"
license: "Apache-2.0"
mode: "V"
---

Nucleo H743ZI board includes an ST-LINK/V2-1 embedded debug tool interface.

Applications for the `nucleo_h743zi` board configuration can be built and
flashed in the usual way (see build_an_application and
application_run for more details).


### Flashing


The board is configured to be flashed using west STM32CubeProgrammer runner,
so its installation is required.

Alternatively, OpenOCD, JLink or pyOCD can also be used to flash the board using
the `--runner` (or `-r`) option:

```console

$ west flash --runner openocd
$ west flash --runner jlink
$ west flash --runner pyocd
```

#### Flashing an application to Nucleo H743ZI


Here is an example for the hello_world application.

Run a serial host program to connect with your Nucleo board.

```console

$ minicom -b 115200 -D /dev/ttyACM0
```
Build and flash the application:

You should see the following message on the console:

```console

$ Hello World! nucleo_h743zi
```

### Debugging


You can debug an application in the usual way.  Here is an example for the
hello_world application.

.. _STM32H743ZI on www.st.com:
   https://www.st.com/content/st_com/en/products/microcontrollers-microprocessors/stm32-32-bit-arm-cortex-mcus/stm32-high-performance-mcus/stm32h7-series/stm32h743-753/stm32h743zi.html
