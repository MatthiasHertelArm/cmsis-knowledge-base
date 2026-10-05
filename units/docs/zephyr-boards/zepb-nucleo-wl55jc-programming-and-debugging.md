---
id: "zepb-nucleo-wl55jc-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "nucleo_wl55jc: Programming and Debugging"
summary: "Nucleo WL55JC board includes an STLINK-V3 embedded debug tool interface."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/st/nucleo_wl55jc/doc/nucleo_wl55jc.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/st/nucleo_wl55jc/doc/index.html#programming-and-debugging"
license: "Apache-2.0"
mode: "V"
---

Nucleo WL55JC board includes an STLINK-V3 embedded debug tool interface.

Applications for the `nucleo_wl55jc` board configuration can be built the
usual way (see build_an_application).


### Flashing


The board is configured to be flashed using west STM32CubeProgrammer runner,
so its installation is required.

Alternatively, OpenOCD can also be used to flash the board using
the `--runner` (or `-r`) option:

```console

$ west flash --runner openocd
```

#### Flashing an application to Nucleo WL55JC


Connect the Nucleo WL55JC to your host computer using the USB port.
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
.. Note:

   Nucleo WL55JC board is provided with a stock firmware which demonstrates
   sleep mode. Unfortunately, default openocd configuration, which is debug
   compatible, doesn't allow flashing when SoC is in sleep mode.
   As a consequence, when flashing Nucleo WL55JC board over a stock firmware,
   please update board's openocd.cfg configuration file to select sleep mode
   compatible configuration.


### Debugging


You can debug an application in the usual way.  Here is an example for the
blinky application.

.. _STM32WL55JC on www.st.com:
   https://www.st.com/en/microcontrollers-microprocessors/stm32wl55jc.html
