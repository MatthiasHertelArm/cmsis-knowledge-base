---
id: "zepb-rpi-pico-programmable-i-o-pio"
type: "concept"
domain: "bring-up"
title: "rpi_pico: Programmable I/O (PIO)"
summary: "The RP2040 SoC comes with two PIO peripherals. These are two simple co-processors that are designed for I/O operations. The PIOs run a custom instruction set, generated from a custom assembly language."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/raspberrypi/rpi_pico/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/raspberrypi/rpi_pico/doc/index.html#programmable-i-o-pio"
license: "Apache-2.0"
mode: "V"
---

The RP2040 SoC comes with two PIO peripherals. These are two simple
co-processors that are designed for I/O operations. The PIOs run
a custom instruction set, generated from a custom assembly language.
PIO programs are assembled using `pioasm`, a tool provided by Raspberry Pi.

Zephyr does not (currently) assemble PIO programs. Rather, they should be
manually assembled and embedded in source code. An example of how this is done
can be found at `drivers/serial/uart_rpi_pico_pio.c`.


### Sample:  SPI via PIO


The `samples/sensor/bme280/README.rst` sample includes a
demonstration of using the PIO SPI driver to communicate with an
environmental sensor.  The PIO SPI driver supports using any
combination of GPIO pins for an SPI bus, as well as allowing up to
four independent SPI buses on a single board (using the two SPI
devices as well as both PIO devices).


### PIO Based Features


Raspberry Pi Pico's PIO is a programmable chip that can implement a variety of peripherals.


* - Peripheral
  - Kconfig option
  - Devicetree compatible
* - UART (PIO)
  - `CONFIG_SERIAL`
  - `raspberrypi,pico-uart-pio`
* - SPI (PIO)
  - `CONFIG_SPI`
  - `raspberrypi,pico-spi-pio`
* - WS2812 (PIO)
  - `CONFIG_LED_STRIP`
  - `worldsemi,ws2812-rpi_pico-pio`
