---
id: "zepb-rpi-pico2-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "rpi_pico2: Programming and Debugging"
summary: "The overall explanation regarding flashing and debugging is the same as for rpi_pico. See rpi_pico_programming_and_debugging in rpi_pico documentation. N.b. OpenOCD support requires using Raspberry Pi's forked version of OpenOCD."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/raspberrypi/rpi_pico2/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/raspberrypi/rpi_pico2/doc/index.html#programming-and-debugging"
license: "Apache-2.0"
mode: "V"
---

The overall explanation regarding flashing and debugging is the same as for rpi_pico.
See rpi_pico_programming_and_debugging in rpi_pico documentation. N.b. OpenOCD support requires using Raspberry Pi's forked version of OpenOCD.

Below is an example of building and flashing the blinky application.

The blinky sample is not yet supported on Pico 2W, so try the wifi-shell application to connect to the network.


### Wi-Fi Firmware Setup


Before building applications for the Pico 2W variant, you must fetch the required Wi-Fi firmware blobs.
The Infineon CYW43439 chip requires proprietary firmware and CLM (Country Localization Module) files.

Run the following command to download these blobs:

```console

west blobs fetch hal_infineon
```
This command downloads the necessary firmware files from Infineon's repositories, including:

- `43439A0.bin` - Wi-Fi firmware for CYW43439
- `43439A0.clm_blob` - Country localization data

You only need to run this command once per workspace. Without these blobs, the build will fail with
CMake errors about missing firmware files.


### Building Wi-Fi Applications


After fetching the blobs, you can build Wi-Fi applications:
