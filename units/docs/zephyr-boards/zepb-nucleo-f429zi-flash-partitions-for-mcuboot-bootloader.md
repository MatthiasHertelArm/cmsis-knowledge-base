---
id: "zepb-nucleo-f429zi-flash-partitions-for-mcuboot-bootloader"
type: "concept"
domain: "bring-up"
title: "nucleo_f429zi: Flash partitions for MCUBoot bootloader"
summary: "The on-board STM32F429ZI MCU has 2MBs of internal flash memory. To use MCUboot, define a Zephyr partition table for the flash memory in its devicetree file nucleo_f429zi.dts."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/st/nucleo_f429zi/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/st/nucleo_f429zi/doc/index.html#flash-partitions-for-mcuboot-bootloader"
license: "Apache-2.0"
mode: "V"
---

The on-board STM32F429ZI MCU has 2MBs of internal flash memory. To use MCUboot,
define a Zephyr partition table for the flash memory in
its devicetree file `nucleo_f429zi.dts`. As a reference, a partition table for
MCUBoot is already defined in the devicetree file, with these settings:

- MCUBoot bootloader partition takes 64K bytes.
- Zephyr settings partition takes 64K bytes.
- Application image takes 256K bytes in Slot 0 partition.
- Updating image takes another 256K bytes in Slot 1 partition.
- A scratch partition with 128K is required for image swap.

A specific application can adjust each partition size based on its needs.


.. _STM32F429ZI on www.st.com:
   https://www.st.com/en/microcontrollers/stm32f429zi.html
