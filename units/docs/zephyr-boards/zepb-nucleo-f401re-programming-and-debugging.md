---
id: "zepb-nucleo-f401re-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "nucleo_f401re: Programming and Debugging"
summary: "Nucleo F401RE board includes an ST-LINK/V2-1 embedded debug tool interface."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/st/nucleo_f401re/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/st/nucleo_f401re/doc/index.html#programming-and-debugging"
license: "Apache-2.0"
mode: "V"
---

Nucleo F401RE board includes an ST-LINK/V2-1 embedded debug tool interface.

Applications for the `nucleo_f401re` board configuration can be built and
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

#### Flashing an application to Nucleo F401RE


Connect the Nucleo F401RE to your host computer using the USB port,
then run a serial host program to connect with your Nucleo board:

```console

$ minicom -D /dev/ttyACM0
```
Now build and flash an application. Here is an example for
hello_world.

You should see the following message on the console:

```console

Hello World! arm
```

### Debugging


You can debug an application in the usual way.  Here is an example for the
hello_world application.

.. _STM32F401RE on www.st.com:
   https://www.st.com/en/microcontrollers/stm32f401re.html
