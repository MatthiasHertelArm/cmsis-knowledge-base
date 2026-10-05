---
id: "zepb-rpi-pico2-hardware"
type: "concept"
domain: "bring-up"
title: "rpi_pico2: Hardware"
summary: "The default pin mapping is unchanged from the Pico 1 (see rpi_pico_pin_mapping)."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/raspberrypi/rpi_pico2/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/raspberrypi/rpi_pico2/doc/index.html#hardware"
license: "Apache-2.0"
mode: "V"
---

- Dual Cortex-M33 or Hazard3 processors at up to 150MHz
- 520KB of SRAM, and 4MB of on-board flash memory
- USB 1.1 with device and host support
- Low-power sleep and dormant modes
- Drag-and-drop programming using mass storage over USB
- 26 multi-function GPIO pins including 3 that can be used for ADC
- 2 SPI, 2 I2C, 2 UART, 3 12-bit 500ksps Analogue to Digital - Converter (ADC), 24 controllable PWM channels
- 2 Timer with 4 alarms, 1 AON Timer
- Temperature sensor
- 3 Programmable IO (PIO) blocks, 12 state machines total for custom peripheral support
- Infineon CYW43439 2.4 GHz Wi-Fi chip (Pico 2W only)

  - Flexible, user-programmable high-speed IO
  - Can emulate interfaces such as SD Card and VGA


### Supported Features



### Connections and IOs


The default pin mapping is unchanged from the Pico 1 (see rpi_pico_pin_mapping).
