---
id: "zepb-frdm-k64f-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "frdm_k64f: Programming and Debugging"
summary: "Build and flash applications as usual (see build_an_application and application_run for more details)."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/nxp/frdm_k64f/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/nxp/frdm_k64f/doc/index.html#programming-and-debugging"
license: "Apache-2.0"
mode: "V"
---

Build and flash applications as usual (see build_an_application and
application_run for more details).


### Configuring a Debug Probe


A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the opensda-daplink-onboard-debug-probe.

Early versions of this board have an outdated version of the OpenSDA bootloader
and require an update. Please see the DAPLink Bootloader Update page for
instructions to update from the CMSIS-DAP bootloader to the DAPLink bootloader.


### Configuring a Console


Regardless of your choice in debug probe, we will use the OpenSDA
microcontroller as a usb-to-serial adapter for the serial console.

Connect a USB cable from your PC to J26.

Use the following settings with your serial terminal of choice (minicom, putty,
etc.):

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1


### Flashing


Here is an example for the hello_world application.

Open a serial terminal, reset the board (press the SW1 button), and you should
see the following message in the terminal:

```console

***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! frdm_k64f
```

### Debugging


Here is an example for the hello_world application.

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```console

***** Booting Zephyr OS v1.14.0-rc1 *****
Hello World! frdm_k64f
```

### Troubleshooting


If pyocd raises an uncaught `DAPAccessIntf.TransferFaultError()` exception
when you try to flash or debug, it's possible that the K64F flash may have been
locked by a corrupt application. You can unlock it with the following sequence
of pyocd commands:

```console

$ pyocd cmd
0001915:WARNING:target_kinetis:Forcing halt on connect in order to gain control of device
Connected to K64F [Halted]: 0240000026334e450028400d5e0e000e4eb1000097969900
>>> unlock
0016178:WARNING:target_kinetis:K64F secure state: unlocked successfully
>>> reinit
0034584:WARNING:target_kinetis:Forcing halt on connect in order to gain control of device
>>> load build/zephyr/zephyr.bin
[====================] 100%
>>> reset
Resetting target
>>> quit
```
