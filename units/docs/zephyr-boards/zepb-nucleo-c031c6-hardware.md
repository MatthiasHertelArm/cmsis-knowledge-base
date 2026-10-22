---
id: "zepb-nucleo-c031c6-hardware"
type: "concept"
domain: "bring-up"
title: "nucleo_c031c6: Hardware"
summary: "Nucleo C031C6 provides the following hardware components:"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/st/nucleo_c031c6/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/st/nucleo_c031c6/doc/index.html#hardware"
license: "Apache-2.0"
mode: "V"
---

Nucleo C031C6 provides the following hardware components:

- STM32 microcontroller in 48-pin package featuring 32 Kbytes of Flash memory
  and 12 Kbytes of SRAM.
- Extension resource:

  - Arduino* Uno V3 connectivity

- On-board ST-LINK/V2-1 debugger/programmer with SWD connector:

- Flexible board power supply:

  - USB VBUS or external source (3.3V, 5V, 7 - 12V)
  - Current consumption measurement (IDD)

- Four LEDs:

  - USB communication (LD1), USB power fault LED (LD2), power LED (LD3),
    user LED (LD4)

- Two push-button: USER and RESET

- USB re-enumeration capability. Three different interfaces supported on USB:

  - Virtual COM port
  - Mass storage
  - Debug port

More information about STM32C031C6 can be found here:
STM32C0x1 reference manual


### Supported Features



### Connections and IOs


Each of the GPIO pins can be configured by software as output (push-pull or open-drain), as
input (with or without pull-up or pull-down), or as peripheral alternate function. Most of the
GPIO pins are shared with digital or analog alternate functions. All GPIOs are high current
capable except for analog inputs.


#### Default Zephyr Peripheral Mapping:


- UART_2 TX/RX : PA2/PA3 (ST-Link Virtual Port Com)
- LD4       : PA5

For more details please refer to STM32 Nucleo-64 board User Manual.
