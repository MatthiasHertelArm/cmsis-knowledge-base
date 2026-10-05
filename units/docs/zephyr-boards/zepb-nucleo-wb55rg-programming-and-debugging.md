---
id: "zepb-nucleo-wb55rg-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "nucleo_wb55rg: Programming and Debugging"
summary: "Nucleo WB55RG board includes an ST-LINK/V2-1 embedded debug tool interface."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/st/nucleo_wb55rg/doc/nucleo_wb55rg.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/st/nucleo_wb55rg/doc/index.html#programming-and-debugging"
license: "Apache-2.0"
mode: "V"
---

Nucleo WB55RG board includes an ST-LINK/V2-1 embedded debug tool interface.

Applications for the `nucleo_wb55rg` board configuration can be built the
usual way (see build_an_application).


### Flashing


The board is configured to be flashed using west STM32CubeProgrammer runner,
so its installation is required.

Alternatively, OpenOCD or pyOCD can also be used to flash the board using
the `--runner` (or `-r`) option:

```console

$ west flash --runner openocd
$ west flash --runner pyocd
```
If you prefer, you can use pyOCD, but it requires to enable "pack" support with
the following pyOCD command:

```console

$ pyocd pack --update
$ pyocd pack --install stm32wb55rg
```

#### Flashing an application to Nucleo WB55RG


Connect the Nucleo WB55RG to your host computer using the USB port.
Then build and flash an application. Here is an example for the
hello_world application.

Run a serial host program to connect with your Nucleo board:

```console

$ minicom -D /dev/ttyUSB0
```
Then build and flash the application.

You should see the following message on the console:

```console

Hello World! arm
```

### Debugging


You can debug an application in the usual way.  Here is an example for the
blinky application.

.. _STM32WB55RG on www.st.com:
   https://www.st.com/en/microcontrollers-microprocessors/stm32wb55rg.html
