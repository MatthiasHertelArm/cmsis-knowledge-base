---
id: "zepb-mps3-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "mps3: Programming and Debugging"
summary: "You can build applications in the usual way. Here is an example for the hello_world application with AN547."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/arm/mps3/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/arm/mps3/doc/index.html#programming-and-debugging"
license: "Apache-2.0"
mode: "V"
---

### Flashing


MPS3 provides:

- A USB connection to the host computer, which exposes Mass Storage and
  CMSIS-DAP, and serial ports.


#### Building an application with AN547


You can build applications in the usual way. Here is an example for
the hello_world application with AN547.

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board, and you should see the following message on the corresponding
serial port:

```console

Hello World! mps3
```

#### Uploading an application to MPS3 AN547


Applications can be in elf, hex or bin format. The binaries are flashed when
the board boots up, using files stored on the on-board Micro SD card. The
Motherboard Configuration Controller (MCC) is responsible for loading the FPGA
image and binaries.

Connect the MPS3 to your host computer using the USB port. You should see a
USB connection exposing a Mass Storage (`V2M-MPS3` by default).

The update requires 3 steps:

1. Copy application files to `<MPS3 device name>/SOFTWARE/`.
2. Open `<MPS3 device name>/MB/HBI0309C/AN547/images.txt`.
3. Update the `images.txt` file as follows:

```bash

TITLE: Versatile Express Images Configuration File

[IMAGES]
TOTALIMAGES: 1 ;Number of Images (Max: 32)

IMAGE0ADDRESS: 0x01000000 ;Please select the required executable program

IMAGE0FILE: \SOFTWARE\zephyr.elf
```
Reset the board, and you should see the following message on the corresponding
serial port:

```console

Hello World! mps3
```

#### Building and running an application with AN536


You can build applications in the usual way. Here is an example for
the hello_world application with AN536.

To run the application with QEMU:

You should see the following message:

```console

Hello World! mps3/an536/cpu0
```
For more details refer to:
 - MPS3 AN536 Application Note
 - MPS3 AN547 Technical Reference Manual (TRM)
 - MPS3 AN552 Technical Reference Manual (TRM)
 - MPS3 AN555 Technical Reference Manual (TRM)
 - MPS3 FPGA Prototyping Board Technical Reference Manual (TRM)
 - Cortex R52 Technical Reference Manual
 - Cortex M55 Generic User Guide
 - Cortex M85 Generic User Guide
 - Corelink SSE-300 Example Subsystem
 - Corelink SSE-310 Example Subsystem

.. _MPS3 AN547 Technical Reference Manual (TRM):
   https://developer.arm.com/-/media/Arm%20Developer%20Community/PDF/DAI0547B_SSE300_PLUS_U55_FPGA_for_mps3.pdf

.. _MPS3 AN552 Technical Reference Manual (TRM):
   https://developer.arm.com/documentation/dai0552/latest

.. _MPS3 AN555 Technical Reference Manual (TRM):
   https://developer.arm.com/documentation/107642/latest

.. _MPS3 FPGA Prototyping Board Technical Reference Manual (TRM):
   https://developer.arm.com/documentation/100765/latest
