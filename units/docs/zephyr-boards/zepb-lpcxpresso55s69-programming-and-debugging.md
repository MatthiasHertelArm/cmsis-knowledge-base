---
id: "zepb-lpcxpresso55s69-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "lpcxpresso55s69: Programming and Debugging"
summary: "Build and flash applications as usual (see build_an_application and application_run for more details)."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/nxp/lpcxpresso55s69/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/nxp/lpcxpresso55s69/doc/index.html#programming-and-debugging"
license: "Apache-2.0"
mode: "V"
---

Build and flash applications as usual (see build_an_application and
application_run for more details).


### Configuring a Debug Probe


LinkServer is the default runner for this board.
A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the integrated lpc-link2-onboard-debug-probe
in the CMSIS-DAP mode. To use this probe with Zephyr, you need to install the
linkserver-debug-host-tools and make sure they are in your search path.
Refer to the detailed overview about application_debugging for additional
information.

The integrated LPC-Link2 hardware can also be used as a J-Link probe with a
firmware update, as described in lpclink2-jlink-onboard-debug-probe.
The jlink-debug-host-tools should be available in this case.


### Configuring a Console


Connect a USB cable from your PC to P6, and use the serial terminal of your choice
(minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1


### Flashing


Here is an example for the hello_world application. This example uses the
linkserver-debug-host-tools as default.

Open a serial terminal, reset the board (press the RESET button), and you should
see the following message in the terminal:

```console

***** Booting Zephyr OS v3.7.0 *****
Hello World! lpcxpresso55s69/lpc55s69/cpu0
```

#### Building and flashing secure/non-secure with Arm® TrustZone®

The TF-M integration samples can be run using the
`lpcxpresso55s69/lpc55s69/cpu0/ns` target. To run we need to manually flash
the resulting image (`tfm_merged.hex`) with a J-Link as follows
(reset and erase are for recovering a locked core):

```console

JLinkExe -device lpc55s69 -if swd -speed 2000 -autoconnect 1
J-Link>r
J-Link>erase
J-Link>loadfile build/zephyr/tfm_merged.hex
```
We need to reset the board manually after flashing the image to run this code.


#### Building a dual-core image

The dual-core samples are run using `lpcxpresso55s69/lpc55s69/cpu0` target.
Images built for `lpcxpresso55s69/lpc55s69/cpu1` will be loaded from flash
and executed on the second core when `SECOND_CORE_MCUX` is selected. For
an example of building for both cores with sysbuild, see
`samples/subsys/ipc/openamp/`


### Debugging


Here is an example for the hello_world application. This example uses the
linkserver-debug-host-tools as default.

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```console

***** Booting Zephyr OS zephyr-v1.14.0 *****
Hello World! lpcxpresso55s69
```
