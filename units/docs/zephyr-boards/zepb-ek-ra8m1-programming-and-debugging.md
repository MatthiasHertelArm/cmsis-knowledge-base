---
id: "zepb-ek-ra8m1-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "ek_ra8m1: Programming and Debugging"
summary: "Applications for the ek_ra8m1 board configuration can be built, flashed, and debugged in the usual way. See build_an_application and application_run for more details on building and running."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/renesas/ek_ra8m1/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/renesas/ek_ra8m1/doc/index.html#programming-and-debugging"
license: "Apache-2.0"
mode: "V"
---

Applications for the `ek_ra8m1` board configuration can be
built, flashed, and debugged in the usual way. See
build_an_application and application_run for more details on
building and running.

**Note:** Only support from SDK v0.16.6 in which GCC for Cortex Arm-M85 was available.
To build for EK-RA8M1 user need to get and install GNU Arm Embedded toolchain from https://github.com/zephyrproject-rtos/sdk-ng/releases/tag/v0.16.6


### Flashing


Program can be flashed to EK-RA8M1 via the on-board SEGGER J-Link debugger.
SEGGER J-link's drivers are available at https://www.segger.com/downloads/jlink/

To flash the program to board

1. Connect to J-Link OB via USB port to host PC

2. Make sure J-Link OB jumper is in default configuration as describe in EK-RA8M1 - User's Manual

3. Execute west command

```console

west flash -r jlink
```

### Debugging


You can use Segger Ozone (Segger Ozone Download) for a visual debug interface

Once downloaded and installed, open Segger Ozone and configure the debug project
like so:

* Target Device: R7FA8M1AH
* Target Interface: SWD
* Target Interface Speed: 4 MHz
* Host Interface: USB
* Program File: <path/to/your/build/zephyr.elf>

**Note:** It's verified that we can debug OK on Segger Ozone v3.30d so please use this or later
version of Segger Ozone
