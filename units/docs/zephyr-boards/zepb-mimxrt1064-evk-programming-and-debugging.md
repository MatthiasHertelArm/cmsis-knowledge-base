---
id: "zepb-mimxrt1064-evk-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "mimxrt1064_evk: Programming and Debugging"
summary: "This board supports 3 debug host tools. Please install your preferred host tool, then follow the instructions in Configuring a Debug Probe to configure the board appropriately."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/nxp/mimxrt1064_evk/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/nxp/mimxrt1064_evk/doc/index.html#programming-and-debugging"
license: "Apache-2.0"
mode: "V"
---

This board supports 3 debug host tools. Please install your preferred host
tool, then follow the instructions in Configuring a Debug Probe to
configure the board appropriately.

* jlink-debug-host-tools (Supported by NXP)
* linkserver-debug-host-tools (Supported by NXP)
* pyocd-debug-host-tools (Not supported by NXP)

Once the host tool and board are configured, build and flash applications
as usual (see build_an_application and application_run for more
details).


### Configuring a Debug Probe



**Note:** * To boot from the QSPI flash, make sure SW7 is set to 0010 and SW5 is set to 0000. * When the device transitions into low power states, the debugger may be unable to access the chip. Use caution when enabling `CONFIG_PM`, and if the debugger cannot flash the part, see Troubleshooting RT1064

For the RT1064, J47/J48 are the SWD isolation jumpers, J42 is the DFU
mode jumper, and J21 is the 20 pin JTAG/SWD header.

See Using J-Link with MIMXRT1060-EVK or MIMXRT1064-EVK for more
details.


### Configuring a Console


Regardless of your choice in debug probe, we will use the OpenSDA
microcontroller as a usb-to-serial adapter for the serial console. Check that
jumpers J45 and J46 are **on** (they are on by default when boards ship from
the factory) to connect UART signals to the OpenSDA microcontroller.

Connect a USB cable from your PC to J41.

Use the following settings with your serial terminal of choice (minicom, putty,
etc.):

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1


#### Using SWO

SWO can be used as a logging backend, by setting `CONFIG_LOG_BACKEND_SWO=y`.
Your SWO viewer should be configured with a CPU frequency of 132MHz, and
SWO frequency of 7500KHz.


### Flashing


Here is an example for the hello_world application.

Open a serial terminal, reset the board (press the SW9 button), and you should
see the following message in the terminal:

```console

***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! mimxrt1064_evk
```

### Debugging


Here is an example for the hello_world application.

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```console

***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! mimxrt1064_evk
```

### Troubleshooting


If the debug probe fails to connect with the following error, it's possible
that the boot header in QSPI flash is invalid or corrupted. The boot header is
configured by `CONFIG_NXP_IMXRT_BOOT_HEADER`.

```console

Remote debugging using :2331
Remote communication error.  Target disconnected.: Connection reset by peer.
"monitor" command not supported by this target.
"monitor" command not supported by this target.
You can't do that when your target is `exec'
(gdb) Could not connect to target.
Please check power, connection and settings.
```
You can fix it by erasing and reprogramming the QSPI flash with the following
steps:

#. Set the SW7 DIP switches to ON-OFF-ON-OFF to prevent booting from QSPI flash.

#. Reset by pressing SW9

#. Run `west debug` or `west flash` again with a known working Zephyr
   application.

#. Set the SW7 DIP switches to OFF-OFF-ON-OFF to boot from QSPI flash.

#. Reset by pressing SW9

If the west flash or debug commands fail, and the command hangs while executing
runners.jlink, confirm the J-Link debug probe is configured, powered, and
connected to the EVK properly.

.. _i.MX RT1064 Website:
   https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/i.mx-applications-processors/i.mx-rt-series/i.mx-rt1064-crossover-processor-with-arm-cortex-m7-core:i.MX-RT1064

.. _i.MX RT1064 Datasheet:
   https://www.nxp.com/docs/en/data-sheet/IMXRT1064CEC.pdf

.. _i.MX RT1064 Reference Manual:
   https://www.nxp.com/webapp/Download?colCode=IMXRT1064RM
