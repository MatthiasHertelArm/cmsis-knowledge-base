---
id: "zepb-frdm-mcxn947-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "frdm_mcxn947: Programming and Debugging"
summary: "Build and flash applications as usual (see build_an_application and application_run for more details)."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/nxp/frdm_mcxn947/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/nxp/frdm_mcxn947/doc/index.html#programming-and-debugging"
license: "Apache-2.0"
mode: "V"
---

Build and flash applications as usual (see build_an_application and
application_run for more details).


### Configuring a Debug Probe


A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the MCU-Link CMSIS-DAP Onboard Debug Probe.


#### Using LinkServer


Linkserver is the default runner for this board, and supports the factory
default MCU-Link firmware. Follow the instructions in
mcu-link-cmsis-onboard-debug-probe to reprogram the default MCU-Link
firmware. This only needs to be done if the default onboard debug circuit
firmware was changed. To put the board in `DFU mode` to program the firmware,
short jumper J21.


#### Using J-Link


There are two options. The onboard debug circuit can be updated with Segger
J-Link firmware by following the instructions in
mcu-link-jlink-onboard-debug-probe.
To be able to program the firmware, you need to put the board in `DFU mode`
by shortening the jumper J21.
The second option is to attach a jlink-external-debug-probe to the
10-pin SWD connector (J23) of the board. Additionally, the jumper J19 must
be shortened.
For both options use the `-r jlink` option with west to use the jlink runner.

```console

west flash -r jlink
```

### Configuring a Console


Connect a USB cable from your PC to J17, and use the serial terminal of your choice
(minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1


### Flashing


Here is an example for the hello_world application.

Open a serial terminal, reset the board (press the RESET button), and you should
see the following message in the terminal:

```console

*** Booting Zephyr OS build v3.6.0-479-g91faa20c6741 ***
Hello World! frdm_mcxn947/mcxn947/cpu0
```

#### Building a dual-core image


The dual-core samples are run using `frdm_mcxn947/mcxn947/cpu0` target.

Images built for `frdm_mcxn947/mcxn947/cpu1` will be loaded from flash
and executed on the second core when `CONFIG_SECOND_CORE_MCUX` is selected.

For an example of building for both cores with System Build, see
`samples/subsys/ipc/ipc_service/static_vrings`

Here is an example for the mbox_data application.


### Debugging


Here is an example for the hello_world application.

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```console

*** Booting Zephyr OS build v3.6.0-479-g91faa20c6741 ***
Hello World! frdm_mcxn947/mcxn947/cpu0
```

#### Debugging a dual-core image


For dual core builds, the secondary core should be placed into a loop,
then a debugger can be attached.
As a reference please see (AN13264, section 4.2.3 for more information).
The reference is for the RT1170 but similar technique can be also used here.


### Using QSPI board variant

The FRDM-MCXN947 board includes an external QSPI flash.  The MCXN947 can boot and
XIP directly from this flash using the FlexSPI interface.  The QSPI variant
enables building applications and code to execute from the QSPI.


#### Programming the ROM bootloader for external QSPI

By default, the MCXN947 bootloader in ROM will boot using internal flash.  But
the MCU can be programmed to boot from external memory on the FlexSPI interface.
Before using the QSPI board variant, the board should be programmed to boot from
QSPI using the steps below.

To configure the ROM bootloader, the Protected Flash Region (PFR) must be
programmed.  Programming the PFR is done using NXP's ROM bootloader tools.
Some simple steps are provided in NXP's
MCUXpresso SDK example hello_world_qspi_xip readme.  The binary to program
with blhost is found at bootfromflexspi.bin.  A much more detailed explanation
is available at this post Running code from external memory with MCX N94x.
The steps below program the FRDM-MCXN947 board.  Note that these steps interface
to the ROM bootloader through the UART serial port, but USB is another option.

1. Disconnect any terminal from the UART serial port, since these steps use that
   serial port.
#. Connect a USB Type-C cable to the host computer and J17 on the board, in the
   upper left corner.  This powers the board, connects the debug probe, and
   connects the UART serial port used for the `blhost` command.
#. Place the MCU in ISP mode.  On the FRDM-MCXN947 board, the ISP button
   can be used for this.  Press and hold the ISP button SW3, on the bottom right
   corner of the board.  Press and release the Reset button SW1 on the upper left
   corner of the board.  The MCU has booted into ISP mode.  Release the ISP
   button.
#. Run the `blhost` command:

Successful programming should look something like this:

```console

$ blhost -t 2000 -p /dev/ttyACM0,115200 -j -- write-memory 0x01004000 bootfromflexspi.bin
{
   "command": "write-memory",
   "response": [
      256
   ],
   "status": {
      "description": "0 (0x0) Success.",
      "value": 0
   }
}
```
5. Reset the board with SW1 to exit ISP mode.  Now the MCU is ready to boot from
   QSPI.

The ROM bootloader can be configured to boot from internal flash again.  Repeat
the steps above to program the PFR, and program the file bootfromflash.bin.


#### Build, flash, and debug with the QSPI variant


Once the PFR is programmed to boot from QSPI, the normal Zephyr steps to build,
flash, and debug can be used with the QSPI board variant.  Here are some examples.

Here is an example for the hello_world application:

MCUboot can also be used with the QSPI variant.  By default, this places the
MCUboot bootloader in the `boot-partition` in QSPI flash, with the application
images.  The ROM bootloader will boot first and load MCUboot in the QSPI, which
will load the app.  This example builds and loads the blinky
sample with MCUboot using Sysbuild:

Open a serial terminal, reset the board with the SW1 button, and the console
will print:

```console

*** Booting MCUboot vX.Y.Z ***
*** Using Zephyr OS build vX.Y.Z ***
I: Starting bootloader
I: Image index: 0, Swap type: none
I: Bootloader chainload address offset: 0x14000
I: Image version: v0.0.0
I: Jumping to the first image slot
*** Booting Zephyr OS build vX.Y.Z ***
LED state: OFF
LED state: ON
```
