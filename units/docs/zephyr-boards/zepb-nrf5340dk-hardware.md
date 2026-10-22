---
id: "zepb-nrf5340dk-hardware"
type: "concept"
domain: "bring-up"
title: "nrf5340dk: Hardware"
summary: "nRF5340 DK has two external oscillators. The frequency of the slow clock is 32.768 kHz. The frequency of the main clock is 32 MHz."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/nordic/nrf5340dk/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/nordic/nrf5340dk/doc/index.html#hardware"
license: "Apache-2.0"
mode: "V"
---

nRF5340 DK has two external oscillators. The frequency of
the slow clock is 32.768 kHz. The frequency of the main clock
is 32 MHz.


### Supported Features


See nRF5340 DK Product Specification
for a complete list of nRF5340 DK board hardware features.


### Connections and IOs



#### LED


* LED1 (green) = P0.28
* LED2 (green) = P0.29
* LED3 (green) = P0.30
* LED4 (green) = P0.31


#### Push buttons


* BUTTON1 = SW1 = P0.23
* BUTTON2 = SW2 = P0.24
* BUTTON3 = SW3 = P0.8
* BUTTON4 = SW4 = P0.9
* BOOT = SW5 = boot/reset


### Security components


- Implementation Defined Attribution Unit (IDAU) on the application core.
  The IDAU is implemented with the System Protection Unit and is used to
  define secure and non-secure memory maps.  By default, all of the memory
  space  (Flash, SRAM, and peripheral address space) is defined to be secure
  accessible only.
- Secure boot.
