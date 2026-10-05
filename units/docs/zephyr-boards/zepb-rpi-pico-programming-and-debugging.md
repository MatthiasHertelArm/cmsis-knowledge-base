---
id: "zepb-rpi-pico-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "rpi_pico: Programming and Debugging"
summary: "Applications for the rpi_pico board configuration can be built and flashed in the usual way (see build_an_application and application_run for more details)."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/raspberrypi/rpi_pico/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/raspberrypi/rpi_pico/doc/index.html#programming-and-debugging"
license: "Apache-2.0"
mode: "V"
---

Applications for the `rpi_pico` board configuration can be built and
flashed in the usual way (see build_an_application and
application_run for more details).

Several debugging tools support the Raspberry Pi Pico.
The Raspberry Pi Debug Probe is an easy-to-obtain CMSIS-DAP adapter
officially provided by the Raspberry Pi Foundation,
making it a convenient choice for debugging `rpi_pico`.
It can be used with `openocd` or `pyocd`.



### Flashing


The `rpi_pico` can flash with Zephyr's standard method.
See also Building, Flashing and Debugging.


#### Using OpenOCD


To use a debugging adapter such as the Raspberry Pi Debug Probe,
You must configure **udev**. Refer to setting-udev-rules for details.

The Raspberry Pi Pico has an SWD interface that can be used to program
and debug the onboard SoC. This interface can be used with OpenOCD.
To use it, OpenOCD version 0.12.0 or later is needed.

If you are using a Debian based system (including Raspberry Pi OS, Ubuntu. and more),
using the pico_setup.sh script is a convenient way to set up the forked version of OpenOCD.

Here is an example of building and flashing the blinky application.

Set the flash runner option **--openocd** to `/usr/local/bin/openocd`. This should work
with the OpenOCD that was installed with the default configuration.
This configuration also works with an environment that is set up by the pico_setup.sh script.

In this sample, **RPI_PICO_DEBUG_ADAPTER** specifies which debug adapter is used for debugging.

If **RPI_PICO_DEBUG_ADAPTER** was not set, `cmsis-dap` is used by default.
The `raspberrypi-swd` and `jlink` are verified to work.
How to connect `cmsis-dap` and `raspberrypi-swd` is described in Getting Started with Raspberry Pi Pico.
Any other SWD debug adapter maybe also work with this configuration.

The value of **RPI_PICO_DEBUG_ADAPTER** is cached, so it can be omitted from
`west flash` and `west debug` if it was previously set while running
`west build`.

**RPI_PICO_DEBUG_ADAPTER** is used in an argument to OpenOCD as `"source [find interface/${RPI_PICO_DEBUG_ADAPTER}.cfg]"`.
Thus, **RPI_PICO_DEBUG_ADAPTER** needs to be assigned the file name of the debug adapter.



#### Using JLink or other supported tools


You can Flash with a SEGGER J-Link debug probe as described in
Building, Flashing and Debugging.

Here is an example of building and flashing the blinky application.

You can also use other supported tools, such as Black Magic Probe,
by changing the `-- runner` option.



#### Using UF2


If you don't have an SWD adapter, you can flash the Raspberry Pi Pico with
a UF2 file. By default, building an app for this board will generate a
`build/zephyr/zephyr.uf2` file. If the Pico is powered on with the `BOOTSEL`
button pressed, it will appear on the host as a mass storage device.
Run the following command, or drag-and-drop the uf2 file to the device,
which will flash the Pico.


### Debugging


Like flashing, debugging can also be performed using Zephyr's standard method
(see application_run).
The following sample demonstrates how to debug using OpenOCD and
the Raspberry Pi Debug Probe.

The default debugging tool is `openocd`.
If you use a different tool, specify it with the `--runner`,
such as `jlink`.


.. _pico_setup.sh:
   https://raw.githubusercontent.com/raspberrypi/pico-setup/master/pico_setup.sh
