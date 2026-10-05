---
id: "alp-new-debug-targets-armds-dstream-before-you-begin"
type: "concept"
domain: "debug"
title: "Add new debug targets to Arm Development Studio: Debug connection with Arm DSTREAM: Before you begin"
summary: "You should have Arm Development Studio installed and your license configured. Refer to the Arm Development Studio install guide for more information."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/new_debug_targets_armds/dstream.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/new_debug_targets_armds/dstream/#before-you-begin"
license: "CC-BY-SA-4.0"
mode: "V"
---

You should have Arm Development Studio installed and your license configured. Refer to the [Arm Development Studio install guide](https://learn.arm.com/install-guides/armds/) for more information.

It is assumed you have access to a DSTREAM unit, and an appropriate development board. For this example, you shall use an [MPS2+](https://developer.arm.com/Tools%20and%20Software/MPS2%20Plus%20FPGA%20Prototyping%20Board) programmed for Cortex-M3 (`AN385`), which is the same hardware as modeled by the FVPs in the previous section.

### Updating IP Address

By default, DSTREAM units are provided with DHCP enabled, allowing the network to specify the IP address. If you wish to set to a fixed IP address, in the Development Studio IDE open the `Debug Hardware Configure IP` view (`Windows > Open View`), Browse for your DSTREAM unit, and set as appropriate. Note if your network does not support DHCP you should use USB to connect to the unit for this step.

### Updating firmware

Firmware for the DSTREAM family is provided with Arm Development Studio, and generally needs to be updated when a new version of Development Studio is released. To manually update the firmware, open the `Debug Hardware Firmware Installer`. Browse for your DSTREAM, and install. The unit will reboot when complete.
