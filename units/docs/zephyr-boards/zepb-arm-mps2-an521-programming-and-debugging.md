---
id: "zepb-arm-mps2-an521-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "ARM MPS2+ AN521: Programming and Debugging"
summary: "MPS2+ AN521 (CPU0) supports the Armv8m Security Extension. Applications built for the mps2/an521 board by default boot in the Secure state."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/arm/mps2/doc/mps2_an521.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/arm/mps2/doc/index.html#programming-and-debugging"
license: "Apache-2.0"
mode: "V"
---

MPS2+ AN521 (CPU0) supports the Armv8m Security Extension.
Applications built for the mps2/an521 board by default
boot in the Secure state.

MPS2+ AN521 (CPU1) does not support the Armv8m Security Extension.


### Building Secure/Non-Secure Zephyr applications with Arm® TrustZone®


Applications on the MPS2+ AN521 (CPU0) may contain a Secure and a Non-Secure
firmware image. The Secure image can be built using either Zephyr
or Trusted Firmware M (TF-M). Non-Secure firmware images are always built
using Zephyr. The two alternatives are described below.


**Note:** By default the Secure image for the MPS2+ AN521 (CPU0) is built using TF-M.


#### Building the Secure firmware with TF-M


The process to build the Secure firmware image using TF-M and the Non-Secure
firmware image using Zephyr requires the following steps:

1. Build the Non-Secure Zephyr application
   for MPS2+ AN521 (CPU0) using `-DBOARD=mps2/an521/cpu0/ns`.
   To invoke the building of TF-M the Zephyr build system requires the
   Kconfig option `BUILD_WITH_TFM` to be enabled, which is done by
   default when building Zephyr as a Non-Secure application.
   The Zephyr build system will perform the following steps automatically:

      * Build the Non-Secure firmware image as a regular Zephyr application
      * Build a TF-M (secure) firmware image
      * Merge the output image binaries together
      * Optionally build a bootloader image (MCUboot)


**Note:** Depending on the TF-M configuration, an application DTS overlay may be required, to adjust the Non-Secure image Flash and SRAM starting address and sizes.


#### Building the Secure firmware using Zephyr


The process to build the Secure and the Non-Secure firmware images
using Zephyr requires the following steps:

1. Build the Secure Zephyr application for MPS2+ AN521 (CPU0)
   using `-DBOARD=mps2/an521` and
   `CONFIG_TRUSTED_EXECUTION_SECURE=y` and `CONFIG_BUILD_WITH_TFM=n`
   in the application project configuration file.
2. Build the Non-Secure Zephyr application for MPS2+ AN521 (CPU0)
   using `-DBOARD=mps2/an521/cpu0/ns`.
3. Merge the two binaries together.


### Building a Secure only application on MPS2+ AN521 (CPU0)


Build the Zephyr app in the usual way (see build_an_application
and application_run), using `-DBOARD=mps2/an521` for
the firmware running on the MPS2+ AN521 (CPU0).

When building a Secure/Non-Secure application for the MPS2+ AN521 (CPU0),
the Secure application will have to set the SAU/IDAU configuration to allow
Non-Secure access to all CPU resources utilized by the Non-Secure application
firmware. SAU/IDAU configuration shall take place before jumping to the
Non-Secure application.

The following system components are required to be properly configured during the
secure firmware:

- AHB5 TrustZone Memory Protection Controller (MPC)
- AHB5 TrustZone Peripheral Protection Controller (PPC)
- Implementation-Defined Attribution Unit (IDAU)

For more details refer to Corelink SSE-200 Subsystem.




### Building standalone applications on MPS2+ AN521 CPU1


Applications may be built for the second Cortex-M33
(remote) core of MPS2+ AN521. The core is referred to as CPU1.

Build the Zephyr app in the usual way (see build_an_application
and application_run), using `-DBOARD=mps2/an521/cpu1` for
the firmware running on the MPS2+ AN521 (CPU1).

The Zephyr build will automatically trigger building a minimal (empty)
secure-only firmware for CPU0, which will be used to boot the remote
core (CPU1).



### Flashing


MPS2+ AN521 provides:

- A USB connection to the host computer, which exposes a Mass Storage
- A Serial Port which is J10 on MPS2+ board

Build applications as described above.
Here is an example for the hello_world application built as
a secure-only application for CPU0.

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board, and you should see the following message on the corresponding
serial port:

```console

Hello World! mps2_an521
```

#### Uploading an application to MPS2+ AN521


Applications can be in elf, hex or bin format. The binaries are flashed when
the board boots up, using files stored on the on-board Micro SD card. The
Motherboard Configuration Controller (MCC) is responsible for loading the FPGA
image and binaries.

Connect the MPS2+ to your host computer using the USB port. You should see a
USB connection exposing a Mass Storage (`V2M_MPS2` by default).

The update requires 3 steps:

1. Copy application files to `<MPS2 device name>/SOFTWARE/`.
2. Open `<MPS2 device name>/MB/HBI0263C/AN521/images.txt`.
3. Update the `AN521/images.txt` file as follows:

```bash

TITLE: Versatile Express Images Configuration File

[IMAGES]
TOTALIMAGES: 1 ;Number of Images (Max: 32)

IMAGE0ADDRESS: 0x10000000 ;Please select the required executable program

IMAGE0FILE: \SOFTWARE\zephyr.bin
```
Reset the board, and you should see the following message on the corresponding
serial port:

```console

Hello World! mps2_an521
```

**Note:** Refer to the tfm_integration sample for more details about integrating with TF-M and multiple images scenario.

.. _MPS2+ AN521 Technical Reference Manual (TRM):
   https://developer.arm.com/documentation/dai0521/latest/

.. _AMBA®:
   https://developer.arm.com/products/architecture/system-architectures/amba
