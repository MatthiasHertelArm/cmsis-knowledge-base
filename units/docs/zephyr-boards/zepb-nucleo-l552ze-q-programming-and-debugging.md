---
id: "zepb-nucleo-l552ze-q-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "nucleo_l552ze_q: Programming and Debugging"
summary: "Nucleo L552ZE Q board includes an ST-LINK/V2-1 embedded debug tool interface."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/st/nucleo_l552ze_q/doc/nucleol552ze_q.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/st/nucleo_l552ze_q/doc/index.html#programming-and-debugging"
license: "Apache-2.0"
mode: "V"
---

Nucleo L552ZE Q board includes an ST-LINK/V2-1 embedded debug tool interface.

Applications for the `nucleo_l552ze_q` board configuration can be built and
flashed in the usual way (see build_an_application and
application_run for more details).


### Flashing


The board is configured to be flashed using west STM32CubeProgrammer runner,
so its installation is required.

Alternatively, OpenOCD or pyOCD can also be used to flash the board using
the `--runner` (or `-r`) option:

```console

$ west flash --runner openocd
$ west flash --runner pyocd
```
Support can be enabled for pyOCD by adding "pack" support with the
following pyOCD commands:

```console

$ pyocd pack --update
$ pyocd pack --install stm32l552ze
```

#### Flashing an application to Nucleo L552ZE Q


Connect the Nucleo L552ZE Q to your host computer using the USB port.
Then build and flash an application. Here is an example for the
hello_world application.

Run a serial host program to connect with your Nucleo board:

```console

$ minicom -D /dev/ttyACM0
```
Then build and flash the application.

You should see the following message on the console:

```console

Hello World! arm
```

### Debugging


You can debug an application in the usual way.  Here is an example for the
hello_world application.

.. _STM32L552ZE on www.st.com:
   https://www.st.com/en/microcontrollers/stm32l552ze.html
