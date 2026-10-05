---
id: "zepb-nrf52840dk-hardware"
type: "concept"
domain: "bring-up"
title: "nrf52840dk: Hardware"
summary: "nRF52840 DK has two external oscillators. The frequency of the slow clock is 32.768 kHz. The frequency of the main clock is 32 MHz."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/nordic/nrf52840dk/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/nordic/nrf52840dk/doc/index.html#hardware"
license: "Apache-2.0"
mode: "V"
---

nRF52840 DK has two external oscillators. The frequency of the slow clock
is 32.768 kHz. The frequency of the main clock is 32 MHz.


### Supported Features


See nRF52840 DK website and nRF52840 DK Hardware guide
for a complete list of nRF52840 Development Kit board hardware features.


### Connections and IOs



#### LED


* LED1 (green) = P0.13
* LED2 (green) = P0.14
* LED3 (green) = P0.15
* LED4 (green) = P0.16


#### Push buttons


* BUTTON1 = SW1 = P0.11
* BUTTON2 = SW2 = P0.12
* BUTTON3 = SW3 = P0.24
* BUTTON4 = SW4 = P0.25
* BOOT = SW5 = boot/reset
