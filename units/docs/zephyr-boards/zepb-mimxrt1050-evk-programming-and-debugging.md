---
id: "zepb-mimxrt1050-evk-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "mimxrt1050_evk: Programming and Debugging"
summary: "This board supports 3 debug host tools."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/nxp/mimxrt1050_evk/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/nxp/mimxrt1050_evk/doc/index.html#programming-and-debugging"
license: "Apache-2.0"
mode: "V"
---

**Note:** Newer revisions of this board use lpc-link2-onboard-debug-probe, while older revisions use the opensda-onboard-debug-probe. Schematic revisions A/A1 use the K20 OpenSDA probe, and B/B1 use the LPC-Link2 LPC4322 probe.

This board supports 3 debug host tools. Please install your preferred host
tool, then follow the instructions in `Configuring a Debug Probe
(Schematic A/A1)`_ or Configuring a Debug Probe (Schematic B/B1),
depending on board schematic revision to configure the board appropriately.

* linkserver-debug-host-tools (Default, NXP Supported)
* jlink-debug-host-tools (NXP Supported)
* pyocd-debug-host-tools (Not supported by NXP)

Once the host tool and board are configured, build and flash applications
as usual (see build_an_application and application_run for more
details).


### Configuring a Debug Probe (Schematic A/A1)


For the RT1050 Schematic Rev A, J32/J33 are the SWD isolation jumpers, SW4 is
the reset button, and J21 is the 20 pin JTAG/SWD header.


### Configuring a Debug Probe (Schematic B/B1)


For the RT1050 Schematic Rev B, J47/J48 are the SWD isolation jumpers, J42 is
the DFU mode jumper, and J21 is the 20 pin JTAG/SWD header.


### Configuring a Console


Regardless of your choice in debug probe, we will use the OpenSDA
microcontroller as a usb-to-serial adapter for the serial console. Check that
jumpers J30 and J31 are **on** (they are on by default when boards ship from
the factory) to connect UART signals to the OpenSDA microcontroller.

Connect a USB cable from your PC to J28.

Use the following settings with your serial terminal of choice (minicom, putty,
etc.):

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1


### Flashing


Here is an example for the hello_world application.

Open a serial terminal, reset the board (press the SW4 button), and you should
see the following message in the terminal:

```console

***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! mimxrt1050_evk//hyperflash
```

### Debugging


Here is an example for the hello_world application.

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```console

***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! mimxrt1050_evk//hyperflash
```

### Troubleshooting


If the debug probe fails to connect with the following error, it's possible
that the boot header in HyperFlash is invalid or corrupted. The boot header is
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
You can fix it by erasing and reprogramming the HyperFlash with the following
steps:

#. Set the SW7 DIP switches to ON-ON-ON-OFF to prevent booting from HyperFlash.

#. Reset by pressing SW4

#. Run `west debug` or `west flash` again with a known working Zephyr
   application.

#. Set the SW7 DIP switches to OFF-ON-ON-OFF to boot from HyperFlash.

#. Reset by pressing SW4
