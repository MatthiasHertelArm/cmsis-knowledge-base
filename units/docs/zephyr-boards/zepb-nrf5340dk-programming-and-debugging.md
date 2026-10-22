---
id: "zepb-nrf5340dk-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "nrf5340dk: Programming and Debugging"
summary: "nRF5340 application core supports the Armv8-M Security Extension. Applications built for the nrf5340dk/nrf5340/cpuapp board by default boot in the Secure state."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/nordic/nrf5340dk/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/nordic/nrf5340dk/doc/index.html#programming-and-debugging"
license: "Apache-2.0"
mode: "V"
---

nRF5340 application core supports the Armv8-M Security Extension.
Applications built for the `nrf5340dk/nrf5340/cpuapp` board by default
boot in the Secure state.

nRF5340 network core does not support the Armv8-M Security Extension.
nRF5340 IDAU may configure bus accesses by the nRF5340 network core
to have Secure attribute set; the latter allows to build and run
Secure only applications on the nRF5340 SoC.


### Building Secure/Non-Secure Zephyr applications with Arm® TrustZone®


Applications on the nRF5340 may contain a Secure and a Non-Secure firmware
image for the application core. The Secure image can be built using either
Zephyr or Trusted Firmware M (TF-M). Non-Secure firmware
images are always built using Zephyr. The two alternatives are described below.


**Note:** By default the Secure image for nRF5340 application core is built using TF-M.


#### Building the Secure firmware with TF-M


The process to build the Secure firmware image using TF-M and the Non-Secure
firmware image using Zephyr requires the following steps:

1. Build the Non-Secure Zephyr application
   for the application core using `-DBOARD=nrf5340dk/nrf5340/cpuapp/ns`.
   To invoke the building of TF-M the Zephyr build system requires the
   Kconfig option `BUILD_WITH_TFM` to be enabled, which is done by
   default when building Zephyr as a Non-Secure application.
   The Zephyr build system will perform the following steps automatically:

      * Build the Non-Secure firmware image as a regular Zephyr application
      * Build a TF-M (secure) firmware image
      * Merge the output image binaries together
      * Optionally build a bootloader image (MCUboot)


**Note:** Depending on the TF-M configuration, an application DTS overlay may be required, to adjust the Non-Secure image Flash and SRAM starting address and sizes.

2. Build the application firmware for the network core using
   `-DBOARD=nrf5340dk/nrf5340/cpunet`.



#### Building the Secure firmware using Zephyr


The process to build the Secure and the Non-Secure firmware images
using Zephyr requires the following steps:

1. Build the Secure Zephyr application for the application core
   using `-DBOARD=nrf5340dk/nrf5340/cpuapp` and
   `CONFIG_TRUSTED_EXECUTION_SECURE=y` and `CONFIG_BUILD_WITH_TFM=n`
   in the application project configuration file.
2. Build the Non-Secure Zephyr application for the application core
   using `-DBOARD=nrf5340dk/nrf5340/cpuapp/ns`.
3. Merge the two binaries together.
4. Build the application firmware for the network core using
   `-DBOARD=nrf5340dk/nrf5340/cpunet`.


When building a Secure/Non-Secure application for the nRF5340 application core,
the Secure application will have to set the IDAU (SPU) configuration to allow
Non-Secure access to all CPU resources utilized by the Non-Secure application
firmware. SPU configuration shall take place before jumping to the Non-Secure
application.


### Building a Secure only application


Build the Zephyr app in the usual way (see build_an_application
and application_run), using `-DBOARD=nrf5340dk/nrf5340/cpuapp` for
the firmware running on the nRF5340 application core, and using
`-DBOARD=nrf5340dk/nrf5340/cpunet` for the firmware running
on the nRF5340 network core.


### Flashing


Follow the instructions in the nordic_segger page to install
and configure all the necessary software. Further information can be
found in nordic_segger_flashing. Then you can build and flash
applications as usual (build_an_application and
application_run for more details).


**Warning:** The nRF5340 has a flash read-back protection feature. When flash read-back protection is active, you will need to recover the chip before reflashing. If you are flashing with west, run this command for more details on the related `--recover` option: .. code-block:: console west flash -H -r nrfutil --no-rebuild


**Note:** Flashing and debugging applications on the nRF5340 DK requires upgrading the nRF Command Line Tools to version 10.12.0. Further information on how to install the nRF Command Line Tools can be found in nordic_segger_flashing.

Here is an example for the hello_world application running on the
nRF5340 application core.

First, run your favorite terminal program to listen for output.

```console

$ minicom -D <tty_device> -b 115200
```
Replace `<tty_device>` with the port where the board nRF5340 DK
can be found. For example, under Linux, `/dev/ttyACM0`.

Then build and flash the application in the usual way.


### Debugging


Refer to the nordic_segger page to learn about debugging Nordic
boards with a Segger IC.
