---
id: "zepb-nucleo-h563zi-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "nucleo_h563zi: Programming and Debugging"
summary: "Nucleo H563ZI board includes an ST-LINK/V3EC embedded debug tool interface. This probe allows to flash the board using various tools."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/st/nucleo_h563zi/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/st/nucleo_h563zi/doc/index.html#programming-and-debugging"
license: "Apache-2.0"
mode: "V"
---

Nucleo H563ZI board includes an ST-LINK/V3EC embedded debug tool interface.
This probe allows to flash the board using various tools.

Applications for the `nucleo_h563zi` board can be built and
flashed in the usual way (see build_an_application and
application_run for more details).


### OpenOCD Support


For now, openocd support  for stm32h5 is not available on upstream OpenOCD.
You can check OpenOCD official Github mirror.
In order to use it though, you should clone from the customized
STMicroelectronics OpenOCD Github and compile it following usual README guidelines.
Once it is done, you can set the OPENOCD and OPENOCD_DEFAULT_PATH variables in
`boards/st/nucleo_h563zi/board.cmake` to point the build
to the paths of the OpenOCD binary and its scripts,  before
including the common openocd.board.cmake file:

```none

set(OPENOCD "<path_to_openocd_repo>/src/openocd" CACHE FILEPATH "" FORCE)
set(OPENOCD_DEFAULT_PATH <path_to_opneocd_repo>/tcl)
include(${ZEPHYR_BASE}/boards/common/openocd.board.cmake)
```

### Flashing


The board is configured to be flashed using west STM32CubeProgrammer runner,
so its installation is required.

Alternatively, OpenOCD, JLink, or pyOCD can also be used to flash the board using
the `--runner` (or `-r`) option:

```console

$ west flash --runner openocd
$ west flash --runner pyocd
$ west flash --runner jlink
```
For pyOCD, additional target information needs to be installed.
This can be done by executing the following commands.

```console

$ pyocd pack --update
$ pyocd pack --install stm32h5
```

#### Flashing an application to Nucleo H563ZI


Connect the Nucleo H563ZI to your host computer using the USB port.
Then build and flash an application. Here is an example for the
hello_world application.

Run a serial host program to connect with your Nucleo board:

```console

$ minicom -D /dev/ttyACM0
```
Then build and flash the application.

You should see the following message on the console:

```console

Hello World! nucleo_h563zi
```

### Debugging


You can debug an application in the usual way.  Here is an example for the
blinky application.

.. _STM32H563ZI on www.st.com:
   https://www.st.com/en/microcontrollers/stm32h563zi.html
