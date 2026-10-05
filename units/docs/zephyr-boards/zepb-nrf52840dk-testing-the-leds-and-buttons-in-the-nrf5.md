---
id: "zepb-nrf52840dk-testing-the-leds-and-buttons-in-the-nrf5"
type: "concept"
domain: "bring-up"
title: "nrf52840dk: Testing the LEDs and buttons in the nRF52840 DK"
summary: "There are 2 samples that allow you to test that the buttons (switches) and LEDs on the board are working properly with Zephyr:"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/nordic/nrf52840dk/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/nordic/nrf52840dk/doc/index.html#testing-the-leds-and-buttons-in-the-nrf52840-dk"
license: "Apache-2.0"
mode: "V"
---

There are 2 samples that allow you to test that the buttons (switches) and LEDs on
the board are working properly with Zephyr:

```console

samples/basic/blinky
samples/basic/button
```
You can build and flash the examples to make sure Zephyr is running correctly on
your board. The button and LED definitions can be found in
`boards/nordic/nrf52840dk/nrf52840dk_nrf52840.dts`.
