---
id: "zepb-nucleo-g474re-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "nucleo_g474re: Programming and Debugging"
summary: "Nucleo G474RE board includes an ST-LINK/V3E embedded debug tool interface."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/st/nucleo_g474re/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/st/nucleo_g474re/doc/index.html#programming-and-debugging"
license: "Apache-2.0"
mode: "V"
---

Nucleo G474RE board includes an ST-LINK/V3E embedded debug tool interface.

Applications for the `nucleo_g474re` board configuration can be built and
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

#### Flashing an application to Nucleo G474RE


Connect the Nucleo G474RE to your host computer using the USB port,
then run a serial host program to connect with your Nucleo board.

```console

$ minicom -D /dev/ttyACM0
```
Now build and flash an application. Here is an example for
hello_world.

You should see the following message on the console:

```console

$ Hello World! arm
```

### Debugging


You can debug an application in the usual way.  Here is an example for the
hello_world application.

.. _STM32G474RE on www.st.com:
   https://www.st.com/en/microcontrollers/stm32g474re.html
