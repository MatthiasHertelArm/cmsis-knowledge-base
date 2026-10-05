---
id: "zepb-nrf52840dk-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "nrf52840dk: Programming and Debugging"
summary: "Applications for the nrf52840dk/nrf52840 board configuration can be built, flashed, and debugged in the usual way. See build_an_application and application_run for more details on building and running."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/nordic/nrf52840dk/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/nordic/nrf52840dk/doc/index.html#programming-and-debugging"
license: "Apache-2.0"
mode: "V"
---

Applications for the `nrf52840dk/nrf52840` board configuration can be
built, flashed, and debugged in the usual way. See
build_an_application and application_run for more details on
building and running.

The nRF52840 DK supports programming and debugging external boards with
nRF51 Series or nRF52 Series System on Chip (SoC)s. For more information,
see the documentation on nRF52840 DK Debug output.


### Flashing


Follow the instructions in the nordic_segger page to install
and configure all the necessary software. Further information can be
found in nordic_segger_flashing. Then build and flash
applications as usual (see build_an_application and
application_run for more details).

Here is an example for the hello_world application.

First, run your favorite terminal program to listen for output.

```console

$ minicom -D <tty_device> -b 115200
```
Replace `<tty_device>` with the port where the board nRF52840 DK
can be found. For example, under Linux, `/dev/ttyACM0`.

Then build and flash the application in the usual way.


### Debugging


Refer to the nordic_segger page to learn about debugging Nordic boards with a
Segger IC.
