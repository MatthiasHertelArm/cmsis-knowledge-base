---
id: "zepb-nrf5340dk-testing-the-leds-and-buttons-in-the-nrf5"
type: "concept"
domain: "bring-up"
title: "nrf5340dk: Testing the LEDs and buttons in the nRF5340 DK"
summary: "There are 2 samples that allow you to test that the buttons (switches) and LEDs on the board are working properly with Zephyr:"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/nordic/nrf5340dk/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/nordic/nrf5340dk/doc/index.html#testing-the-leds-and-buttons-in-the-nrf5340-dk"
license: "Apache-2.0"
mode: "V"
---

There are 2 samples that allow you to test that the buttons (switches) and
LEDs on the board are working properly with Zephyr:

* blinky
* button

You can build and flash the examples to make sure Zephyr is running correctly on
your board. The button and LED definitions can be found in
`boards/nordic/nrf5340dk/nrf5340_cpuapp_common.dtsi`.
